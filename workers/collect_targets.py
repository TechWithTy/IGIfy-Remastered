#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import sys

# Ensure repo root is on sys.path when running as a script
try:
    from utilities.client import create_client
    from utilities.targets import build_targets_from_hashtags
except ModuleNotFoundError:
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
    from utilities.client import create_client
    from utilities.targets import build_targets_from_hashtags


def main():
    p = argparse.ArgumentParser(description="Collect target users from hashtag authors and save as JSON mapping (username -> user_id)")
    p.add_argument("-u", "--username", required=True, help="Instagram username or email")
    p.add_argument("-p", "--password", required=True, help="Instagram password")
    p.add_argument("-t", "--tags", nargs="+", required=True, help="Hashtags to scan (without #)")
    p.add_argument("-o", "--out", default="targets.json", help="Output JSON file path")
    p.add_argument("--session", help="Path to instagrapi settings JSON (optional)")
    p.add_argument("--source", choices=["top", "recent"], default="top", help="Use top or recent medias")
    p.add_argument("--media-count", type=int, default=20, help="Medias per hashtag to scan")
    p.add_argument("--max-users", type=int, default=100, help="Cap on collected users")
    p.add_argument("--include-self", action="store_true", help="Include your own account if encountered")
    p.add_argument("--no-likers", action="store_true", help="Do not include likers of medias (authors only)")
    p.add_argument("--verbose", action="store_true", help="Print debug info while collecting")
    args = p.parse_args()

    cl = create_client(
        username=args.username,
        password=args.password,
        session_path=args.session,
    )

    mapping = build_targets_from_hashtags(
        cl=cl,
        hashtags=args.tags,
        media_source=args.source,
        media_count=args.media_count,
        max_users=args.max_users,
        exclude_self=not args.include_self,
        include_likers=not args.no_likers,
        verbose=args.verbose,
    )

    with open(args.out, "w", encoding="utf-8") as f:
        json.dump(mapping, f, ensure_ascii=False, indent=2)
    print(f"Saved {len(mapping)} users to {os.path.abspath(args.out)}")


if __name__ == "__main__":
    main()
