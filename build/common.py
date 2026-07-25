# Shared HTML fragments for Stearn Designs site generator

TICKER_ITEMS = [
    "Get in Touch With Your Projects",
    "Comprehensive Branding Systems",
    "Based in the UK",
    "Professional Web Design",
    "Social Media Management",
]

def ticker_html():
    items = "".join(f'<span class="ticker__item">{t}</span>' for t in TICKER_ITEMS)
    # duplicate the run twice for seamless 50% loop
    return f'''  <div class="ticker" aria-hidden="true">
    <div class="ticker__track">
      {items}
      {items}
    </div>
  </div>
'''

def head_html(title, description, root=""):
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{description}">

<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300..700&family=Urbanist:ital,wght@0,100..900;1,100..900&display=swap" rel="stylesheet">

<link rel="stylesheet" href="{root}css/style.css">
<link rel="icon" href="{root}assets/logo/stearn-designs-logo.png">
</head>
'''

NAV_LINKS = [
    ("index.html", "Home"),
    ("portfolio.html", "Portfolio"),
    ("gallery.html", "Gallery"),
    ("posters.html", "Posters"),
    ("index.html#contact", "Contact"),
]

def header_html(active, root=""):
    links = ""
    for href, label in NAV_LINKS:
        cls = " is-active" if label == active else ""
        links += f'<a href="{root}{href}" class="nav__links-item{cls}">{label}</a>'
    return f'''  <header class="site-header">
    <div class="site-header__inner">
      <a href="{root}index.html" class="logo">
        <img src="{root}assets/logo/stearn-designs-logo.png" alt="Stearn Designs logo">
      </a>
      <nav class="nav" id="siteNav">
        <div class="nav__links">
          {links}
        </div>
        <a href="{root}index.html#contact" class="nav__cta">Start a Project</a>
      </nav>
      <button class="nav-toggle" id="navToggle" aria-label="Toggle menu" aria-expanded="false">
        <span></span>
      </button>
    </div>
  </header>
'''

def footer_html(root=""):
    return f'''  <footer class="site-footer">
    <div class="wrap">
      <div class="site-footer__top">
        <div class="site-footer__brand">Stearn Designs</div>
        <ul class="site-footer__links">
          <li><a href="{root}index.html">Home</a></li>
          <li><a href="{root}portfolio.html">Portfolio</a></li>
          <li><a href="{root}gallery.html">Gallery</a></li>
          <li><a href="{root}posters.html">Posters</a></li>
          <li><a href="{root}index.html#contact">Contact</a></li>
        </ul>
      </div>
      <div class="site-footer__bottom">
        <span>&copy; 2026 Stearn Designs. All rights reserved.</span>
        <div class="site-footer__social">
          <a href="#" aria-label="Instagram">Instagram</a>
          <a href="#" aria-label="LinkedIn">LinkedIn</a>
          <a href="#" aria-label="Behance">Behance</a>
        </div>
      </div>
    </div>
  </footer>
'''

def lightbox_html():
    return '''  <div class="lightbox" data-lightbox>
    <div class="lightbox__stage-wrap">
      <div class="lightbox__stage"></div>
      <div class="lightbox__caption"></div>
    </div>
    <button class="lightbox__close" aria-label="Close">
      <svg viewBox="0 0 24 24" fill="none" stroke-width="2" stroke-linecap="round"><path d="M6 6l12 12M18 6L6 18"/></svg>
    </button>
    <button class="lightbox__nav lightbox__nav--prev" aria-label="Previous">
      <svg viewBox="0 0 24 24" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M15 18l-6-6 6-6"/></svg>
    </button>
    <button class="lightbox__nav lightbox__nav--next" aria-label="Next">
      <svg viewBox="0 0 24 24" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 18l6-6-6-6"/></svg>
    </button>
  </div>
'''

ARROW_SVG = '<svg viewBox="0 0 24 24" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M7 17L17 7M17 7H9M17 7V15"/></svg>'

def scripts_html(root=""):
    return f'  <script src="{root}js/main.js"></script>\n'
