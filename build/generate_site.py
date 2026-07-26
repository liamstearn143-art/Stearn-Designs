import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from common import ticker_html, head_html, header_html, footer_html, lightbox_html, scripts_html, ARROW_SVG
from projects_data import PROJECTS, SERVICES, POSTERS

SITE = "/home/claude/site"

PLAY_SVG = '<svg class="icon-play" viewBox="0 0 24 24" fill="currentColor" stroke="none"><path d="M8 5v14l11-7z" fill="var(--cream)"/></svg>'
PAUSE_SVG = '<svg class="icon-pause" viewBox="0 0 24 24" fill="currentColor" stroke="none"><rect x="6" y="5" width="4" height="14" fill="var(--cream)"/><rect x="14" y="5" width="4" height="14" fill="var(--cream)"/></svg>'
PREV_SVG = '<svg viewBox="0 0 24 24" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M15 18l-6-6 6-6"/></svg>'
NEXT_SVG = '<svg viewBox="0 0 24 24" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 18l6-6-6-6"/></svg>'
EXPAND_SVG = '<svg viewBox="0 0 24 24" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 4H4v5M15 4h5v5M9 20H4v-5M15 20h5v-5"/></svg>'
CAMERA_PLAY_SVG = '<svg viewBox="0 0 24 24"><path d="M8 5v14l11-7z"/></svg>'
INSTAGRAM_SVG = '<svg viewBox="0 0 24 24" fill="none" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.2" cy="6.8" r="1"/></svg>'
EXTERNAL_LINK_SVG = '<svg viewBox="0 0 24 24" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M7 17L17 7M9 7h8v8"/></svg>'
INSTAGRAM_URL = "https://www.instagram.com/stearndesigns/"

def instagram_section_html():
    return f'''
  <section class="instagram-section">
    <div class="wrap">
      <div class="instagram-section__head">
        <div>
          <p class="eyebrow">Follow Along</p>
          <h2>Recent Work On Instagram</h2>
          <span class="instagram-section__handle">
            <a href="{INSTAGRAM_URL}" target="_blank" rel="noopener">@stearndesigns</a>
          </span>
        </div>
        <a href="{INSTAGRAM_URL}" target="_blank" rel="noopener" class="instagram-follow-btn">
          {INSTAGRAM_SVG} Follow on Instagram
        </a>
      </div>

      <div class="instagram-embed" id="instagram-live-embed">
        <!-- SnapWidget -->
        <script src="https://snapwidget.com/js/snapwidget.js"></script>
        <iframe src="https://snapwidget.com/embed/1127696" class="snapwidget-widget" allowtransparency="true" frameborder="0" scrolling="no" style="border:none; overflow:hidden; width:100%;" title="Posts from Instagram"></iframe>
      </div>

    </div>
  </section>
'''


