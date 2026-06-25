#!/usr/bin/env python3
"""Generate Keith Christman's portfolio as plain static HTML.
Run at authoring time only; output is hand-editable HTML/CSS with no build step."""
import os, html

# Write alongside this script, so it runs from wherever the repo lives.
OUT = os.path.dirname(os.path.abspath(__file__))

SITE = "Keith Christman"
ROLE = "Mechanical & Mechatronics Engineer"
# Contact placeholders — Keith edits these (see README).
EMAIL = "keithschristman@gmail.com"
LINKEDIN = "https://www.linkedin.com/in/keith-christman-300a68103"

# ---------------------------------------------------------------- projects ---
PROJECTS = [
 dict(
   slug="mechanical-design", num="01", cat="Mechanical Design",
   imgdir="mechanical-design",
   hero="4-1.webp",
   oneliner="Dropper seatposts taken from free-body diagram to mass production — every part iterated to shed grams without losing strength.",
   chips=["96 PARTS","109 PG · 2D","8 MO → POC","CONCEPT→PRODUCTION"],
   lede="Two telescoping dropper-seatpost programs, each carried from first sketch to a "
        "fully detailed, manufacturable assembly. The work is the unglamorous core of "
        "mechanical design: load cases, tolerance stacks, and hundreds of detailed parts "
        "that all have to fit, seal, and survive.",
   blocks=[
     dict(type="prose", html=(
       "<p>The 34.9 Command Post was designed from concept to mass production. It started "
       "with a free-body diagram and a clear picture of the static and dynamic loads the "
       "post would see, then moved into part-by-part iteration aimed at minimizing mass "
       "while holding strength and stiffness targets. The program produced <strong>96 "
       "designed parts</strong> and <strong>109 pages of 2D</strong> documentation, and "
       "reached proof of concept in <strong>eight months</strong>.</p>")),
     dict(type="sub", label="Command Post 34.9"),
     dict(type="figs", layout="two", items=[
       ("sketch.webp","Early concept sketch — defining the architecture before any CAD.",""),
       ("notebook.webp","Free-body diagram and hand calculations: static and dynamic load cases.",""),
     ]),
     dict(type="figs", layout="three", items=[
       ("4-1.webp","Full CAD assembly.",""),
       ("4-2.webp","Exploded view — component breakdown.",""),
       ("4-3.webp","Assembly section, collapsed.",""),
     ]),
     dict(type="figs", layout="two", items=[
       ("2.webp","FEA: stress fields used to drive material down where it was not earning its weight.",""),
       ("3.webp","Structural analysis across the load cases.",""),
     ]),
     dict(type="figs", layout="two", items=[
       ("5.webp","Part of the 109-page 2D drawing package.",""),
       ("img_20190416_214737.webp","Prototype hardware and components on the bench.","cover"),
     ]),
     dict(type="figs", layout="one", items=[
       ("done.webp","Production release — the program reached mass production.","cover"),
     ]),
     dict(type="sub", label="Dropper Post — WU LT"),
     dict(type="prose", html=(
       "<p>A second dropper-post design worked out in full internal detail. The cross-sections "
       "below show the sealing, bushing, and actuation stack-up through the length of the "
       "post — the geometry that determines how smoothly it travels and how well it holds "
       "position under load.</p>")),
     dict(type="figs", layout="two", items=[
       ("full-assembly.webp","Full assembly (CAD).",""),
       ("full-assembly-cross-section.webp","Full-assembly cross-section.",""),
     ]),
     dict(type="figs", layout="three", items=[
       ("upper-cross-section.webp","Upper internal section.",""),
       ("mid-cross-section.webp","Mid internal section.",""),
       ("bottom-cross-section.webp","Lower internal section.",""),
     ]),
     dict(type="figs", layout="two", items=[
       ("wu-lt-on-bike.webp","Installed on the test bike.","cover"),
       ("wu-lt-on-bike-down.webp","Dropped, under rider weight.","cover"),
     ]),
   ],
 ),

 dict(
   slug="composites", num="02", cat="Composite Manufacturing & Design",
   imgdir="composites",
   hero="20150615_-brakethrough-media_a22y3850.webp",
   oneliner="Carbon wheelsets and structures from napkin sketch to molded prototype — plus an in-house process for cure-cycle hole piercing and a cross-section optimized for impact.",
   chips=["LAYUP → CURE","SILICONE MANDRELS","DOE-DRIVEN","1ST-PRINCIPLES"],
   lede="Designing and building structural carbon parts end to end: tooling, layup, cure, "
        "and the test data that closes the loop. The thread running through this work is "
        "treating composites as something you can analyze and optimize from first "
        "principles, not just lay up and hope.",
   blocks=[
     dict(type="prose", html=(
       "<p>Starting from napkin sketches and moving to 3D CAD, the goal each time was a "
       "structurally sound, functioning prototype. To get there quickly, we developed an "
       "in-house process for fabricating <strong>silicone mandrels</strong> to prototype "
       "hollow composite structures — the tooling that lets a one-off carbon part exist at "
       "all. I designed the wheelset and seatpost for the EPIC model family, taking a "
       "first-principles approach to validate different cross-sections that maximized "
       "impact resistance while minimizing mass.</p>")),
     dict(type="sub", label="Layup & Tooling"),
     dict(type="figs", layout="two", items=[
       ("20150615_-brakethrough-media_a22y3850.webp","Layup in progress on the shop floor.  Photo: BrakeThrough Media.","cover"),
       ("20150615_-brakethrough-media_a22y3885.webp","Prototyping and inspection in the shop.  Photo: BrakeThrough Media.","cover"),
     ]),
     dict(type="figs", layout="two", items=[
       ("20150615_-brakethrough-media_a10o6501.webp","A molded composite section in its tooling.  Photo: BrakeThrough Media.","cover"),
       ("x7.webp","Mandrel and tooling design (CAD).",""),
     ]),
     dict(type="figs", layout="three", items=[
       ("cutpieces.webp","Silicone-mandrel molded sections.",""),
       ("1stply.webp","Layup test pieces.",""),
       ("img_0260.webp","Carbon frame on the build jig.","cover"),
     ]),
     dict(type="sub", label="Shear-Out Resistance"),
     dict(type="prose", html=(
       "<p>One process innovation: improving the shear-out resistance of composite joints by "
       "piercing holes during the <strong>minimum-viscosity point of the cure cycle</strong> "
       "— when the resin is fluid enough to flow around the fibers rather than cutting "
       "through them, leaving a far stronger hole.</p>")),
     dict(type="figs", layout="two", items=[
       ("holes.webp","Holes pierced at the minimum-viscosity point of the cure.",""),
       ("holes2.webp","Detail of the pierced hole.",""),
     ]),
     dict(type="sub", label="Cross-Section Optimization"),
     dict(type="prose", html=(
       "<p>During impact testing, the spoke bed on the previous-generation Control SL failed "
       "under a compressive stress. Rather than simply adding material, I ran a design study: "
       "varying the cross-section height across a realistic range revealed a "
       "<strong>minimum stress at an ideal geometry</strong>, driving higher impact-energy "
       "tolerance without a mass penalty.</p>")),
     dict(type="figs", layout="two", items=[
       ("stress.webp","Spoke-bed stress as a function of cross-section moment of inertia — the minimum sets the target geometry.",""),
       ("doe.webp","Design-of-experiments setup and hoop-stiffness derivation.",""),
     ]),
     dict(type="figs", layout="two", items=[
       ("controlsl.webp","The wheelset, in production.","cover"),
       ("mtb.webp","On the bike.","cover"),
     ]),
     dict(type="figs", layout="two", items=[
       ("pullout.webp","Pull-out / shear test fixture.","cover"),
       ("flow.webp","Analysis workflow.",""),
     ]),
   ],
 ),

 dict(
   slug="mechatronics", num="03", cat="Mechatronics — LET",
   imgdir="mechatronics",
   hero="front.webp",
   oneliner="A linear electromagnetic transducer for harvesting energy from suspension motion — built, instrumented on the trail, and honestly assessed against its theoretical limit.",
   chips=["HALLBACH ARRAY","0.61 T PEAK","FEMM + MATLAB","TRAIL-VALIDATED"],
   lede="The LET (Linear Electromagnetic Transducer) was a research program asking a simple "
        "question: can the motion a mountain-bike suspension already dissipates be turned "
        "into useful electrical power? Two prototype generations took it from proof of "
        "concept to a trail-instrumented answer.",
   blocks=[
     dict(type="prose", html=(
       "<p>The transducer is a coreless linear generator. LET&nbsp;2.0 uses a cylindrical "
       "<strong>Halbach magnet array</strong> on an aluminum mover, which directs the "
       "magnetic flux radially across the coils and removes the need for a steel core. "
       "A 1,500-point FEMM magnetics model fed a MATLAB model of the device; peak radial "
       "flux climbed from roughly 0.4&nbsp;T on the first prototype to "
       "<strong>0.577&nbsp;T</strong>, and 0.61&nbsp;T on the refined LET&nbsp;2.2 "
       "magnet arrangement.</p>")),
     dict(type="sub", label="Architecture & Model"),
     dict(type="figs", layout="two", items=[
       ("front.webp","LET 2.0 — coil and magnet geometry (CAD).",""),
       ("model.webp","Theoretical model: radial magnetic flux from the Halbach array.",""),
     ]),
     dict(type="figs", layout="two", items=[
       ("arch.webp","Comparing LET architectures against the magnetics target.",""),
       ("build.webp","Coil wiring scheme and the physical build.",""),
     ]),
     dict(type="sub", label="Build & Test"),
     dict(type="prose", html=(
       "<p>Beyond the generator itself, the program meant building the supporting hardware: "
       "two-phase rectified coil sets, voltage-divider circuits to keep velocity-dependent "
       "voltage spikes inside a logging window, and enclosures for the battery and logger. "
       "The device was characterized on a dynamometer and then run on the trail in both "
       "fork-mounted (position-dependent) and tuned-mass-damper configurations.</p>")),
     dict(type="figs", layout="two", items=[
       ("sdf.webp","Hand-built: coils, soldering, and bench checks.","cover"),
       ("dyno.webp","Dynamometer sine-sweep testing, model correlation.",""),
     ]),
     dict(type="figs", layout="two", items=[
       ("hlgh.webp","Trail testing — fork-lower vertical mount on the bike.",""),
       ("wer.webp","Ride-session data: LET voltage tracked against fork position.",""),
     ]),
     dict(type="sub", label="The Honest Answer"),
     dict(type="prose", html=(
       "<p>The most useful result was a limit. By treating the maximum harvestable energy as "
       "the energy the damper already dissipates, the study put a ceiling on the whole idea. "
       "A free-to-oscillate tuned-mass-damper LET generated several times more energy than a "
       "fork-position-dependent one — but even at that, charging a small Live&nbsp;Neo battery "
       "would take many descents, and a real device (generator, one-way clutch, gearbox, power "
       "electronics) would add roughly <strong>600&nbsp;grams</strong>. For an industry that "
       "fights for 50&nbsp;grams on a crown, the conclusion was that the weight and feel cost "
       "outweighs the energy — a clear-eyed feasibility call backed by real numbers.</p>")),
     dict(type="figs", layout="two", items=[
       ("energy.webp","Upper bound: energy the damper already dissipates over a run.",""),
       ("concl.webp","Theoretical vs. measured energy across configurations.",""),
     ]),
   ],
 ),

 dict(
   slug="data-acquisition", num="04", cat="Data Acquisition",
   imgdir="data-acquisition",
   hero="5.webp",
   oneliner="A compact, purpose-built data logger for ride dynamics — custom PCB, onboard charging, and a quick-snap mount, designed board-up.",
   chips=["CUSTOM PCB","TEENSY","Li-ION CHARGING","6 DIG · 2 ANALOG"],
   lede="To get trustworthy suspension and ride-dynamics data you need a logger that fits the "
        "bike and the problem. So I designed one from the board up — the same DAQ that "
        "captured the data behind the LET and suspension work.",
   blocks=[
     dict(type="prose", html=(
       "<p>The logger is built around a <strong>Teensy soldered to a custom PCB</strong>, with "
       "a designed-in Li-ion charging circuit. It carries a 3-axis accelerometer and 3-axis "
       "gyroscope, <strong>six digital and two analog channels</strong>, and external channels "
       "for logging signals like a shaft-displacement potentiometer for fork position. A "
       "quick-snap mount makes it a full-frame, grab-and-go instrument.</p>")),
     dict(type="figs", layout="two", items=[
       ("pcb.webp","Custom PCB layout — 61.5 mm board, 'Christman Technologies'.",""),
       ("3.webp","Populated board.","cover"),
     ]),
     dict(type="figs", layout="two", items=[
       ("4.webp","Assembled logger with battery in a printed enclosure.","cover"),
       ("5.webp","Finished unit and quick-snap mount.","cover"),
     ]),
     dict(type="figs", layout="three", items=[
       ("fork1.webp","Mounted at the fork.","cover"),
       ("onbike1.webp","On the frame.","cover"),
       ("onbike2.webp","Full-frame implementation on the test bike.","cover"),
     ]),
     dict(type="figs", layout="one", items=[
       ("troubleshooting.webp","Bench validation — scope, meter, and the board under test.","cover"),
     ]),
   ],
 ),

 dict(
   slug="digital-products", num="05", cat="Digital Products & Research",
   imgdir="digital-products",
   hero="cv-pose-tracking.webp",
   oneliner="A physics model plus a computer-vision system that, together, redefine what an 'ideal' suspension setup is — and measure it from a single GoPro.",
   chips=["SDOF MODEL","COMPUTER VISION","RANDOM FOREST R²≈0.9","ASME PAPER"],
   lede="The most ambitious thread in my work: turning suspension setup from opinion into "
        "something you can define, measure, and reproduce. It pairs a mechanical model of "
        "the bike with an AI vision system that reads the rider — and the two together "
        "produced a result I believe is new to the industry.",
   download=dict(label="Read the white paper (PDF)", file="suspension-setup-white-paper.pdf"),
   blocks=[
     dict(type="prose", html=(
       "<p>For decades, setting up a mountain bike's suspension has been guided by sag charts "
       "and feel — an opinion rather than an informed decision. This project set out to answer "
       "what an ideal setup actually <em>is</em>, and why ideal varies so much from rider to "
       "rider.</p>"
       "<p>I built two things. The first is a software model that simulates how any fork and "
       "shock behaves on any bike for any rider — how firm it is, how quickly it settles, and "
       "how well front and rear are matched. The second is a measurement system built around a "
       "<strong>GoPro and a pose-tracking AI</strong> that determines, frame by frame, a "
       "rider's weight distribution and center of gravity while they ride.</p>")),
     dict(type="figs", layout="two", items=[
       ("cv-pose-tracking.webp","Pose-tracking pipeline: torso landmarks become five metrics fed to the model.",""),
       ("sdof-model.webp","Front and rear single-degree-of-freedom models of the bike.",""),
     ]),
     dict(type="sub", label="The Discovery"),
     dict(type="prose", html=(
       "<p>Putting the two together produced the central finding. An experienced rider "
       "continuously balances the bike with their body: as a trail steepens they shift "
       "rearward, keeping a familiar load on the front and rear contact patches — in effect "
       "keeping the front and rear suspension responding at the same rhythm. Across riders "
       "on different bikes with deliberately different setups, each one moved to a position "
       "that produced the <strong>same balanced natural-frequency response</strong>.</p>"
       "<p>The rider is the missing variable. The setup and the rider's body act as one "
       "system, and a good setup is simply one the rider can keep in balance across the "
       "trails they actually ride.</p>")),
     dict(type="figs", layout="two", items=[
       ("cg-across-gradients.webp","Rider center-of-gravity position across 5%, 30%, and 42% gradients.",""),
       ("balanced-response.webp","Settled riding position converging on a balanced front/rear response.",""),
     ]),
     dict(type="sub", label="How It's Measured"),
     dict(type="prose", html=(
       "<p>A <strong>random-forest regressor</strong> predicts rear-wheel bias and "
       "rider-system CG height from the five torso metrics, calibrated against a pair of "
       "wheel scales, reaching coefficients of determination of <strong>0.9 to 0.95</strong>. "
       "A multi-rider trail study across three trails of very different gradient "
       "(4.5%, 12.5%, and 42%) confirmed the behavior repeatedly. As far as I'm aware, this "
       "is the first time this rider behavior has been measured directly and tied to a working "
       "setup model — packaged in a MATLAB App Designer tool.</p>")),
     dict(type="figs", layout="one", items=[
       ("setup-application.webp","The Set-Up Application: the SDOF model behind an engineer-facing tool.",""),
     ]),
     dict(type="prose", html=(
       "<p>The work was written up as a formal engineering paper — <em>A Single-Degree-of-"
       "Freedom Model and Computer-Vision Methodology for Mountain Bicycle Suspension "
       "Set-Up</em> — and presented internally. The full paper is linked above.</p>")),
   ],
 ),

 dict(
   slug="van-build", num="06", cat="Net-Zero Sprinter — Master's Thesis",
   imgdir="van-build",
   hero="img_20190921_190736.webp",
   oneliner="A net-zero energy system designed, fabricated, and installed on a Sprinter van — then modeled so it can predict interior temperature from the weather forecast.",
   chips=["260 Ah LiFePO4","550 W SOLAR","MATLAB MODEL","PREDICTIVE CONTROL"],
   lede="My master's thesis: design, fabricate, and implement a net-zero energy platform for "
        "a mobile residence — and then build the thermal and electrical model that lets it "
        "make decisions about its own energy use.",
   download=dict(label="Read the thesis (PDF)", file="net-zero-sprinter-thesis.pdf"),
   blocks=[
     dict(type="prose", html=(
       "<p>The hardware is a complete off-grid energy system on a Sprinter van: two 275&nbsp;W "
       "Canadian Solar panels on MIG-welded steel mounting frames, a Victron SmartSolar MPPT "
       "charge controller, a <strong>260&nbsp;Ah LiFePO4</strong> battery, a 2,000&nbsp;W "
       "inverter, and a custom electrical containment box housing the battery management, "
       "disconnects, and load lines. The goal was a self-sufficient platform for off-grid "
       "living and exploring.</p>")),
     dict(type="figs", layout="two", items=[
       ("img_20190921_190736.webp","The platform — a Sprinter built to run net-zero.","cover"),
       ("6.webp","Solar panels mounted to the roof.","cover"),
     ]),
     dict(type="sub", label="Electrical System"),
     dict(type="figs", layout="three", items=[
       ("1.webp","Charge-controller board (LTC4015-based design exploration).","cover"),
       ("3.webp","Charge controller install and electrical containment box.",""),
       ("4.webp","Fabricating the steel solar-panel mounting frames.","cover"),
     ]),
     dict(type="sub", label="Thermal + Electrical Model"),
     dict(type="prose", html=(
       "<p>The second half of the thesis is a model. Using acquired thermal data, I built a "
       "thermal and electrical model of the van in MATLAB that predicts interior temperature "
       "from forecasted conditions, and tells the user how a desired set-point temperature "
       "will affect how long the system's stored solar energy lasts. It closes the loop from "
       "<strong>weather forecast → thermal response → battery state of charge</strong>, so the "
       "platform can inform real energy-use decisions.</p>")),
     dict(type="figs", layout="two", items=[
       ("matlab2.webp","Set-point temperature prediction from forecast and battery state.",""),
       ("thermal.webp","Thermal-model data acquisition at the bench.","cover"),
     ]),
     dict(type="sub", label="Living In It"),
     dict(type="figs", layout="three", items=[
       ("img_20200412_185658.webp","Interior — sleeping platform.","cover"),
       ("img_20200412_185750.webp","Interior — galley.","cover"),
       ("img_20200412_185459.webp","Loaded up and ready.","cover"),
     ]),
   ],
 ),
]

