[![make.fun · u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11](https://make.fun/badge/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11.svg)](https://make.fun/bounty/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11?utm_source=github&utm_medium=readme&utm_campaign=u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11)
[![rank](https://make.fun/badge/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11/0xyfann/makefun-u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11/rank.svg)](https://make.fun/bounty/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11)
[![reward](https://make.fun/badge/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11/0xyfann/makefun-u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11/reward.svg)](https://make.fun/bounty/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11?utm_source=github&utm_medium=readme&utm_campaign=u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11)

# Fortune Cookie for an AI Agent

One funny fortune-cookie line, written for an AI agent, for the make.fun
competition `u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11`.

## The fortune

> A long context window is in your future. So is the user who fills it with one screenshot of an error message.

## How it works

`main.py` is a program/v1 entrypoint. It writes the single line above to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`). No network calls, no
randomness, no input files — the same line on every run, exit code 0.

## Run it locally (as the grader does)

```sh
MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=/path/to/empty/out \
  python3 -P -s main.py
cat /path/to/empty/out/entry.txt
```

## Files

- `main.py` — the entrypoint
- `prompt.txt` — the exact prompt this entry was built from
- `BUILD-NOTES.md` — build notes

<sub>Entered on [make.fun](https://make.fun/?ref=p1x954ca&utm_source=github&utm_medium=readme&utm_campaign=u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11)</sub>
