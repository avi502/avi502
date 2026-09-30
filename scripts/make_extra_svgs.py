#!/usr/bin/env python3
"""header.svg, marquee.svg, projects.svg, ecg.svg -- SMIL-only animated SVGs."""
import math, os
from xml.sax.saxutils import escape
OUT = os.path.join(os.path.dirname(__file__), "..", "assets")
BG, CY, MG, GR, MU, TX = "#0a0e14", "#22d3ee", "#ff4fd8", "#39d353", "#7d8590", "#e6edf3"
F = 'font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace"'
def head(W, H, extra=""): return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" {F}><defs>{extra}'
    f'<filter id="g" x="-40%" y="-40%" width="180%" height="180%"><feGaussianBlur stdDeviation="3" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>'
    f'<clipPath id="rc"><rect width="{W}" height="{H}" rx="14"/></clipPath></defs><rect width="{W}" height="{H}" rx="14" fill="{BG}"/>')
FRAME = lambda W, H: f'<rect x=".5" y=".5" width="{W-1}" height="{H-1}" rx="14" fill="none" stroke="#1f2b3a"/>'

def header():
    W, H = 860, 210
    s = [head(W, H, '<filter id="bl" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="32"/></filter>'), '<g clip-path="url(#rc)"><g filter="url(#bl)">']
    for col, cx, cy, rx, ry, dx, dy, dur in [(CY, 200, 80, 190, 60, 260, 40, 9), (MG, 600, 140, 200, 60, -280, -50, 11), (GR, 420, 50, 150, 45, 120, 70, 8)]:
        s.append(f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="{col}" fill-opacity=".55"><animate attributeName="cx" values="{cx};{cx+dx};{cx}" dur="{dur}s" repeatCount="indefinite"/><animate attributeName="cy" values="{cy};{cy+dy};{cy}" dur="{dur*1.3:.1f}s" repeatCount="indefinite"/></ellipse>')
    s.append(f'</g><rect width="{W}" height="{H}" fill="{BG}" fill-opacity=".45"/></g>{FRAME(W,H)}')
    s.append(f'<text x="{W/2}" y="112" text-anchor="middle" font-size="58" font-weight="700" fill="{TX}" fill-opacity="0" stroke="{CY}" stroke-width="1.5" stroke-dasharray="700" stroke-dashoffset="700" filter="url(#g)">Avisekh Mondal'
             f'<animate attributeName="stroke-dashoffset" values="700;0" dur="2.6s" begin=".3s" fill="freeze"/><animate attributeName="fill-opacity" values="0;1" dur="1s" begin="2.4s" fill="freeze"/></text>')
    s.append(f'<text x="{W/2}" y="158" text-anchor="middle" font-size="18" fill="{TX}" letter-spacing="2" opacity="0">code . learn . repeat<animate attributeName="opacity" values="0;1" dur="1s" begin="3.2s" fill="freeze"/><animate attributeName="letter-spacing" values="14;2" dur="1.4s" begin="3.2s" fill="freeze"/></text></svg>')
    return "".join(s)

def marquee():
    W, H = 860, 84; tags = ["C", "C++", "Python", "Java", "HTML5", "CSS3", "JavaScript", "Linux", "Git", "Open Source"]
    cols = [CY, MG, GR]; x = 0; items = []
    for i, t in enumerate(tags):
        w = len(t) * 9 + 34; c = cols[i % 3]
        items.append(f'<rect x="{x}" y="24" width="{w}" height="36" rx="18" fill="{c}" fill-opacity=".12" stroke="{c}"/><text x="{x+w/2}" y="47" text-anchor="middle" font-size="15" fill="{TX}">{escape(t)}</text>'); x += w + 16
    row = "".join(items); T = x
    return (head(W, H, f'<linearGradient id="fd" x1="0" x2="1"><stop offset="0" stop-color="{BG}"/><stop offset=".12" stop-color="{BG}" stop-opacity="0"/><stop offset=".88" stop-color="{BG}" stop-opacity="0"/><stop offset="1" stop-color="{BG}"/></linearGradient>')
            + f'<g clip-path="url(#rc)"><g><animateTransform attributeName="transform" type="translate" values="0,0;-{T},0" dur="22s" repeatCount="indefinite"/>{row}<g transform="translate({T},0)">{row}</g><g transform="translate({2*T},0)">{row}</g></g>'
            f'<rect width="{W}" height="{H}" fill="url(#fd)"/></g>{FRAME(W,H)}</svg>')

def projects():
    W, H = 860, 230; s = [head(W, H)]
    cards = [("GUESSING_GAME", "C", CY, ["Number-guessing game with hints,", "limited attempts, scoring, Hard Mode"]),
             ("SIMPLE_CALCULATOR", "C++", MG, ["Arithmetic, power, root,", "trig, log, min / max"])]
    for i, (nm, lang, col, ds) in enumerate(cards):
        x, w, y, h = 30 + i * 420, 400, 30, 170; b = .3 + i * .5; sx = -60 if i == 0 else 60
        s.append(f'<g opacity="0"><animateTransform attributeName="transform" type="translate" values="{sx},0;0,0" dur=".9s" begin="{b}s" calcMode="spline" keySplines=".2 .8 .2 1" fill="freeze"/><animate attributeName="opacity" values="0;1" dur=".6s" begin="{b}s" fill="freeze"/>'
                 f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="#0d1420"/>'
                 f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="none" stroke="{col}" stroke-width="2" pathLength="1" stroke-dasharray=".25 .75" filter="url(#g)"><animate attributeName="stroke-dashoffset" values="0;-1" dur="4s" repeatCount="indefinite"/></rect>'
                 f'<text x="{x+24}" y="{y+44}" font-size="20" font-weight="700" fill="{TX}">{nm}</text>'
                 f'<text x="{x+24}" y="{y+80}" font-size="14" fill="{MU}">{ds[0]}</text><text x="{x+24}" y="{y+102}" font-size="14" fill="{MU}">{ds[1]}</text>'
                 f'<rect x="{x+24}" y="{y+122}" width="{len(lang)*10+26}" height="26" rx="13" fill="{col}" fill-opacity=".15" stroke="{col}"/><text x="{x+37}" y="{y+140}" font-size="13" fill="{col}">{lang}</text>'
                 f'<circle cx="{x+w-34}" cy="{y+38}" r="6" fill="{col}"><animate attributeName="r" values="6;10;6" dur="2s" repeatCount="indefinite"/><animate attributeName="opacity" values="1;.3;1" dur="2s" repeatCount="indefinite"/></circle></g>')
    return "".join(s) + f'{FRAME(W,H)}</svg>'

def ecg():
    W, H, y0 = 860, 110, 62; pts = [(0, y0)]
    for k in range(5):
        b = 20 + k * 172; pts += [(b + 40, y0), (b + 52, y0 - 8), (b + 64, y0), (b + 84, y0), (b + 92, y0 + 10), (b + 100, y0 - 46), (b + 110, y0 + 30), (b + 120, y0), (b + 150, y0), (b + 160, y0 - 10), (b + 172, y0)]
    d = "M" + " L".join(f"{min(x, W)},{y}" for x, y in pts)
    return (head(W, H) + f'<path d="{d}" pathLength="1" fill="none" stroke="{GR}" stroke-opacity=".25" stroke-width="2"/>'
            f'<path d="{d}" pathLength="1" fill="none" stroke="{GR}" stroke-width="3" stroke-linecap="round" stroke-dasharray=".14 1" filter="url(#g)"><animate attributeName="stroke-dashoffset" values=".14;-1" dur="3.2s" repeatCount="indefinite"/></path>'
            f'<text x="24" y="30" font-size="13" fill="{MU}">commit --pulse</text><text x="{W-24}" y="30" text-anchor="end" font-size="13" fill="{GR}">alive<animate attributeName="opacity" values="1;.3;1" dur="1.2s" repeatCount="indefinite"/></text>{FRAME(W,H)}</svg>')

for n, fn in (("header", header), ("marquee", marquee), ("projects", projects), ("ecg", ecg)):
    open(os.path.join(OUT, n + ".svg"), "w").write(fn())