BYSLUG = {p["slug"]: p for p in PROJECTS}

# ---------------------------------------------------------------- helpers ----
def esc(s): return html.escape(s, quote=True)

def head(title, prefix, desc):
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<script>document.documentElement.classList.add('js')</script>
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="icon" href="{prefix}favicon.svg" type="image/svg+xml">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:type" content="website">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo:wght@500;600;700;800&family=IBM+Plex+Mono:wght@400;500;600&family=IBM+Plex+Sans:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{prefix}css/style.css">
</head>
<body>"""

def nav(prefix, current):
    def cur(p): return ' aria-current="page"' if p==current else ''
    return f"""
<header class="nav"><div class="wrap">
  <a class="brand" href="{prefix}index.html">
    <span class="mark">KC</span>
    <span class="who">{esc(SITE)} · Engineering</span>
  </a>
  <nav class="nav-links">
    <a href="{prefix}index.html#work"{cur('work')}>Work</a>
    <a href="{prefix}about.html"{cur('about')}>About</a>
    <a href="mailto:{esc(EMAIL)}">Contact</a>
  </nav>
</div></header>"""

def footer(prefix):
    return f"""
<footer><div class="wrap">
  <div>
    <div class="who">{esc(SITE)}</div>
    <div class="meta">{esc(ROLE)}</div>
  </div>
  <nav class="links">
    <a href="{prefix}index.html#work">Work</a>
    <a href="{prefix}about.html">About</a>
    <a href="mailto:{esc(EMAIL)}">Email</a>
    <a href="{esc(LINKEDIN)}">LinkedIn</a>
  </nav>
  <div class="meta">© <span id="yr"></span> {esc(SITE)}</div>
