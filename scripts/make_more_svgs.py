#!/usr/bin/env python3
"""terminal.svg, rain.svg, orbit.svg, rings.svg, waves.svg -- SMIL-only animated SVGs for the README."""
import math, os, random
from xml.sax.saxutils import escape
OUT = os.path.join(os.path.dirname(__file__), "..", "assets")
BG, CY, MG, GR, MU, TX = "#0a0e14", "#22d3ee", "#ff4fd8", "#39d353", "#7d8590", "#e6edf3"
F = 'font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace"'
def head(W, H): return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" {F}><defs>'
    f'<filter id="g" x="-40%" y="-40%" width="180%" height="180%"><feGaussianBlur stdDeviation="3" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter></defs>'
    f'<rect width="{W}" height="{H}" rx="14" fill="{BG}"/><rect x=".5" y=".5" width="{W-1}" height="{H-1}" rx="14" fill="none" stroke="#1f2b3a"/>')

def terminal():
    W, H, fs = 860, 330, 17; cw = fs * .6
    L = [("whoami", "avisekh_mondal"), ("cat skills.txt", "C  C++  Python  Java  HTML  CSS  JS"),
         ("echo $GOAL", "open-source contributor"), ("uptime", "B.Tech 1st year, Kolkata, still learning")]
    s = [head(W, H), f'<line x1="0" y1="34" x2="{W}" y2="34" stroke="#1f2b3a"/><circle cx="20" cy="17" r="5" fill="#ff5f56"/><circle cx="38" cy="17" r="5" fill="#ffbd2e"/><circle cx="56" cy="17" r="5" fill="#27c93f"/>']
    t, y = .6, 82; P = "avi502@github:~$ "
    for k, (cmd, out) in enumerate(L):
        n = len(P) + len(cmd); w = n * cw; dur = n * .045
        s.append(f'<clipPath id="t{k}"><rect x="30" y="{y-20}" height="28" width="0"><animate attributeName="width" values="0;{w:.0f}" dur="{dur:.2f}s" begin="{t:.2f}s" fill="freeze"/></rect></clipPath>'
                 f'<text x="30" y="{y}" font-size="{fs}" fill="{TX}" clip-path="url(#t{k})"><tspan fill="{GR}">{P}</tspan>{escape(cmd)}</text>'
                 f'<text x="30" y="{y+26}" font-size="{fs}" fill="{CY}" opacity="0">{escape(out)}<animate attributeName="opacity" values="0;1" dur=".3s" begin="{t+dur+.15:.2f}s" fill="freeze"/></text>')
        t += dur + 1.0; y += 62
    s.append(f'<rect x="30" y="{y-20}" width="10" height="20" fill="{GR}" opacity="0"><animate attributeName="opacity" values="1;0;1" dur="1s" begin="{t:.2f}s" repeatCount="indefinite"/></rect></svg>')
    return "".join(s)

def rain():
    W, H = 860, 150; random.seed(502); ch = "01<>{}/;=+*$#"; s = [head(W, H), f'<clipPath id="rc"><rect width="{W}" height="{H}" rx="14"/></clipPath><g clip-path="url(#rc)" font-size="13">']
    for i in range(0, W, 14):
        dur = random.uniform(3.5, 8); n = 8
        tsp = "".join(f'<tspan x="{i+7}" dy="14" fill="{"#d1fae5" if j==n-1 else GR}" fill-opacity="{(j+1)/n*.85:.2f}">{random.choice(ch).replace("<","&lt;").replace(">","&gt;")}</tspan>' for j in range(n))
        s.append(f'<text y="-20" text-anchor="middle">{tsp}<animateTransform attributeName="transform" type="translate" values="0,0;0,{H+150}" dur="{dur:.1f}s" begin="-{random.uniform(0,dur):.1f}s" repeatCount="indefinite"/></text>')
    s.append(f'</g><rect x="150" y="52" width="560" height="46" rx="10" fill="{BG}" fill-opacity=".88" stroke="{CY}" stroke-opacity=".5"/>'
             f'<text x="{W/2}" y="82" text-anchor="middle" font-size="20" fill="{CY}" filter="url(#g)">while (alive) {{ learn(); build(); }}<animate attributeName="opacity" values="1;.7;1" dur="2.5s" repeatCount="indefinite"/></text></svg>')
    return "".join(s)

