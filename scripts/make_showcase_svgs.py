#!/usr/bin/env python3
"""Make hero.svg (animated name + typing roles) and skills-graph.svg (radar + growth curve).
Pure SMIL, no JS, so it animates inside a GitHub README <img>. Edit SKILLS / CURVE below."""
import math, os
from xml.sax.saxutils import escape
OUT = os.path.join(os.path.dirname(__file__), "..", "assets")
BG, CY, MG, GR, MU = "#0a0e14", "#22d3ee", "#ff4fd8", "#39d353", "#7d8590"
FONT = 'font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace"'
SKILLS = {"C": 70, "C++": 60, "Python": 65, "Java": 45, "Web": 75, "Linux": 40}   # 0-100, edit me
CURVE = [4, 9, 14, 22, 27, 38, 45, 58, 66, 79, 88, 100]                           # growth, edit me
ROLES = ["B.Tech 1st-year student", "Kolkata, India", "C / C++ / Python / Java", "Learning Linux & open source"]

def hero():
    W, H, name, fs = 860, 230, "AVISEKH MONDAL", 54
    cw = fs * 0.6; x0 = (W - cw * len(name)) / 2; y = 110
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" {FONT}>',
         f'<defs><linearGradient id="scan" x1="0" x2="1"><stop offset="0" stop-color="{CY}" stop-opacity="0"/><stop offset=".5" stop-color="#fff" stop-opacity=".9"/><stop offset="1" stop-color="{MG}" stop-opacity="0"/></linearGradient>'
         f'<filter id="glow" x="-20%" y="-50%" width="140%" height="200%"><feGaussianBlur stdDeviation="4" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>'
         f'<pattern id="dots" width="18" height="18" patternUnits="userSpaceOnUse"><circle cx="1" cy="1" r=".9" fill="#1c2633"/></pattern>'
         f'<clipPath id="nameclip"><rect x="0" y="40" width="{W}" height="90"/></clipPath></defs>',
         f'<rect width="{W}" height="{H}" rx="14" fill="{BG}"/><rect width="{W}" height="{H}" rx="14" fill="url(#dots)"/>',
         f'<rect x=".5" y=".5" width="{W-1}" height="{H-1}" rx="14" fill="none" stroke="#1f2b3a"/>']
    cols = [CY, MG, GR, CY]
    for i, ch in enumerate(name):
        if ch == " ": continue
        x = x0 + i * cw; b = 0.15 + i * 0.07
        cyc = ";".join(cols[(i + k) % 4] for k in range(5))
        s.append(f'<g clip-path="url(#nameclip)"><g opacity="0"><animateTransform attributeName="transform" type="translate" values="0,-70;0,8;0,0" keyTimes="0;.7;1" dur=".7s" begin="{b:.2f}s" fill="freeze"/>'
                 f'<animate attributeName="opacity" values="0;1" dur=".3s" begin="{b:.2f}s" fill="freeze"/>'
                 f'<g><animateTransform attributeName="transform" type="translate" values="0,0;0,-7;0,0" dur="3.2s" begin="{b+1.2+i*.12:.2f}s" repeatCount="indefinite" calcMode="spline" keySplines=".4 0 .6 1;.4 0 .6 1"/>'
                 f'<text x="{x:.1f}" y="{y}" font-size="{fs}" font-weight="700" fill="{CY}" filter="url(#glow)">{ch}'
                 f'<animate attributeName="fill" values="{cyc}" dur="8s" begin="{b+1.5:.2f}s" repeatCount="indefinite"/></text></g></g></g>')
    s.append(f'<rect x="-60" y="38" width="60" height="4" fill="url(#scan)" opacity=".9"><animate attributeName="x" values="-60;{W}" dur="3.4s" begin="1.8s;scan_end.end+2s" repeatCount="1" id="scan_end"/></rect>')
    s.append(f'<line x1="{x0:.0f}" x2="{W-x0:.0f}" y1="128" y2="128" stroke="{MU}" stroke-opacity=".5" stroke-dasharray="3 6"><animate attributeName="stroke-dashoffset" values="0;-18" dur="1.2s" repeatCount="indefinite"/></line>')
    n, slot, fs2 = len(ROLES), 4.0, 20; T = n * slot; cw2 = fs2 * 0.6
    for k, r in enumerate(ROLES):
        w = cw2 * len(r); xs = (W - w) / 2; a, t, e = k / n, k / n + 0.35 / n, (k + 1) / n - 0.04 / n; z = (k + 1) / n
        kt = f"0;{a:.4f};{t:.4f};{e:.4f};{z:.4f};1" if z < 1 else f"0;{a:.4f};{t:.4f};{e:.4f};1"
        vw = f"0;0;{w:.0f};{w:.0f};0;0" if z < 1 else f"0;0;{w:.0f};{w:.0f};0"
        vx = ";".join(f"{xs + float(v):.0f}" for v in vw.split(";"))
        s.append(f'<clipPath id="c{k}"><rect x="{xs:.0f}" y="150" height="34" width="0"><animate attributeName="width" values="{vw}" keyTimes="{kt}" dur="{T}s" repeatCount="indefinite"/></rect></clipPath>'
                 f'<text x="{xs:.0f}" y="174" font-size="{fs2}" fill="#e6edf3" clip-path="url(#c{k})">{escape(r)}</text>'
                 f'<rect y="153" width="2" height="26" fill="{GR}" opacity="0"><animate attributeName="x" values="{vx}" keyTimes="{kt}" dur="{T}s" repeatCount="indefinite"/>'
                 f'<animate attributeName="opacity" values="0;0;1;1;0;0" keyTimes="{kt if z<1 else "0;%.4f;%.4f;%.4f;%.4f;1"%(a,t,e,e)}" dur="{T}s" repeatCount="indefinite"/></rect>')
    s.append(f'<text x="{W/2}" y="212" text-anchor="middle" font-size="12" fill="{MU}">avi502@github ~ $ <tspan fill="{GR}">online</tspan><animate attributeName="opacity" values="1;.35;1" dur="2s" repeatCount="indefinite"/></text></svg>')
    return "".join(s)