def write(path, content):
    full = os.path.join(SITE, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w") as f:
        f.write(content)
    print("wrote", path)


# ---------------------------------------------------------------------------
# INDEX
# ---------------------------------------------------------------------------
def build_index():
    root = ""
    services_cards = ""
    for i, s in enumerate(SERVICES, start=1):
        services_cards += f'''
        <a href="portfolio.html" class="service-card reveal">
          <span class="service-card__num">{i:02d}</span>
          <div class="service-card__media"><img src="assets/icons/{s['icon']}" alt="" loading="lazy"></div>
          <div class="service-card__scrim"></div>
          <div class="service-card__body">
            <h3>{s['title']}</h3>
            <p>{s['desc']}</p>
            <span class="service-card__arrow">{ARROW_SVG}</span>
          </div>
        </a>'''

    project_cards = ""
    for p in PROJECTS:
        hero_path = f"assets/projects/{p['slug']}/{p['hero']}"
        project_cards += f'''
        <a href="projects/{p['slug']}.html" class="project-card reveal">
          <div class="project-card__frame">
            <img src="{hero_path}" alt="{p['title']} project cover" loading="lazy">
            <span class="project-card__tag">{p['tags'][0]}</span>
            <div class="project-card__meta">
              <h3>{p['title']} {ARROW_SVG}</h3>
              <span>{p['card_desc']}</span>
            </div>
          </div>
        </a>'''

    content = f'''{head_html("Stearn Designs — Design With Edge.", "Freelance brand, web and motion design studio based in the UK. Branding, web design, motion design, social media management and poster design.", root)}
<body>
{ticker_html()}
{header_html("Home", root)}

  <section class="hero">
    <div class="hero__video-wrap">
      <video class="hero__video" autoplay muted loop playsinline poster="">
        <source src="assets/showreel/Showreel.mp4" type="video/mp4">
      </video>
    </div>
    <div class="hero__scrim"></div>
    <div class="hero__content">
      <p class="eyebrow hero__eyebrow">Design &middot; Motion &middot; Web</p>
      <h1>Design With Edge.</h1>
      <div class="hero__row">
        <p class="hero__lede">Crafting brands, sites, and content that cut through the noise.</p>
        <div class="hero__ctas">
          <a href="portfolio.html" class="btn btn--solid">View Portfolio</a>
          <a href="#contact" class="btn btn--outline">Start a Project</a>
        </div>
      </div>
    </div>
  </section>

  <section class="section" id="services">
    <div class="wrap">
      <div class="section__head">
        <div>
          <p class="eyebrow">What I Do</p>
          <h2>Services Built For Impact</h2>
        </div>
      </div>
      <div class="services-grid">{services_cards}
      </div>
    </div>
  </section>

  <section class="section" id="work">
    <div class="wrap">
      <div class="section__head">
        <div>
          <p class="eyebrow">Selected Work</p>
          <h2>Selected Projects</h2>
        </div>
        <a href="portfolio.html" class="section__link">See all projects</a>
      </div>
      <div class="projects-grid">{project_cards}
      </div>
    </div>
  </section>

  <section class="contact" id="contact">
    <div class="wrap">
      <div class="contact__grid">
        <div class="contact__info reveal">
          <p class="eyebrow">Get In Touch</p>
          <h2>Start Your Project</h2>
          <p>Tell me a little about what you're working on and I'll come back to you within a couple of days with next steps.</p>
          <div class="contact__detail"><span>Email</span><a href="mailto:liam@stearndesigns.com">liam@stearndesigns.com</a></div>
          <div class="contact__detail"><span>Location</span><span>United Kingdom</span></div>
          <div class="contact__detail"><span>Social</span><span>Instagram &middot; LinkedIn &middot; Behance</span></div>
        </div>
        <form class="contact-form reveal" data-contact-form novalidate>
          <div class="form-row">
            <div class="form-field">
              <input type="text" id="name" name="name" placeholder=" " required>
              <label for="name">Full Name</label>
            </div>
            <div class="form-field">
              <input type="email" id="email" name="email" placeholder=" " required>
              <label for="email">Email Address</label>
            </div>
          </div>
          <div class="form-field">
            <input type="text" id="project" name="project" placeholder=" ">
            <label for="project">Project Type</label>
          </div>
          <div class="form-field">
            <textarea id="message" name="message" placeholder=" " required></textarea>
            <label for="message">Tell me about your project</label>
          </div>
          <button type="submit" class="contact-form__submit">Send Message</button>
          <p class="form-status" role="status" aria-live="polite"></p>
        </form>
      </div>
    </div>
  </section>
{instagram_section_html()}
{footer_html(root)}
{scripts_html(root)}</body>
</html>
'''
    write("index.html", content)


# ---------------------------------------------------------------------------
# PORTFOLIO
# ---------------------------------------------------------------------------
def build_portfolio():
    root = ""
    project_cards = ""
    for p in PROJECTS:
        hero_path = f"assets/projects/{p['slug']}/{p['hero']}"
        project_cards += f'''
        <a href="projects/{p['slug']}.html" class="project-card reveal">
          <div class="project-card__frame">
            <img src="{hero_path}" alt="{p['title']} project cover" loading="lazy">
            <span class="project-card__tag">{p['tags'][0]}</span>
            <div class="project-card__meta">
              <h3>{p['title']} {ARROW_SVG}</h3>
              <span>{p['card_desc']}</span>
            </div>
          </div>
        </a>'''

    content = f'''{head_html("Portfolio — Stearn Designs", "Full portfolio of branding, web design, motion and print projects by Stearn Designs.", root)}
<body>
{ticker_html()}
{header_html("Portfolio", root)}

  <section class="portfolio-hero page-hero">
    <div class="wrap">
      <p class="eyebrow">Full Portfolio</p>
      <h1>Every Project, One Place.</h1>
      <p>A running record of brand, web, motion and print work — click into any project for the full gallery.</p>
    </div>
  </section>

  <section class="portfolio-grid-section">
    <div class="wrap">
      <div class="projects-grid">{project_cards}
      </div>
    </div>
  </section>

{footer_html(root)}
{scripts_html(root)}</body>
</html>
'''
    write("portfolio.html", content)


# ---------------------------------------------------------------------------
# GALLERY (masonry, all project images)
# ---------------------------------------------------------------------------
def build_gallery():
    root = ""
    filters = '<button class="is-active" data-filter="all">All Work</button>'
    for p in PROJECTS:
        filters += f'<button data-filter="{p["slug"]}">{p["title"]}</button>'

    items = ""
    for p in PROJECTS:
        images = [(p["hero"], p["title"] + " — Hero")] + list(p["gallery"])
        for src, cap in images:
            path = f"assets/projects/{p['slug']}/{src}"
            items += f'''
        <figure class="masonry-item" data-project="{p['slug']}">
          <a href="#" data-lightbox-src="{path}" data-lightbox-caption="{p['title']} — {cap}">
            <img src="{path}" alt="{p['title']} — {cap}" loading="lazy">
          </a>
          <span class="masonry-item__tag">{p['title']}</span>
        </figure>'''

    content = f'''{head_html("Gallery — Stearn Designs", "A masonry gallery of every image across the Stearn Designs project portfolio.", root)}
<body>
{ticker_html()}
{header_html("Gallery", root)}

  <section class="page-hero">
    <div class="wrap">
      <p class="eyebrow">Full Gallery</p>
      <h1>Every Image, Together.</h1>
      <p>Filter by project or scroll the full mix — click any image to view it full-size.</p>
    </div>
  </section>

  <section class="section" style="border-bottom:none;">
    <div class="wrap">
      <div class="masonry-filters" data-masonry-filters>
        {filters}
      </div>
      <div class="masonry" data-masonry-grid data-gallery-group>{items}
      </div>
    </div>
  </section>

{footer_html(root)}
{lightbox_html()}
{scripts_html(root)}</body>
</html>
'''
    write("gallery.html", content)


# ---------------------------------------------------------------------------
# POSTERS (scrolling gallery)
# ---------------------------------------------------------------------------
def build_posters():
    root = ""
    def rail(items, reverse=False):
        cards = ""
        doubled = items + items  # duplicate for seamless loop
        for post in doubled:
            path = f"assets/posters/{post['src']}"
            cards += f'''
          <a href="#" class="poster-card" data-lightbox-src="{path}" data-lightbox-caption="{post['label']}">
            <img src="{path}" alt="{post['label']}" loading="lazy">
            <span class="poster-card__label">{post['label']}</span>
          </a>'''
        cls = " reverse" if reverse else ""
        return f'''
      <div class="posters-rail-outer">
        <div class="posters-rail{cls}" data-gallery-group>{cards}
        </div>
      </div>'''

    half = len(POSTERS)
    row1 = POSTERS[:max(1, half // 2 + half % 2)] or POSTERS
    row2 = POSTERS[max(1, half // 2 + half % 2):] or POSTERS

    content = f'''{head_html("Posters — Stearn Designs", "A scrolling gallery of poster and cover art design work by Stearn Designs.", root)}
<body>
{ticker_html()}
{header_html("Posters", root)}

  <section class="posters-hero page-hero">
    <div class="wrap">
      <p class="eyebrow">Poster &amp; Cover Art</p>
      <h1>Print That Stops You.</h1>
      <p>An auto-scrolling rail of poster and cover art design — hover or tap a row to pause, click any poster to view it full-size.</p>
    </div>
  </section>

  <section class="posters-rail-section">
    {rail(row1, reverse=False)}
    {rail(row2 if row2 else row1, reverse=True)}
  </section>

{footer_html(root)}
{lightbox_html()}
{scripts_html(root)}</body>
</html>
'''
    write("posters.html", content)


# ---------------------------------------------------------------------------
# PROJECT PAGES
# ---------------------------------------------------------------------------
def build_project_pages():
    root = "../"
    for p in PROJECTS:
        slug = p["slug"]
        tags_html = "".join(f"<span>{t}</span>" for t in p["tags"])

        # hero media: video for bolt (seamless use of BoltAnimation.mp4), image otherwise
        if p.get("video"):
            hero_media = f'''<video autoplay muted loop playsinline>
          <source src="../assets/projects/{slug}/{p['video']}" type="video/mp4">
        </video>'''
        else:
            hero_media = f'<img src="../assets/projects/{slug}/{p["hero"]}" alt="{p["title"]} hero image" loading="lazy">'

        # gallery track: include hero image as first still, plus bolt animation as an inline video item
        gallery_items = ""
        first_items = []
        if p.get("video"):
            first_items.append(("video", p["video"], p["title"] + " — Brand Animation"))
        first_items.append(("image", p["hero"], p["title"] + " — Hero"))
        for src, cap in p["gallery"]:
            first_items.append(("image", src, p["title"] + " — " + cap))

        for kind, src, cap in first_items:
            path = f"../assets/projects/{slug}/{src}"
            if kind == "video":
                gallery_items += f'''
          <div class="gallery-item is-video" data-gallery-group>
            <a href="#" data-lightbox-src="{path}" data-lightbox-type="video" data-lightbox-caption="{cap}">
              <video muted loop autoplay playsinline>
                <source src="{path}" type="video/mp4">
              </video>
              <span class="play-badge">{CAMERA_PLAY_SVG} Watch animation</span>
            </a>
          </div>'''
            else:
                gallery_items += f'''
          <div class="gallery-item" data-gallery-group>
            <a href="#" data-lightbox-src="{path}" data-lightbox-caption="{cap}">
              <img src="{path}" alt="{cap}" loading="lazy">
            </a>
            <button class="expand" aria-label="Expand image" tabindex="-1">{EXPAND_SVG}</button>
            <span class="gallery-item__cap">{cap}</span>
          </div>'''

        # related projects (next two)
        idx = PROJECTS.index(p)
        others = (PROJECTS[idx+1:] + PROJECTS[:idx])[:3]
        related_cards = ""
        for o in others:
            hero_path = f"../assets/projects/{o['slug']}/{o['hero']}"
            related_cards += f'''
        <a href="{o['slug']}.html" class="project-card reveal">
          <div class="project-card__frame">
            <img src="{hero_path}" alt="{o['title']} project cover" loading="lazy">
            <span class="project-card__tag">{o['tags'][0]}</span>
            <div class="project-card__meta">
              <h3>{o['title']} {ARROW_SVG}</h3>
              <span>{o['card_desc']}</span>
            </div>
          </div>
        </a>'''

        content = f'''{head_html(p["title"] + " — Stearn Designs", p["description"], root)}
<body>
{ticker_html()}
{header_html("Portfolio", root)}

  <section class="project-hero">
    <div class="wrap">
      <a href="../portfolio.html" class="back-link">
        <svg viewBox="0 0 24 24" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M15 18l-6-6 6-6"/></svg>
        Back to Portfolio
      </a>
      <div class="project-hero__top">
        <div class="project-hero__title reveal">
          <p class="eyebrow">Case Study</p>
          <h1>{p['title']}</h1>
          <p>{p['description']}</p>
        </div>
        <div class="project-hero__tags reveal">{tags_html}</div>
      </div>
    </div>
    <div class="project-hero__media">
      {hero_media}
    </div>
  </section>

  <section class="gallery-scroller">
    <div class="wrap">
      <div class="gallery-scroller__head">
        <h2>Project Gallery</h2>
        <div class="gallery-scroller__controls">
          <button class="gs-btn" data-gs-play aria-label="Play or pause auto-scroll">
            {PAUSE_SVG}{PLAY_SVG}
          </button>
          <button class="gs-btn" data-gs-prev aria-label="Scroll left">{PREV_SVG}</button>
          <button class="gs-btn" data-gs-next aria-label="Scroll right">{NEXT_SVG}</button>
        </div>
      </div>
      <div class="gallery-track-outer" data-gallery-scroller>
        <div class="gallery-track">{gallery_items}
        </div>
      </div>
    </div>
  </section>

  <section class="section" style="border-top:1px solid var(--grey-line);">
    <div class="wrap">
      <div class="section__head">
        <div>
          <p class="eyebrow">Keep Exploring</p>
          <h2>More Projects</h2>
        </div>
        <a href="../portfolio.html" class="section__link">See all projects</a>
      </div>
      <div class="projects-grid">{related_cards}
      </div>
    </div>
  </section>

{footer_html(root)}
{lightbox_html()}
{scripts_html(root)}</body>
</html>
'''
        write(f"projects/{slug}.html", content)


if __name__ == "__main__":
    build_index()
    build_portfolio()
    build_gallery()
    build_posters()
    build_project_pages()
    print("ALL DONE")
