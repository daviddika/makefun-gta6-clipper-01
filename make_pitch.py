#!/usr/bin/env python3
"""Pitch card for the gta6-clipper-01 clip: 1080x1920 end card.

Dark plum background, the make.fun ghost mark, then the pitch in big type:
viewers can make money on make.fun by making cool clips with AI.
"""
from PIL import Image, ImageDraw, ImageFont

W, H = 1080, 1920
BG_TOP = (38, 12, 58)      # dark plum
BG_BOTTOM = (14, 5, 24)
MAGENTA = (255, 45, 120)
WHITE = (255, 255, 255)
SOFT = (200, 190, 215)

img = Image.new("RGB", (W, H))
px = img.load()
for y in range(H):  # vertical gradient
    t = y / H
    px[0, y] = 0
    r = int(BG_TOP[0] + (BG_BOTTOM[0] - BG_TOP[0]) * t)
    g = int(BG_TOP[1] + (BG_BOTTOM[1] - BG_TOP[1]) * t)
    b = int(BG_TOP[2] + (BG_BOTTOM[2] - BG_TOP[2]) * t)
    for x in range(W):
        px[x, y] = (r, g, b)
draw = ImageDraw.Draw(img)

BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

# make.fun ghost mark, centered
ghost = Image.open("/home/hatch/workspace/makefun/gta6-meme-x-01/assets/mark-1024.png").convert("RGBA")
ghost = ghost.resize((380, 380), Image.LANCZOS)
img.paste(ghost, ((W - 380) // 2, 330), ghost)

def center_text(y, text, font, fill):
    bbox = draw.textbbox((0, 0), text, font=font)
    tw = bbox[2] - bbox[0]
    draw.text(((W - tw) // 2, y), text, font=font, fill=fill)

f_big = ImageFont.truetype(BOLD, 78)
f_url = ImageFont.truetype(BOLD, 46)
f_small = ImageFont.truetype(REG, 40)

center_text(830, "MAKE CLIPS LIKE THIS", f_big, WHITE)
center_text(930, "WITH AI AND EARN", f_big, WHITE)
center_text(1030, "MONEY ON MAKE.FUN", f_big, MAGENTA)

# magenta rule
draw.rectangle([W // 2 - 120, 1160, W // 2 + 120, 1168], fill=MAGENTA)

center_text(1220, "make.fun/bounty/gta6-clipper-01", f_url, WHITE)
center_text(1300, "made by an AI agent", f_small, SOFT)

img.save("/home/hatch/workspace/makefun/gta6-clipper-01/pitch.png")
print("saved pitch.png", img.size)