def graph():
    W, H = 860, 380; cx, cy, R = 230, 205, 120; n = len(SKILLS); names = list(SKILLS)
    pt = lambda i, v: (cx + R * v / 100 * math.sin(2 * math.pi * i / n), cy - R * v / 100 * math.cos(2 * math.pi * i / n))
    fmt = lambda pts: " ".join(f"{x:.1f},{y:.1f}" for x, y in pts)
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" {FONT}>',
         f'<defs><filter id="g" x="-30%" y="-30%" width="160%" height="160%"><feGaussianBlur stdDeviation="3" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>'
         f'<linearGradient id="ar" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{MG}" stop-opacity=".45"/><stop offset="1" stop-color="{MG}" stop-opacity="0"/></linearGradient>'
         f'<linearGradient id="ln" x1="0" x2="1"><stop offset="0" stop-color="{CY}"/><stop offset="1" stop-color="{MG}"/></linearGradient></defs>',
         f'<rect width="{W}" height="{H}" rx="14" fill="{BG}"/><rect x=".5" y=".5" width="{W-1}" height="{H-1}" rx="14" fill="none" stroke="#1f2b3a"/>',
         f'<text x="30" y="36" font-size="15" fill="#e6edf3">skill radar</text><text x="470" y="36" font-size="15" fill="#e6edf3">learning curve</text>']
    for ring in (25, 50, 75, 100):
        s.append(f'<polygon points="{fmt([pt(i, ring) for i in range(n)])}" fill="none" stroke="#243244" stroke-dasharray="4 5"><animate attributeName="stroke-dashoffset" values="0;-18" dur="3s" repeatCount="indefinite"/></polygon>')
    for i, nm in enumerate(names):
        x, y = pt(i, 100); lx, ly = pt(i, 122)
        s.append(f'<line x1="{cx}" y1="{cy}" x2="{x:.1f}" y2="{y:.1f}" stroke="#243244"/><text x="{lx:.1f}" y="{ly+4:.1f}" text-anchor="middle" font-size="13" fill="{MU}">{nm}</text>')
    fin = [pt(i, SKILLS[nm]) for i, nm in enumerate(names)]; ctr = [(cx, cy)] * n
    breathe = [pt(i, SKILLS[nm] * 0.93) for i, nm in enumerate(names)]
    s.append(f'<polygon points="{fmt(ctr)}" fill="{CY}" fill-opacity=".22" stroke="{CY}" stroke-width="2" filter="url(#g)">'
             f'<animate attributeName="points" values="{fmt(ctr)};{fmt(fin)}" dur="1.6s" begin=".3s" calcMode="spline" keySplines=".2 .8 .2 1" fill="freeze" id="rad"/>'
             f'<animate attributeName="points" values="{fmt(fin)};{fmt(breathe)};{fmt(fin)}" dur="4s" begin="rad.end" repeatCount="indefinite"/></polygon>')
    for (x, y), nm in zip(fin, names):
        s.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="0" fill="{MG}"><animate attributeName="r" values="0;5" dur=".4s" begin="1.9s" fill="freeze"/></circle>'
                 f'<text x="{x:.1f}" y="{y-10:.1f}" text-anchor="middle" font-size="11" fill="#e6edf3" opacity="0"><animate attributeName="opacity" values="0;1" dur=".4s" begin="2s" fill="freeze"/>{SKILLS[nm]}</text>')
    gx, gy, gw, gh = 490, 70, 340, 250
    for k in range(5):
        yy = gy + gh * k / 4; s.append(f'<line x1="{gx}" x2="{gx+gw}" y1="{yy}" y2="{yy}" stroke="#182230"/>')
    P = [(gx + gw * i / (len(CURVE) - 1), gy + gh - gh * v / 100) for i, v in enumerate(CURVE)]
    d = f"M{P[0][0]:.1f},{P[0][1]:.1f}" + "".join(f" C{(a[0]+b[0])/2:.1f},{a[1]:.1f} {(a[0]+b[0])/2:.1f},{b[1]:.1f} {b[0]:.1f},{b[1]:.1f}" for a, b in zip(P, P[1:]))
    s.append(f'<path d="{d} L{gx+gw},{gy+gh} L{gx},{gy+gh} Z" fill="url(#ar)" opacity="0"><animate attributeName="opacity" values="0;1" dur="1s" begin="1.6s" fill="freeze"/></path>'
             f'<path d="{d}" pathLength="1" fill="none" stroke="url(#ln)" stroke-width="3" stroke-linecap="round" stroke-dasharray="1" stroke-dashoffset="1" filter="url(#g)"><animate attributeName="stroke-dashoffset" values="1;0" dur="2.2s" begin=".4s" calcMode="spline" keySplines=".5 0 .2 1" fill="freeze"/></path>'
             f'<circle r="6" fill="#fff" filter="url(#g)" opacity="0"><animateMotion path="{d}" dur="5s" begin="2.8s" repeatCount="indefinite"/><animate attributeName="opacity" values="0;1;1;0" keyTimes="0;.05;.9;1" dur="5s" begin="2.8s" repeatCount="indefinite"/></circle>')
    lx, ly = P[-1]
    s.append(f'<circle cx="{lx}" cy="{ly}" r="5" fill="{MG}"/><circle cx="{lx}" cy="{ly}" r="5" fill="none" stroke="{MG}"><animate attributeName="r" values="5;18" dur="1.8s" repeatCount="indefinite"/><animate attributeName="opacity" values=".9;0" dur="1.8s" repeatCount="indefinite"/></circle>')
    s.append(f'<text x="{gx}" y="{gy+gh+28}" font-size="12" fill="{MU}">day 1</text><text x="{gx+gw}" y="{gy+gh+28}" text-anchor="end" font-size="12" fill="{MU}">today</text></svg>')
    return "".join(s)

for f, fn in (("hero.svg", hero), ("skills-graph.svg", graph)):
    open(os.path.join(OUT, f), "w").write(fn())
