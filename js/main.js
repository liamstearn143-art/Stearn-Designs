/* ==========================================================================
   STEARN DESIGNS — shared behaviour
   Safe to include on every page: each block checks the DOM before running.
   ========================================================================== */

document.documentElement.classList.add('js');

/* ---------- mobile nav ---------- */
(function () {
  const toggle = document.querySelector('.nav-toggle');
  const nav = document.querySelector('.nav');
  if (!toggle || !nav) return;
  toggle.addEventListener('click', () => {
    const open = nav.classList.toggle('is-open');
    toggle.classList.toggle('is-open', open);
    toggle.setAttribute('aria-expanded', String(open));
  });
  nav.querySelectorAll('a').forEach(a => a.addEventListener('click', () => {
    nav.classList.remove('is-open');
    toggle.classList.remove('is-open');
  }));
})();

/* ---------- header background on scroll ---------- */
(function () {
  const header = document.querySelector('.site-header');
  if (!header) return;
  const onScroll = () => header.style.boxShadow = window.scrollY > 8 ? '0 8px 24px rgba(0,0,0,0.25)' : 'none';
  document.addEventListener('scroll', onScroll, { passive: true });
  onScroll();
})();

/* ---------- scroll reveal ---------- */
(function () {
  const targets = document.querySelectorAll('.reveal, .masonry-item');
  if (!targets.length) return;
  const io = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('is-visible');
        io.unobserve(entry.target);
      }
    });
  }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });
  targets.forEach(t => io.observe(t));
})();

/* ---------- generic drag-to-scroll + autoscroll gallery ---------- */
(function () {
  document.querySelectorAll('[data-gallery-scroller]').forEach((outer) => {
    const track = outer.querySelector('.gallery-track');
    if (!track) return;
    const section = outer.closest('.gallery-scroller') || outer.parentElement;
    const prevBtn = section ? section.querySelector('[data-gs-prev]') : null;
    const nextBtn = section ? section.querySelector('[data-gs-next]') : null;
    const playBtn = section ? section.querySelector('[data-gs-play]') : null;

    let isDown = false, startX = 0, startScroll = 0, autoTimer = null, playing = true;

    const step = () => Math.min(420, outer.clientWidth * 0.8);

    function autoScroll() {
      if (!playing) return;
      const max = outer.scrollWidth - outer.clientWidth;
      if (max <= 0) return;
      if (outer.scrollLeft >= max - 2) {
        outer.scrollTo({ left: 0, behavior: 'smooth' });
      } else {
        outer.scrollBy({ left: step() * 0.55, behavior: 'smooth' });
      }
    }
    function startAuto() {
      stopAuto();
      autoTimer = setInterval(autoScroll, 3200);
    }
    function stopAuto() { if (autoTimer) clearInterval(autoTimer); }

    outer.addEventListener('pointerdown', (e) => {
      isDown = true;
      outer.classList.add('is-dragging');
      startX = e.clientX;
      startScroll = outer.scrollLeft;
      stopAuto();
    });
    window.addEventListener('pointerup', () => {
      if (!isDown) return;
      isDown = false;
      outer.classList.remove('is-dragging');
      if (playing) startAuto();
    });
    window.addEventListener('pointermove', (e) => {
      if (!isDown) return;
      outer.scrollLeft = startScroll - (e.clientX - startX);
    });
    outer.addEventListener('wheel', () => stopAuto(), { passive: true });
    outer.addEventListener('mouseenter', stopAuto);
    outer.addEventListener('mouseleave', () => { if (playing) startAuto(); });

    if (prevBtn) prevBtn.addEventListener('click', () => { stopAuto(); outer.scrollBy({ left: -step(), behavior: 'smooth' }); if (playing) startAuto(); });
    if (nextBtn) nextBtn.addEventListener('click', () => { stopAuto(); outer.scrollBy({ left: step(), behavior: 'smooth' }); if (playing) startAuto(); });
    if (playBtn) {
      playBtn.setAttribute('data-playing', 'true');
      playBtn.addEventListener('click', () => {
        playing = !playing;
        playBtn.setAttribute('data-playing', String(playing));
        playing ? startAuto() : stopAuto();
      });
    }

    startAuto();
  });
})();

