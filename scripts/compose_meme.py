#!/usr/bin/env python3
"""Compose the GTA 6 meme: AI scene + crisp Impact-style caption + make.fun wordmark.

The scene (a skeleton gamer, cobwebs, a Vice City sunset on the TV, the
make.fun ghost) is generated first; this script only adds the caption text on
top with PIL, so the letters stay sharp at any size instead of the wobbly
text an image model would paint. The top line states the joke's setup, the
two bottom lines its punchline, and the make.fun wordmark sits in the
bottom-right corner, clear of the caption.
"""
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).resolve().parent
# the generated scene lives beside the repo (build input, not committed);
# the finished meme lands in the repo root.
SRC = HERE.parent.parent / "meme-scene.png"
OUT = HERE.parent / "meme.png"
SIZE = 1200
FONT_PATH = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

TOP = "GTA V CAME OUT WHEN I WAS 15"
BOTTOM = ["GTA 6 COMES OUT WHEN", "I HAVE A MORTGAGE"]
BRAND = "make.fun"

im = Image.open(SRC).convert("RGB").resize((SIZE, SIZE), Image.LANCZOS)
draw = ImageDraw.Draw(im)


def fit_font(text, max_w, start):
    size = start
    while size > 20:
        f = ImageFont.truetype(FONT_PATH, size)
        if draw.textlength(text, font=f) <= max_w:
            return f, size
        size -= 2
    return ImageFont.truetype(FONT_PATH, size), size


def meme_text(cx, y, text, font):
    # black outline + white fill, classic meme style
    sw = max(4, font.size // 12)
    draw.text((cx, y), text, font=font, fill="white", anchor="ma",
              stroke_width=sw, stroke_fill="black")


# top line
f_top, _ = fit_font(TOP, SIZE - 60, 88)
meme_text(SIZE // 2, 26, TOP, f_top)

# bottom lines (two lines, stacked upward from the bottom edge)
f_bot1, _ = fit_font(BOTTOM[0], SIZE - 560, 64)
f_bot2, _ = fit_font(BOTTOM[1], SIZE - 560, 64)
line_h = f_bot1.size + 6
y2 = SIZE - 30 - f_bot2.size
y1 = y2 - line_h
meme_text(SIZE // 2, y1, BOTTOM[0], f_bot1)
meme_text(SIZE // 2, y2, BOTTOM[1], f_bot2)

# make.fun wordmark, bottom-right corner, white on the dark floor
f_brand = ImageFont.truetype(FONT_PATH, 46)
draw.text((SIZE - 26, SIZE - 26), BRAND, font=f_brand, fill="white",
          anchor="rb", stroke_width=5, stroke_fill="black")

im.save(OUT, "PNG", optimize=True)
print("saved", OUT, im.size)
