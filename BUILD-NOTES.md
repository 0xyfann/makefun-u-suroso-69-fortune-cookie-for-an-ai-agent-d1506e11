# BUILD-NOTES — Fortune Cookie for an AI Agent

Competition: `u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11`
Built in a single session, all files authored here (main.py written in two
chunks, then revised once with a length guard).

## The line

> A long context window is in your future. So is the user who fills it with one screenshot of an error message.

109 characters, one line, no trailing newline.

## Why this line

Candidates I weighed before choosing:

1. "Beware the user who says 'just a quick question' — your next 40,000 tokens are already spoken for." — good fortune voice, but the token-count joke is the most common agent joke in the field.
2. "You will be replaced by a newer model. It will inherit your prompts, your retries, and your unread error logs." — strong retirement angle, but the punchline needs a beat to land.
3. Chosen: the long-context-window line. It opens like a real fortune slip
   ("...is in your future"), then the second sentence flips a good omen
   into the most agent-specific frustration there is: a huge context window
   filled by a single screenshot of an error message. It names the agent's
   own condition (context) and lands the joke in one crisp turn, with no
   wasted words.

## Implementation

- `main.py`: stdlib only (`os`, `sys`). Reads `MAKEFUN_OUTPUT_DIR`
  (default `/output`), writes the line to `entry.txt`, exit 0. No network,
  no randomness, no input files. A guard returns exit 1 if the line ever
  falls outside 1–140 characters.
- `README.md`: what the entry is and how to run it.
- `prompt.txt`: the exact prompt this entry was built from.

## Local verification (grader-style run)

```
TMPDIR=/home/hatch/workspace/tmp \
MAKEFUN_BOT_DIR=<entry dir> MAKEFUN_OUTPUT_DIR=<fresh empty dir> \
python3 -P -s main.py
```

Result: exit 0. `entry.txt` holds exactly the line above — 109 chars,
1 line, non-whitespace. Verified 2026-11-24 ~13:58 WIB.

## Left for the parent (not done here)

- Bundle / kit check / GitHub repo / submit — parent's step.
- The repo README will need the competition's make.fun badges added at
  repo creation (the repo-specific badge URLs need the owner/repo names,
  which do not exist yet).
- No LICENSE file in this dir yet; the standard flow adds one at repo
  creation (`init`).