</div></footer>
<div class="lb" id="lb" role="dialog" aria-modal="true" aria-label="Image viewer">
  <button class="x" id="lbx" aria-label="Close">CLOSE ✕</button>
  <img id="lbimg" alt="">
</div>
<script src="{prefix}js/main.js"></script>
</body></html>"""

def dim(label, num=None, ticked=True):
    n = f'<span class="n">{esc(num)}</span> ' if num else ''
    return f'<div class="dim {"ticked" if ticked else ""}"><span class="lab">{n}{esc(label)}</span></div>'

def figure(imgdir, item, prefix, fignum):
    img, cap, fit = item
    cls = "fig cover" if fit=="cover" else "fig"
    src = f"{prefix}images/{imgdir}/{img}"
    return (f'<figure class="{cls} reveal">'
            f'<div class="imgwrap"><img src="{src}" alt="{esc(cap)}" loading="lazy" '
            f'data-full="{src}"></div>'
            f'<figcaption><span class="fn">FIG&nbsp;{fignum:02d}</span>{esc(cap)}</figcaption>'
            f'</figure>')

def chips(items):
    return '<div class="stats">'+''.join(f'<span class="chip">{esc(c)}</span>' for c in items)+'</div>'

# ---------------------------------------------------------------- index ------
def render_index():
    p = ""
    cards = ""
    for pr in PROJECTS:
        cards += f"""
      <a class="card reveal" href="projects/{pr['slug']}.html">
        <div class="shot"><img src="images/{pr['imgdir']}/{pr['hero']}" alt="{esc(pr['cat'])}" loading="lazy"></div>
        <div class="body">
          <span class="tag"><span class="n">{esc(pr['num'])}</span> / {esc(pr['cat'])}</span>
          <h3>{esc(pr['cat'])}</h3>
          <p class="desc">{esc(pr['oneliner'])}</p>
          <div class="stats">{''.join(f'<span class="chip">{esc(c)}</span>' for c in pr['chips'][:3])}</div>
        </div>
      </a>"""
    return head(f"{SITE} — {ROLE}", p,
                "Engineering portfolio of Keith Christman: mechanical design, composites, "
                "mechatronics, data acquisition, and ride-dynamics research.") + nav(p,'home') + f"""
