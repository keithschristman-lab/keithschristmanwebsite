# Keith Christman — Engineering Portfolio

A plain HTML/CSS/JS static site. **No build step, no framework, no dependencies.**
Open the files, edit them, push them. That's the whole workflow.

```
index.html              Home — hero + work grid
about.html              About + capabilities + contact
projects/*.html         One page per project (6)
css/style.css           The entire design system
js/main.js              Scroll reveal + image lightbox (optional enhancement)
images/<project>/       Optimized web images (webp)
docs/                   Downloadable PDFs (white paper, thesis)
favicon.svg             Site icon
generate.py             Optional: regenerates the HTML from content (see below)
.nojekyll               Tells GitHub Pages to serve files as-is
```

The whole site is ~12 MB — comfortably inside GitHub's limits.

---

## 1. Preview locally

Exactly like before with Live Server:

- **VS Code:** right-click `index.html` → *Open with Live Server*.
- **Or any terminal:** `python3 -m http.server` in this folder, then open
  `http://localhost:8000`.

Just double-clicking `index.html` mostly works too, but a local server is more
faithful (relative paths, etc.).

---

## 2. Put it on GitHub Pages (free)

1. Create a new GitHub repository.
   - Name it **`yourusername.github.io`** if you want the site at the root of your
     GitHub account, **or** any name (e.g. `portfolio`) for a project site at
     `yourusername.github.io/portfolio`.
2. Upload everything in this folder to the repo (drag-and-drop into the GitHub web
   uploader works, or use git):
   ```bash
   git init
   git add .
   git commit -m "Portfolio site"
   git branch -M main
   git remote add origin https://github.com/YOURNAME/REPO.git
   git push -u origin main
   ```
3. In the repo: **Settings → Pages → Build and deployment**.
   Set **Source = Deploy from a branch**, **Branch = `main`**, **Folder = `/ (root)`**.
   Save. Give it a minute; your site appears at the URL shown there.

That's it — every push updates the live site.

---

## 3. Point keithschristman.com at it

You already own **keithschristman.com** (currently on Squarespace). To move it:

1. **In GitHub:** Settings → Pages → **Custom domain** → enter `keithschristman.com`
   → Save. (GitHub adds a `CNAME` file to the repo automatically.)
2. **In your DNS host** (see the note below about where that is), add:
   - For the apex `keithschristman.com`, four **A records**:
     ```
     185.199.108.153
     185.199.109.153
     185.199.110.153
     185.199.111.153
     ```
     (and optionally the matching AAAA/IPv6 records GitHub lists in its docs)
   - For `www`, one **CNAME** record → `YOURNAME.github.io`
3. Wait for DNS to propagate (minutes to a few hours), then back in
   Settings → Pages, tick **Enforce HTTPS** once the certificate is issued.

**Where is your DNS?** keithschristman.com is on Squarespace right now, so Squarespace
is likely both your registrar and DNS host. You can either add the records above in
Squarespace's DNS settings, or move the domain elsewhere — your call. GitHub's current
instructions live at *docs.github.com → Pages → Configuring a custom domain*; follow
those if the IPs ever change.

> **Don't cancel Squarespace until the new site is confirmed live on
> keithschristman.com.** Keep the old site up as a fallback while DNS propagates.
> Once `https://keithschristman.com` loads this site correctly, you're safe to cancel
> the Squarespace subscription. (If Squarespace is also your *registrar*, make sure you
> either keep the domain registration or transfer it out before cancelling — cancelling
> hosting and losing the domain are two different things.)

---

## 4. Edit content

Two ways — pick whichever you like:

**A. Just edit the HTML.** Every page is plain, readable HTML. Change text, swap an
image `src`, add a `<figure>` — done. This is the simplest path and needs nothing
installed.

**B. Edit `generate.py` and regenerate.** All the words, image lists, captions, and
stats live in one `PROJECTS` data structure at the top of `generate.py`. Edit there,
then run:
```bash
python3 generate.py
```
It rewrites `index.html`, `about.html`, and the six project pages from that content,
so everything stays consistent. (Needs Python 3 — nothing else.)

### Set your real contact details
Right now these are **placeholders**:
- Email: `hello@keithschristman.com`
- LinkedIn: a generic URL

Update them at the top of `generate.py` (`EMAIL` and `LINKEDIN`) and re-run, **or**
find-and-replace them across the `.html` files. (I deliberately did **not** publish
your work email.)

### Add or replace images
Drop web-sized images into the right `images/<project>/` folder and reference them in
the HTML (or in `generate.py`). Keep them optimized — the originals you sent were
38 MB; the versions here are 5.6 MB total (resized to ~1600 px, converted to webp).
If you add big originals, shrink them first so pages stay fast.

---

## 5. About videos

Per what we discussed: **keep video files out of this repo.** Free static hosts cap
file sizes and bandwidth, and some prohibit video outright. When you want video:

- **Easiest:** upload to YouTube or Vimeo and embed the player.
- **Self-hosted look:** put the file on Cloudflare R2 (10 GB free, no egress fees) and
  point an HTML5 `<video>` tag at it.

Either way the video lives elsewhere; only the embed/link goes in the site.

---

## Note on URLs

Your project structure changed from the old Squarespace site (new categories,
different page names), so individual project URLs are different. That's expected when
restructuring — just be aware any old deep links you've shared won't map 1:1.

---

*Built as plain, dependency-free HTML/CSS. Design language: technical drafting —
drafting-grid ground, hairline frames, dimension-line dividers, and a single anodized
accent.*
