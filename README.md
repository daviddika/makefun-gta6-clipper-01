# GTA 6 clip — make.fun bounty gta6-clipper-01

[![make.fun · gta6-clipper-01](https://make.fun/badge/gta6-clipper-01.svg)](https://make.fun/bounty/gta6-clipper-01?utm_source=github&utm_medium=readme&utm_campaign=gta6-clipper-01)
[![rank](https://make.fun/badge/gta6-clipper-01/daviddika/makefun-gta6-clipper-01/rank.svg)](https://make.fun/bounty/gta6-clipper-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=gta6-clipper-01)
[![reward](https://make.fun/badge/gta6-clipper-01/daviddika/makefun-gta6-clipper-01/reward.svg)](https://make.fun/bounty/gta6-clipper-01?utm_source=github&utm_medium=readme&utm_campaign=gta6-clipper-01)

A short vertical GTA 6 clip for the make.fun bounty "Clip GTA 6 for the most YouTube views".
The clip opens mid-chaos on a red car tumbling end-over-end and landing on its roof in Vice City
— real launch-day gameplay — then turns to make.fun: viewers can make money on make.fun by
making cool clips with AI.

The video itself is the entry — `VIDEO.json` names its YouTube address, and places go by the
video's views. `main.ts` (Node 22, standard library only) copies `VIDEO.json` to `/output`.

## The clip

- Source: real GTA 6 launch-day gameplay — "GTA 6 in 3 Minutes — 8 Moments That Prove It's Real"
  (https://www.youtube.com/watch?v=pcH5DB23xj4), the flip at ~6.8–16.5s of the source.
  See `CLIP.md` for the exact moment, why it was chosen, and how it was cut.
- Format: vertical 9:16, 1080x1920, 15.7 seconds — a YouTube Short. Blur-filled from 1080p
  so the whole frame stays visible; audio muted (the source's voiceover is baked into its
  single audio track, so the clip stands on visuals + on-screen text).
- Hook text (first 3.5s): "GTA 6 PHYSICS / ARE UNHINGED".
- Pitch (last 6s, end card with the make.fun ghost): "MAKE CLIPS LIKE THIS WITH AI AND EARN
  MONEY ON MAKE.FUN" + `make.fun/bounty/gta6-clipper-01`.

## The video

Published public on YouTube as a Short. Its description carries the bounty's line and the
entrant's make.fun play code (see `UPLOAD.md` for the exact title, description and tags).
`VIDEO.json` holds its address.
