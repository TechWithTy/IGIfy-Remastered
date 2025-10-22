# IGFI Usage Guide

This guide explains the main ways to run IGFI, including a “gain followers” mode (follow-only with deferred unfollow), a cleanup mode to unfollow queued users, the classic follow+unfollow loop, and niche targeting by hashtag likers.

> Run everything on a single line. On Windows, do not split commands across lines or the shell may try to execute `--session` as a separate command.

## Prerequisites

- Python 3.8+
- Dependencies installed (from the repo root):
  - `pip install -r files/requirements.txt`
- Your Instagram username/email and password

## Quick Start

- Basic run (interactive prompts):
  - Windows CMD:
    - `python igfi.py -u "<username_or_email>" -p "<password>"`
  - PowerShell:
    - `python .\igfi.py -u '<username_or_email>' -p '<password>'`
  - Git Bash:
    - `python igfi.py -u "<username_or_email>" -p "<password>"`

- What you’ll be asked (key prompts):
  - Keep log? yes/no
  - Display usernames later? yes/no
  - Grant extra follower info? yes/no
  - Cleanup previously queued unfollows now? yes/no
  - Use niche targeting by hashtag? yes/no
  - Batch size (default 10)
  - Pause between batches in seconds (default 60)
  - Follow-only now and queue unfollow for later? yes/no
  - Proceed? yes/no

## Use Cases

### 1) Gain Followers (Follow-Only; Queue Unfollow For Later)

- Choose: [1] Increase followers
- At prompts:
  - Cleanup previously queued unfollows now? → no
  - Use niche targeting by hashtag? → your choice (see 4)
  - Batch size / Pause → e.g., 10 and 60
  - Follow-only now and queue unfollow for later? → yes
  - Proceed? → yes
- Result: IGFI follows targets in batches and saves them to a queue for later unfollow. No immediate unfollow occurs.
- Queue file: `files/follow_queue.json`

### 2) Cleanup Queued Unfollows (Unfollow Later)

- Choose: [1] Increase followers
- At prompts:
  - Cleanup previously queued unfollows now? → yes
- Result: IGFI logs in, unfollows every user in `files/follow_queue.json`, then clears the file and exits.

### 3) Classic Follow + Unfollow (Per Batch)

- Choose: [1] Increase followers
- At prompts:
  - Cleanup previously queued unfollows now? → no
  - Use niche targeting by hashtag? → your choice (see 4)
  - Batch size / Pause → set to your preference
  - Follow-only now and queue unfollow for later? → no
  - Proceed? → yes
- Result: For each batch: follow N users, pause, then unfollow the same N users.

### 4) Niche Targeting (Hashtag Likers)

- When asked: Use niche targeting by hashtag? → yes
- You’ll be prompted for:
  - Hashtag (without `#`), e.g., `streetwear`
  - Number of recent posts to scan (default 5)
  - Max users to target (default 50)
- IGFI collects likers from recent posts with that hashtag and targets them instead of the built-in celebrity list.

## Logging and Follower Info

- Keep log? → Saves a summary to `files/log.txt` at the end.
- Grant extra follower info? → Allows IGFI to check follower_count and (optionally) list usernames if endpoints permit.
- Display usernames later? → If enabled and allowed, IGFI prints the usernames of newly detected followers.

## Tips for Best Results

- Stable session/device: IGFI saves settings to `igfi_session.json` to reduce API friction. Reuse it for consistent behavior.
- Pacing: Start with small batches (e.g., 5–10) and longer pauses (60–120s). Increase cautiously.
- Niche targeting: Yields better follow-back rates than following large celebrity accounts.
- Avoid rapid, repeated logins; reuse the saved settings.

## Troubleshooting

- `'--session' is not recognized` on Windows:
  - Keep your command on one line and don’t pass `--session`. IGFI manages its own settings.

- 404 on follow endpoint (e.g., `friendships/create/...`):
  - Usually indicates unstable device/session or throttling. Reuse `igfi_session.json`, reduce batches, increase pauses, and try later.

- KeyError: 'data' or long waits on GraphQL endpoints:
  - IGFI now avoids public GraphQL where possible and skips follower listing if blocked. Proceed with follow logic.

- No followers appear to be added:
  - This method relies on follow-backs. Try niche targeting, smaller batches, longer pauses, and let time pass between runs.

## FAQ

- Does IGFI “create” followers? No. It follows accounts (ideally niche-targeted) to encourage follow-backs, optionally unfollowing later.
- Can I just get a list of targets without following? Run through prompts and answer “no” at the final Proceed? prompt after niche collection to preview inputs, or I can add a dedicated dry-run flag.
- Where are settings stored? `igfi_session.json` in the repo directory.
- Where is the follow queue stored? `files/follow_queue.json`.

## Safety

- Use responsibly and at your own risk. Avoid aggressive settings to prevent rate limits or account restrictions.
- Follow your platform’s terms of service.

