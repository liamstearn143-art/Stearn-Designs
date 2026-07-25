# Stearn Designs — website

A polished rebuild of the reference site, in plain HTML/CSS/JS (no build step —
just open the files or upload the whole folder to any static host / GitHub Pages).

## Structure

```
index.html          Home — ticker, video hero, services, selected projects, contact form
portfolio.html       Full project grid
gallery.html         Masonic gallery of every project image, filterable by project
posters.html         Auto-scrolling poster/cover-art rail
projects/            One page per project (see below)
css/style.css         All styling (design tokens live at the top of the file)
js/main.js            Nav, scroll reveals, gallery scroller, lightbox, contact form
assets/
  logo/                Site logo
  showreel/Showreel.mp4  Hero background video
  icons/               The 5 service card images you supplied
  projects/<slug>/     One folder per project — see "Dropping in real images" below
  posters/             Poster/cover art images used on posters.html
```

## Dropping in real images (framework is ready — just replace files)

You said not all assets were uploaded because of the limit — the site is built so you
can drop the rest straight in without touching any code:

1. **Project images**: for each project in `assets/projects/<slug>/`, replace the
   placeholder `hero.svg` and `gallery-01.svg` … `gallery-05.svg` files with your real
   images. **Keep the same filenames** (or update the two spots below if you rename
   them) and everything — homepage cards, portfolio grid, the project's own gallery
   scroller, and the masonry gallery page — updates automatically.
   - `alicia-faye-beauty/`, `alpha-red/`, `pilot-house/`, `plus/`, `origami/` are all
     currently placeholder graphics (dark diagonal panels with the project name) —
     purely so the layouts, hover states and galleries all work end-to-end already.
   - `bolt/` already has your real `bolt-hero.png` and `BoltAnimation.mp4` — only the
     5 `gallery-0X.svg` placeholders need swapping for the real coaching/competitions/
     jam poster photography.
   - Want more or fewer than 5 gallery images per project, or a different filename?
     Edit the single `PROJECTS` list in `/build/generate_site.py` → `projects_data.py`
     equivalent (see "Editing content" below) — everything regenerates from there.

2. **Posters page**: drop extra posters into `assets/posters/` and add them to the
   `POSTERS` list described below. `crucify-the-dead.png` is already wired in as a
   real example.

## Editing content (titles, descriptions, tags)

All project titles, tag chips, card blurbs and case-study copy live in one place —
`build/projects_data.py` (kept alongside this folder if you'd like the generator, or
just hand-edit the text directly inside each `projects/<slug>.html` file — it's plain
HTML, look for `<h1>`, the `<p>` under it, and the `.project-hero__tags` spans).

Services cards pull from the same pattern in `index.html` — edit the `<h3>` / `<p>`
text directly inside each `.service-card`.

## The Bolt project & video

`BoltAnimation.mp4` is used twice, on purpose:
- as the **ambient, muted, looping hero banner** at the top of `projects/bolt.html`
- as a **clickable tile inside the gallery scroller** — clicking it opens the same
  clip full-size, with sound and controls, in the lightbox

## Instagram feed (live, auto-updating)

The bottom of the home page runs a **live** SnapWidget embed of `@stearndesigns`
— already connected and working. It updates itself the moment you post: new
posts push in and the oldest tile drops off automatically, no site edits ever
needed. To change the layout (columns, captions, colours), log into
[snapwidget.com](https://snapwidget.com), edit the widget, and the site will
reflect it automatically — the embed code here doesn't need to change unless
you create a brand-new widget.

## Contact form

The form in `index.html#contact` is fully wired on the front end (validation,
floating labels, states) but needs one line to actually deliver email — open
`js/main.js`, find `ENDPOINT = ''` near the bottom, and set it to a free
[Formspree](https://formspree.io) endpoint (or Getform/Basin — same idea):

```js
const ENDPOINT = 'https://formspree.io/f/yourFormId';
```

Until you add that, submitting the form falls back to opening the visitor's email
client with the message pre-filled, so nothing is ever broken.

## Fonts & colours

Space Grotesk (display) + Urbanist (body) are loaded via the Google Fonts embed you
supplied, in the `<head>` of every page. Colour tokens are declared once at the top
of `css/style.css`:

```css
--cream: #fff6d9;
--grey:  #434343;
--black: #1a1a1a;
```

## Regenerating pages after edits

If you'd rather edit `build/projects_data.py` than hand-edit HTML, re-run:

```
python3 build/generate_site.py
```

from the project root — it rebuilds every page from the templates in
`build/common.py` + `build/generate_site.py`, so structure stays consistent across
all 10+ pages automatically.
