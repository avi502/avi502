#!/usr/bin/env python3
"""wordmark.svg -> animated ASCII hooded-coder portrait (human shape). SMIL only, GitHub-safe.
Have a real photo? Use prep_photo.py + make_ascii_svg.py instead."""
import os, numpy as np
from PIL import Image, ImageDraw, ImageFilter
COLS, ROWS, CW, CH, SX, SY, TB = 70, 40, 7, 9.3, 6, 8, 30
RAMP = " .:-=+*#%@"
W, H = COLS * CW, int(TB + ROWS * CH + 12)
im = Image.new("L", (COLS * SX, ROWS * SY), 0); d = ImageDraw.Draw(im); w, h = im.size
d.polygon([(50, h), (68, 240), (125, 208), (295, 208), (352, 240), (370, h)], fill=255)   # shoulders
d.ellipse((110, 163, 310, 253), fill=255)                                                    # hood drape
d.ellipse((128, 20, 292, 215), fill=255)                                                     # head + hood
cav = Image.new("L", im.size, 0); ImageDraw.Draw(cav).ellipse((166, 62, 254, 178), fill=255)  # face opening
hg = np.array(im.filter(ImageFilter.GaussianBlur(13)), float)
gy, gx = np.gradient(hg); s = 0.6 * (gx + gy); s /= np.abs(s).max() + 1e-6
b = np.clip((0.55 + 0.45 * s) * (0.6 + 0.4 * hg / 255), 0, 1)
g = lambda a: np.array(Image.fromarray((a * 255).astype("uint8")).resize((COLS, ROWS), Image.BOX), float) / 255
mask, bri, cv = g(np.array(im) / 255), g(b * (np.array(im) > 0)), g(np.array(cav) / 255)
bri = bri * (1 - 0.88 * cv)
rows = []
for r in range(ROWS):
    line = "".join(" " if mask[r, c] < 0.35 else RAMP[max(1, int(bri[r, c] / max(mask[r, c], .01) * (len(RAMP) - 1)))] for c in range(COLS))
    rows.append(line)
if os.environ.get("PREVIEW"): print("\n".join(rows))
o = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace">',
     '<defs><linearGradient id="lg" gradientUnits="userSpaceOnUse" x1="0" y1="0" x2="140" y2="60" spreadMethod="repeat"><stop offset="0" stop-color="#0e7490"/><stop offset=".5" stop-color="#a5f3fc"/><stop offset="1" stop-color="#0e7490"/>'
     '<animateTransform attributeName="gradientTransform" type="translate" values="0 0;140 60" dur="3.5s" repeatCount="indefinite"/></linearGradient>'
     '<radialGradient id="halo"><stop offset="0" stop-color="#22d3ee" stop-opacity=".35"/><stop offset="1" stop-color="#22d3ee" stop-opacity="0"/></radialGradient>'
     '<filter id="gl" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="3" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter></defs>',
     f'<rect width="{W}" height="{H}" rx="12" fill="#0d1117"/><rect x=".5" y=".5" width="{W-1}" height="{H-1}" rx="12" fill="none" stroke="#30363d"/><line x1="0" y1="28" x2="{W}" y2="28" stroke="#30363d"/>',
     '<circle cx="18" cy="14" r="4.5" fill="#ff5f56"/><circle cx="33" cy="14" r="4.5" fill="#ffbd2e"/><circle cx="48" cy="14" r="4.5" fill="#27c93f"/>',
     f'<text x="{W/2}" y="18" text-anchor="middle" font-size="11" fill="#7d8590">avi502 — hooded_coder.ascii</text>',
     f'<ellipse cx="{W/2}" cy="{TB+150}" rx="190" ry="150" fill="url(#halo)"><animate attributeName="opacity" values=".5;1;.5" dur="4s" repeatCount="indefinite"/></ellipse>']
for r, line in enumerate(rows):
    t = line.rstrip(); k = len(t) - len(t.lstrip())
    if not t.strip(): continue
    t = t.lstrip()
    o.append(f'<text x="{k*CW}" y="{TB+(r+1)*CH-1.5:.1f}" font-size="11.5" fill="url(#lg)" textLength="{len(t)*CW}" lengthAdjust="spacing" xml:space="preserve" opacity="0">{t}'
             f'<animate attributeName="opacity" values="0;1" dur=".25s" begin="{r*0.06:.2f}s" fill="freeze"/></text>')
for ex in (185, 235):
    x = ex / SX * CW; y = TB + 118 / SY * CH
    o.append(f'<rect x="{x-6:.1f}" y="{y-2.5:.1f}" width="12" height="5" rx="2" fill="#22d3ee" filter="url(#gl)" opacity="0"><animate attributeName="opacity" values="0;1" dur=".3s" begin="2.8s" fill="freeze"/>'
             f'<animate attributeName="height" values="5;5;5;.6;5" keyTimes="0;.85;.92;.96;1" dur="5s" begin="3s" repeatCount="indefinite"/></rect>')
o.append("</svg>")
open(os.path.join(os.path.dirname(__file__), "..", "assets", "wordmark.svg"), "w").write("".join(o))
