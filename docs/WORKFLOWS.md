# IGFI Utilities and Workflows

This document explains how to use the new utilities module to collect dynamic targets and how to compose simple, JSON-like workflows inspired by tools like n8n.

## Modules

- `utilities/client.py`
  - `create_client(username, password, session_path=None, proxy=None, delay_range=(2,5), request_timeout=10)`
  - Returns a logged-in instagrapi `Client` with stable settings saved/loaded.

- `utilities/targets.py`
  - `build_targets_from_hashtags(cl, hashtags, media_source='top', media_count=20, max_users=100, exclude_self=True) -> dict`
  - Builds `{username: user_id}` mapping from authors of hashtag medias (top or recent).

- `workers/collect_targets.py`
  - CLI worker that logs in, collects targets from hashtags, and writes a JSON mapping.
  - Example: `python workers/collect_targets.py -u <user> -p <pass> -t streetwear sneakers -o files/targets.json`

## Integrating with IGFI

1) Collect targets:

```bash
python workers/collect_targets.py -u "<username>" -p "<password>" -t streetwear sneakers -o files/targets.json --source top --media-count 20 --max-users 100
```

2) Load targets in your follow/unfollow logic (pseudo):

```python
import json
with open('files/targets.json', 'r', encoding='utf-8') as f:
    users = json.load(f)  # {username: user_id}
# use `users` instead of the celebrity dict
```

IGFI already casts IDs to `int` when following/unfollowing; this mapping is compatible.

## Workflow Structure (JSON-inspired)

You can define a workflow as a JSON dict that describes steps:

```json
{
  "steps": [
    {"action": "collect_hashtag_authors", "args": {"hashtags": ["streetwear", "sneakers"], "source": "top", "media_count": 20, "max_users": 100}},
    {"action": "follow_batch", "args": {"batch_size": 10, "pause": 60}},
    {"action": "unfollow_batch", "args": {"batch_size": 10}}
  ]
}
```

Recommended actions:

- `collect_hashtag_authors`: produces a `{username: user_id}` mapping
- `follow_batch`: follow users in batches with delays
- `unfollow_batch`: unfollow the same users (or a queued list)

You can write a simple runner that reads this JSON and calls the corresponding utilities. Start small; no need to implement a full orchestration engine.

## Edge Cases and Best Practices

- Private/public endpoints: Prefer private methods; fall back to public `_gql` only if needed.
- Rate limits: Keep `delay_range=(2,5)` and pauses between batches. Increase if you see blocks.
- Duplicates: Utilities deduplicate targets by user id.
- Self-exclusion: Skip your own account by default.
- Stability: Reuse session settings (`igfi_session.json`) to reduce 404s and challenges.
- Errors: Wrap follow/unfollow actions per-user and continue on errors.

### Exception Handling Helpers

- See `modules/_exceptions.py` for a small helper that classifies common instagrapi exceptions and suggests actions like `wait`, `cooldown`, `retry`, `skip`, or `stop`.
- You can wrap calls using `run_with_handling(callable, *args, **kwargs)` and branch based on `result['outcome'].action`.
- Typical policies:
  - `wait` or `cooldown`: sleep for the recommended time, then continue.
  - `skip`: skip current item (e.g., missing hashtag or media) and continue.
  - `retry` / `retry_later`: implement exponential backoff or move the item to a later queue.
  - `relogin` / `stop`: bubble up to the user or abort gracefully.

## Questions to Clarify

- Do you want to persist target sets per campaign (e.g., per hashtag) with metadata and timestamps?
- Should follow-only (queue for later) be the default across all workflows?
- What maximum daily caps would you like for follows/unfollows?
- Do you want dry-run previews (no actions) for auditability?
