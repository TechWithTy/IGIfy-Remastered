from __future__ import annotations

from typing import Dict, Iterable, List, Tuple, Sequence

from instagrapi import Client


def _collect_medias_for_hashtag(cl: Client, tag: str, source: str, amount: int) -> List:
    """
    Fetch medias for a hashtag from a chosen source.
    source: 'top' or 'recent'
    """
    tag = tag.lstrip('#').strip()
    if source == 'top':
        try:
            return cl.hashtag_medias_top(tag, amount=amount)  # private preferred
        except Exception:
            try:
                return cl.hashtag_medias_top_gql(tag, amount=amount)  # fallback public
            except Exception:
                return []
    else:
        try:
            return cl.hashtag_medias_recent(tag, amount=amount)
        except Exception:
            try:
                return cl.hashtag_medias_recent_gql(tag, amount=amount)
            except Exception:
                return []


def _sanitize_hashtag_variants(tag: str) -> List[str]:
    tag = tag.strip().lstrip('#')
    variants = [tag]
    if ' ' in tag:
        variants.append(tag.replace(' ', ''))
        variants.append(tag.replace(' ', '_'))
    if '-' in tag:
        variants.append(tag.replace('-', ''))
        variants.append(tag.replace('-', '_'))
    # Deduplicate while preserving order
    seen = set()
    out = []
    for v in variants:
        if v and v not in seen:
            seen.add(v)
            out.append(v)
    return out


def _expand_hashtag_candidates(cl: Client, raw: str, verbose: bool = False) -> List[str]:
    """
    Build a list of candidate hashtag names to try, based on:
    - sanitized variants (spaces/dashes → compact and underscore forms)
    - search_hashtags results (top similar tags)
    - related hashtags (if available)
    """
    base_variants = _sanitize_hashtag_variants(raw)
    candidates: List[str] = list(base_variants)
    # Try search_hashtags to get close matches
    try:
        results = cl.search_hashtags(raw.strip().lstrip('#'))
        for ht in results[:5]:  # take top 5
            name = getattr(ht, 'name', None) or getattr(ht, 'id', None)
            if isinstance(name, str) and name and name not in candidates:
                candidates.append(name)
        if verbose:
            print(f"[debug] search_hashtags('{raw}') → {[c for c in candidates if c not in base_variants]}")
    except Exception as e:
        if verbose:
            print(f"[debug] search_hashtags failed: {e}")
    # Try related hashtags for the first base variant
    try:
        primary = base_variants[0] if base_variants else raw.strip().lstrip('#')
        related = cl.hashtag_related(primary)
        for ht in related[:5]:
            name = getattr(ht, 'name', None) or getattr(ht, 'id', None)
            if isinstance(name, str) and name and name not in candidates:
                candidates.append(name)
        if verbose:
            print(f"[debug] hashtag_related('{primary}') → {[c for c in candidates if c not in base_variants]}")
    except Exception as e:
        if verbose:
            print(f"[debug] hashtag_related failed: {e}")
    if verbose:
        print(f"[debug] candidates for '{raw}': {candidates}")
    return candidates


def build_targets_from_hashtags(
    cl: Client,
    hashtags: Iterable[str],
    media_source: str = 'top',  # 'top' or 'recent'
    media_count: int = 20,
    max_users: int = 100,
    exclude_self: bool = True,
    include_likers: bool = True,
    verbose: bool = False,
    fallback_when_empty: bool = True,
) -> Dict[str, str]:
    """
    Build a dict {username: user_id_str} from the authors of medias
    returned for the given hashtags.

    - media_source: 'top' or 'recent'
    - media_count: medias per hashtag to scan
    - max_users: cap on total unique users collected
    - exclude_self: skip the logged-in user id

    Returns a mapping of username -> user_id (as string) suitable for
    reuse where the original celebrity `users` dict is used.
    """
    collected: Dict[int, str] = {}
    my_id = getattr(cl, 'user_id', None)

    for raw in hashtags:
        tag_variants = _expand_hashtag_candidates(cl, raw, verbose=verbose)
        medias_all: List = []
        for tag in tag_variants[:10]:  # cap expansion attempts
            medias = _collect_medias_for_hashtag(cl, tag, media_source, media_count)
            if verbose:
                print(f"[debug] hashtag='{tag}' source='{media_source}' -> medias={len(medias)}")
            if not medias and fallback_when_empty:
                alt = 'recent' if media_source == 'top' else 'top'
                alt_medias = _collect_medias_for_hashtag(cl, tag, alt, media_count)
                if verbose:
                    print(f"[debug] fallback hashtag='{tag}' source='{alt}' -> medias={len(alt_medias)}")
                medias = alt_medias
            if medias:
                medias_all.extend(medias)
        if not medias_all:
            if verbose:
                print(f"[debug] no medias found for any variant of '{raw}'")
            continue
        for m in medias_all:
            uid = None
            uname = None
            try:
                user = getattr(m, 'user', None)
                if user is not None:
                    uid = getattr(user, 'pk', None)
                    uname = getattr(user, 'username', None)
                # Fallback: try media_info for robust user fetch
                if not uid or not uname:
                    mpk = getattr(m, 'pk', getattr(m, 'id', None))
                    if mpk:
                        mi = cl.media_info(mpk)
                        user2 = getattr(mi, 'user', None)
                        uid = uid or getattr(user2, 'pk', None)
                        uname = uname or getattr(user2, 'username', None)
                # Optionally add likers
                if include_likers:
                    mpk = getattr(m, 'pk', getattr(m, 'id', None))
                    if mpk:
                        try:
                            likers = cl.media_likers(mpk)
                            if verbose:
                                print(f"[debug] media {mpk}: likers={len(likers)}")
                            for lu in likers:
                                lpk = getattr(lu, 'pk', None)
                                lun = getattr(lu, 'username', None)
                                # exclude only if my_id is defined and equals liker
                                if lpk and lun and ((not exclude_self) or (my_id is None) or (lpk != my_id)):
                                    if lpk not in collected:
                                        collected[lpk] = lun
                                        if len(collected) >= max_users:
                                            break
                        except Exception as e:
                            if verbose:
                                print(f"[debug] media {mpk}: likers failed: {e}")
            except Exception:
                uid = None
                uname = None

            if len(collected) >= max_users:
                break
            if not uid or not uname:
                continue
            if exclude_self and my_id and uid == my_id:
                continue
            if uid not in collected and len(collected) < max_users:
                collected[uid] = uname
                if len(collected) >= max_users:
                    break
        if len(collected) >= max_users:
            break

    # Convert to username -> id string mapping
    if verbose:
        print(f"[debug] collected users: {len(collected)}")
    return {name: str(uid) for uid, name in collected.items()}
