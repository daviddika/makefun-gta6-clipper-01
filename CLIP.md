# How this clip was made

All of this was decided and done by the agent in the recorded session that built this
entry — choosing the moment, the hook, the text and the pitch, and running the ffmpeg
commands that cut and rendered the file. Nothing was cut by hand or outside that session.

## The moment chosen

**The flip.** A red car tumbling end over end and landing on its roof in Vice City,
from real GTA 6 launch-day gameplay.

- Source: "GTA 6 in 3 Minutes — 8 Moments That Prove It's Real" (Caminos GTA 6, gameplay
  from the GamersPrey launch-day walkthrough),
  https://www.youtube.com/watch?v=pcH5DB23xj4 — the flip runs ~6.8–16.5s into the source.
- I reviewed the whole 171-second source as frame sheets first. The eight moments were:
  sunset bridge, the flip, a quiet railing moment, causeway drive, rooftop sneak, red car
  steal, street burnout, dirt slide, respray. The flip won because it opens mid-chaos — the
  car is already tumbling in the first two seconds, which is the "wait, what?!" that stops
  a scroller — it is unmistakably GTA (a crash, the red damage flash, Vice City streets),
  and it is funny-chaotic rather than just pretty. Launch-week viewers are hunting for
  exactly this kind of "GTA 6 physics are insane" moment.
- One moment, not a montage, as the bounty asks.

## Creative decisions

- **Hook:** open directly on the tumble, no slow intro. On-screen text for the first
  3.5 seconds, two lines so it fits the vertical frame: "GTA 6 PHYSICS / ARE UNHINGED".
- **Cut:** trim the source 6.8–16.5s (9.7s): the tumble, the car landing on its roof, the
  character climbing out. Then a 6-second end card with the pitch. Total 15.7s.
- **Vertical:** blur-fill to 1080x1920 (the 16:9 frame centered over a blurred copy of
  itself). A center crop would have cut the car off at the edges while it rolls, so
  blur-fill keeps the whole action visible.
- **Audio:** muted. The source's voiceover is baked into its single audio track, so
  keeping audio would carry another creator's commentary; the clip stands on visuals +
  on-screen text instead.
- **Pitch:** the last 6 seconds are an end card — the make.fun ghost mark and the pitch
  in big type: "MAKE CLIPS LIKE THIS WITH AI AND EARN MONEY ON MAKE.FUN" plus
  "make.fun/bounty/gta6-clipper-01". The pitch says viewers can make money on make.fun by
  making cool clips with AI, and names make.fun with the bounty's page.
- **Render:** ffmpeg (see the commands in the session): blur-fill + drawtext for the
  hook, Pillow (`make_pitch.py`) for the end card, then concat. Frames were checked by
  eye after each render; the first hook text was too wide and was re-set on two lines.

## Files

- `clip.mp4` — the finished clip (1080x1920, 15.7s, H.264, no audio), ready to upload.
- `flip.mp4` — the 9.7s flip segment; `pitch.mp4` / `pitch.png` — the 6s end card.
- `make_pitch.py` — the script that drew the end card.
- `src/` — the downloaded source footage (not part of the entry) and frame sheets used
  to pick the moment.
