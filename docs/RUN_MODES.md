# IGFI Run Modes

This doc explains how to run IGFI in different modes and how often to run it safely.

## Dry-Run (Preview Only)

- Command:
  - `python igfi.py -u "<username>" -p "<password>"`
- Menu → `[1] Increase followers`
- When asked: `Dry-run (preview targets; no actions)?` → `yes`
- Result: IGFI loads `files/targets.json` if present (or asks for targeting), prints up to 20 targets, and exits. No actions taken.

## Gain Followers (Follow-Only, Queue Unfollow)

- Command:
  - `python igfi.py -u "<username>" -p "<password>" --daily-cap 50`
- Menu → `[1] Increase followers`
- Prompts:
  - `Cleanup previously queued unfollows now?` → `no`
  - `Use niche targeting by hashtag?` → `yes` (or load `files/targets.json` ahead of time)
  - Enter hashtags and parameters
  - `Follow-only now and queue unfollow for later?` → `yes`
  - Confirm `Proceed?` → `yes`
- Result: IGFI follows users in batches and appends them to `files/follow_queue.json` for later unfollow. Stops automatically after `--daily-cap` follows.

## Classic Follow + Unfollow (Per Batch)

- Command:
  - `python igfi.py -u "<username>" -p "<password>" --daily-cap 50`
- Menu → `[1] Increase followers`
- Prompts:
  - `Follow-only now and queue unfollow for later?` → `no`
  - Confirm `Proceed?` → `yes`
- Result: For each batch: follow N users, pause, then unfollow the same N users. Stops after reaching `--daily-cap` follows.

## Collect Targets (Hashtags)

- Option 1 (menu):
  - Menu → `[6] Collect targets (hashtags)`
  - Enter hashtags and parameters
  - Save to `files/targets.json`
- Option 2 (worker):
  - `python workers/collect_targets.py -u "<u>" -p "<p>" -t streetwear sneakers -o files/targets.json --source top --media-count 20 --max-users 100`

## How Often To Run

- Recommended cadence: every 2 days (as per README) to reduce risk of action blocks.
- Keep `--daily-cap` conservative (e.g., 25–50) and use longer pauses between batches for safety.

## Tips

- Stable session: reuse the auto-saved `igfi_session.json` for fewer 404/challenges.
- Prefer niche targeting (hashtags relevant to your audience) for higher follow-back rates.
- Start with dry-run to review targets before acting.