def orbit():
    W, H, cx, cy = 860, 440, 430, 220
    rings = [(80, 18, 1, CY, ["C", "C++"]), (135, 28, -1, MG, ["Python", "Java", "JS"]), (190, 42, 1, GR, ["HTML", "CSS", "Linux"])]
    s = [head(W, H)]
    for r, dur, dr, col, items in rings:
        s.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{col}" stroke-opacity=".35" stroke-dasharray="3 7"/>')
        for j, nm in enumerate(items):
            a = 360 * j / len(items) + r; px = cx + r
            s.append(f'<g><animateTransform attributeName="transform" type="rotate" values="{a} {cx} {cy};{a+360*dr} {cx} {cy}" dur="{dur}s" repeatCount="indefinite"/>'
                     f'<g><animateTransform attributeName="transform" type="rotate" values="{-a} {px} {cy};{-a-360*dr} {px} {cy}" dur="{dur}s" repeatCount="indefinite"/>'
                     f'<circle cx="{px}" cy="{cy}" r="25" fill="{BG}" stroke="{col}" stroke-width="2" filter="url(#g)"/><text x="{px}" y="{cy+4}" text-anchor="middle" font-size="12" fill="{TX}">{nm}</text></g></g>')
    s.append(f'<circle cx="{cx}" cy="{cy}" r="40" fill="{BG}" stroke="{CY}" stroke-width="2" filter="url(#g)"><animate attributeName="r" values="40;46;40" dur="3s" repeatCount="indefinite"/></circle>'
             f'<text x="{cx}" y="{cy+7}" text-anchor="middle" font-size="22" font-weight="700" fill="{TX}">AVI</text></svg>')
    return "".join(s)

def rings():
    W, H = 860, 270; s = [head(W, H)]
    for i, (nm, v, col) in enumerate([("C / C++", 65, CY), ("Web dev", 75, MG), ("Linux", 40, GR)]):
        cx, cy, r = 215 * (i + 1), 120, 62; C = 2 * math.pi * r; b = .3 + i * .3
        s.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="#182230" stroke-width="12"/>'
                 f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{col}" stroke-width="12" stroke-linecap="round" stroke-dasharray="{C:.1f}" stroke-dashoffset="{C:.1f}" transform="rotate(-90 {cx} {cy})" filter="url(#g)">'
                 f'<animate attributeName="stroke-dashoffset" values="{C:.1f};{C*(1-v/100):.1f}" dur="1.8s" begin="{b}s" calcMode="spline" keySplines=".2 .8 .2 1" fill="freeze"/></circle>'
                 f'<circle cx="{cx}" cy="{cy}" r="84" fill="none" stroke="{col}" stroke-opacity=".5" stroke-dasharray="2 10" stroke-linecap="round"><animateTransform attributeName="transform" type="rotate" values="0 {cx} {cy};{360*(1 if i%2==0 else -1)} {cx} {cy}" dur="{16+i*6}s" repeatCount="indefinite"/></circle>'
                 f'<text x="{cx}" y="{cy+9}" text-anchor="middle" font-size="26" font-weight="700" fill="{TX}" opacity="0">{v}%<animate attributeName="opacity" values="0;1" dur=".6s" begin="{b+1.2}s" fill="freeze"/></text>'
                 f'<text x="{cx}" y="{cy+118}" text-anchor="middle" font-size="15" fill="{MU}">{nm}</text>')
    return "".join(s) + "</svg>"

def waves():
    W, H, N = 860, 170, 43
    def path(ph, A, f, base): return "M" + " L".join(f"{i*W/(N-1):.0f},{base + A*math.sin(f*2*math.pi*i/(N-1)+ph):.1f}" for i in range(N)) + f" L{W},{H} L0,{H} Z"
    s = [head(W, H), f'<clipPath id="wc"><rect width="{W}" height="{H}" rx="14"/></clipPath><g clip-path="url(#wc)">']
    for A, f, base, col, op, dur in [(16, 2, 95, CY, .35, 7), (12, 3, 110, MG, .3, 5), (9, 4, 125, GR, .35, 4)]:
        vals = ";".join(path(k * math.pi / 2 * (1 if f % 2 == 0 else -1), A, f, base) for k in range(5))
        s.append(f'<path d="{path(0, A, f, base)}" fill="{col}" fill-opacity="{op}"><animate attributeName="d" values="{vals}" dur="{dur}s" repeatCount="indefinite"/></path>')
    s.append(f'</g><text x="{W/2}" y="62" text-anchor="middle" font-size="22" fill="{TX}" filter="url(#g)">thanks for stopping by</text></svg>')
    return "".join(s)

for name, fn in (("terminal", terminal), ("rain", rain), ("orbit", orbit), ("rings", rings), ("waves", waves)):
    open(os.path.join(OUT, name + ".svg"), "w").write(fn())