<main>
  <section class="hero"><div class="wrap">
    <span class="eyebrow">{esc(ROLE)}</span>
    <h1>Keith<span class="l2">Christman</span></h1>
    <p class="thesis">I design mechanical and mechatronic systems for ride dynamics —
      from production dropper posts and carbon wheelsets to energy-harvesting transducers,
      custom data loggers, and the models that tie them together.</p>
    <div class="titleblock">
      <div class="cell"><div class="k">Discipline</div><div class="v">Mechanical · Mechatronics</div></div>
      <div class="cell"><div class="k">Focus</div><div class="v">Ride Dynamics &amp; Suspension</div></div>
      <div class="cell"><div class="k">Methods</div><div class="v">CAD · FEA · MATLAB · Test</div></div>
      <div class="cell"><div class="k">Projects</div><div class="v">06 Selected</div></div>
    </div>
  </div></section>

  <section class="work" id="work"><div class="wrap">
    {dim('Selected Work','06')}
    <div class="grid">{cards}
    </div>
  </div></section>
</main>""" + footer(p)

# ---------------------------------------------------------------- project ----
def render_project(pr, i):
    p = "../"
    fignum = 0
    body = ""
    for b in pr["blocks"]:
        if b["type"]=="prose":
            body += f'<div class="prose reveal">{b["html"]}</div>'
        elif b["type"]=="sub":
            body += f'<div class="sub">{dim(b["label"])}</div>'
        elif b["type"]=="figs":
            figs=""
            for it in b["items"]:
                fignum += 1
                figs += figure(pr["imgdir"], it, p, fignum)
            body += f'<div class="figs {b["layout"]}">{figs}</div>'

    prev = PROJECTS[i-1] if i>0 else None
    nxt  = PROJECTS[i+1] if i<len(PROJECTS)-1 else None
    pnav = '<nav class="pnav">'
    if prev: pnav += f'<a class="prev" href="{prev["slug"]}.html"><span class="d">← Prev</span>{esc(prev["cat"])}</a>'
    else: pnav += '<span></span>'
    if nxt: pnav += f'<a class="next" href="{nxt["slug"]}.html"><span class="d">Next →</span>{esc(nxt["cat"])}</a>'
    pnav += '</nav>'

    dl = ""
    if pr.get("download"):
        d = pr["download"]
        dl = (f'<a class="dl" href="{p}docs/{d["file"]}" target="_blank" rel="noopener">'
              f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">'
              f'<path d="M12 3v12m0 0l-4-4m4 4l4-4M4 21h16"/></svg>{esc(d["label"])}</a>')

    return head(f"{pr['cat']} — {SITE}", p, pr["oneliner"]) + nav(p,'work') + f"""