/* ---------- lightbox (used by project galleries + masonry + posters) ---------- */
(function () {
  const lightbox = document.querySelector('[data-lightbox]');
  if (!lightbox) return;
  const stage = lightbox.querySelector('.lightbox__stage');
  const caption = lightbox.querySelector('.lightbox__caption');
  const closeBtn = lightbox.querySelector('.lightbox__close');
  const prevBtn = lightbox.querySelector('.lightbox__nav--prev');
  const nextBtn = lightbox.querySelector('.lightbox__nav--next');

  let group = [];
  let index = 0;

  function render() {
    const item = group[index];
    if (!item) return;
    stage.innerHTML = '';
    let el;
    if (item.type === 'video') {
      el = document.createElement('video');
      el.src = item.src;
      el.controls = true;
      el.autoplay = true;
      el.playsInline = true;
    } else {
      el = document.createElement('img');
      el.src = item.src;
      el.alt = item.caption || '';
    }
    stage.appendChild(el);
    caption.textContent = item.caption || '';
  }

  function open(items, startIndex) {
    group = items;
    index = startIndex;
    lightbox.classList.add('is-open');
    document.body.style.overflow = 'hidden';
    render();
  }
  function close() {
    lightbox.classList.remove('is-open');
    document.body.style.overflow = '';
    stage.innerHTML = '';
  }
  function nav(delta) {
    if (!group.length) return;
    index = (index + delta + group.length) % group.length;
    render();
  }

  closeBtn.addEventListener('click', close);
  lightbox.addEventListener('click', (e) => { if (e.target === lightbox) close(); });
  prevBtn.addEventListener('click', () => nav(-1));
  nextBtn.addEventListener('click', () => nav(1));
  document.addEventListener('keydown', (e) => {
    if (!lightbox.classList.contains('is-open')) return;
    if (e.key === 'Escape') close();
    if (e.key === 'ArrowLeft') nav(-1);
    if (e.key === 'ArrowRight') nav(1);
  });

  // wire up any [data-expand] trigger within a common gallery group
  document.querySelectorAll('[data-gallery-group]').forEach((groupEl) => {
    const items = Array.from(groupEl.querySelectorAll('[data-lightbox-src]'));
    const parsed = items.map(el => ({
      src: el.getAttribute('data-lightbox-src'),
      type: el.getAttribute('data-lightbox-type') || 'image',
      caption: el.getAttribute('data-lightbox-caption') || ''
    }));
    items.forEach((el, i) => {
      el.addEventListener('click', (e) => {
        e.preventDefault();
        open(parsed, i);
      });
    });
  });
})();

/* ---------- masonry gallery filters ---------- */
(function () {
  const filterWrap = document.querySelector('[data-masonry-filters]');
  const grid = document.querySelector('[data-masonry-grid]');
  if (!filterWrap || !grid) return;
  const buttons = filterWrap.querySelectorAll('button');
  const items = grid.querySelectorAll('.masonry-item');

  buttons.forEach(btn => {
    btn.addEventListener('click', () => {
      buttons.forEach(b => b.classList.remove('is-active'));
      btn.classList.add('is-active');
      const filter = btn.getAttribute('data-filter');
      items.forEach(item => {
        const match = filter === 'all' || item.getAttribute('data-project') === filter;
        item.style.display = match ? '' : 'none';
      });
    });
  });
})();

/* ---------- posters rail: pause on hover/tap, duplicate handled in HTML ---------- */
(function () {
  document.querySelectorAll('.posters-rail-outer').forEach(outer => {
    outer.addEventListener('click', () => outer.classList.toggle('is-paused'));
  });
})();

/* ---------- contact form ---------- */
(function () {
  const form = document.querySelector('[data-contact-form]');
  if (!form) return;
  const status = form.querySelector('.form-status');
  const submitBtn = form.querySelector('.contact-form__submit');

  /*
    Drop-in email handling:
    Replace ENDPOINT below with your Formspree / Getform / Basin endpoint
    (create a free form at https://formspree.io, e.g. https://formspree.io/f/xxxxxxx)
    to have submissions land straight in your inbox with zero backend code.
    Until then, the form gracefully falls back to opening the user's email client.
  */
  const ENDPOINT = ''; // e.g. 'https://formspree.io/f/yourFormId'
  const FALLBACK_EMAIL = 'liam@stearndesigns.com';

  form.addEventListener('submit', async (e) => {
    e.preventDefault();
    const data = new FormData(form);
    const name = data.get('name');
    const email = data.get('email');
    const project = data.get('project');
    const message = data.get('message');

    if (!name || !email || !message) {
      status.dataset.state = 'error';
      status.textContent = 'Please fill in your name, email and message.';
      return;
    }

    submitBtn.disabled = true;
    status.dataset.state = '';
    status.textContent = 'Sending…';

    if (ENDPOINT) {
      try {
        const res = await fetch(ENDPOINT, {
          method: 'POST',
          headers: { 'Accept': 'application/json' },
          body: data
        });
        if (res.ok) {
          status.dataset.state = 'success';
          status.textContent = 'Thanks — your message is in. I\u2019ll reply within a couple of days.';
          form.reset();
        } else {
          throw new Error('Request failed');
        }
      } catch (err) {
        status.dataset.state = 'error';
        status.textContent = 'Something went wrong sending that — please email hello@stearndesigns.co.uk directly.';
      } finally {
        submitBtn.disabled = false;
      }
      return;
    }

    // fallback: open mail client pre-filled
    const subject = encodeURIComponent(`New project enquiry — ${project || 'General'}`);
    const body = encodeURIComponent(`${message}\n\n— ${name} (${email})`);
    window.location.href = `mailto:${FALLBACK_EMAIL}?subject=${subject}&body=${body}`;
    status.dataset.state = 'success';
    status.textContent = 'Opening your email client…';
    submitBtn.disabled = false;
  });
})();