<main>
  <div class="wrap">
    <div class="crumb"><a href="../index.html#work">← All Work</a></div>
    <section class="phead">
      <span class="tag"><span class="n">{esc(pr['num'])}</span> / {esc(ROLE)}</span>
      <h1>{esc(pr['cat'])}</h1>
      <p class="lede">{esc(pr['lede'])}</p>
      <div class="statrow">{''.join(f'<span class="chip">{esc(c)}</span>' for c in pr['chips'])}</div>
      {dl}
    </section>
    {body}
    {pnav}
  </div>
</main>""" + footer(p)

# ---------------------------------------------------------------- about ------
def render_about():
    p = ""
    return head(f"About — {SITE}", p,
                f"About {SITE}, {ROLE.lower()}.") + nav(p,'about') + f"""
<main>
  <div class="wrap">
    <section class="phead" style="padding-top:48px">
      <span class="eyebrow" style="display:block;margin-bottom:18px">About</span>
      <h1>{esc(SITE)}</h1>
    </section>
    <div class="abt-grid">
      <div class="prose mt0">
        <p>I'm a mechanical and mechatronics engineer focused on ride dynamics. My work runs
        from the very physical — dropper posts and carbon wheelsets carried from free-body
        diagram to mass production — to the computational, building physics models and
        computer-vision systems that turn rider feel into something measurable.</p>
        <p>I tend to work end to end: sketch, CAD, FEA, the custom electronics and data
        loggers needed to test a thing, and the MATLAB models that make sense of the data. I
        like problems where the answer isn't just a better part but a better way of
        understanding what "better" even means — like defining an ideal suspension setup as a
        balanced front-and-rear natural frequency, then measuring it from a single camera.</p>
        <p>Recent work includes a single-degree-of-freedom suspension model paired with a
        pose-tracking vision system for rider center-of-gravity, a linear electromagnetic
        energy-harvesting transducer, and a net-zero energy platform with predictive thermal
        control as my master's thesis.</p>
        <p>The fastest way to reach me is by <a href="mailto:{esc(EMAIL)}">email</a>.</p>
      </div>
      <aside>
        <div class="caps">
          <div class="h">Capabilities</div>
          <ul>
            <li><span class="b">›</span> Mechanical design · DFM · GD&amp;T</li>
            <li><span class="b">›</span> FEA &amp; structural optimization</li>
            <li><span class="b">›</span> Composite design &amp; manufacturing</li>
            <li><span class="b">›</span> Mechatronics · PCB · embedded</li>
            <li><span class="b">›</span> Data acquisition &amp; instrumentation</li>
            <li><span class="b">›</span> MATLAB modeling &amp; simulation</li>
            <li><span class="b">›</span> Computer vision · ML (random forests)</li>
            <li><span class="b">›</span> Suspension &amp; vehicle dynamics</li>
          </ul>
        </div>
        <div class="caps" style="margin-top:18px">
          <div class="h">Contact</div>
          <ul>
            <li><span class="b">›</span> <a href="mailto:{esc(EMAIL)}" style="text-decoration:none;color:inherit">{esc(EMAIL)}</a></li>
            <li><span class="b">›</span> <a href="{esc(LINKEDIN)}" style="text-decoration:none;color:inherit">LinkedIn</a></li>
          </ul>
        </div>
      </aside>
    </div>
  </div>
</main>""" + footer(p)

# ---------------------------------------------------------------- write ------
os.makedirs(f"{OUT}/projects", exist_ok=True)
os.makedirs(f"{OUT}/js", exist_ok=True)

open(f"{OUT}/index.html","w").write(render_index())
open(f"{OUT}/about.html","w").write(render_about())
for i,pr in enumerate(PROJECTS):
    open(f"{OUT}/projects/{pr['slug']}.html","w").write(render_project(pr,i))

print("Wrote index.html, about.html, and", len(PROJECTS), "project pages.")
