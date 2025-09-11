// script.js — dynamic CTA: entrance + ripple + video fallback
document.addEventListener('DOMContentLoaded', function () {
  initCTAAnimations();
  initRippleEffect();
  initVideoFallback();
});

/* Animate CTAs when hero content is in view */
function initCTAAnimations() {
  const heroContent = document.getElementById('heroContent');
  if (!heroContent) return;

  const btns = Array.from(heroContent.querySelectorAll('.btn'));
  btns.forEach((b, i) => {
    // stagger delays
    b.style.setProperty('--delay', `${i * 90}ms`);
  });

  const obs = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        heroContent.classList.add('in');
        obs.disconnect();
      }
    });
  }, { threshold: 0.25 });

  obs.observe(heroContent);
}

/* Ripple effect on .btn elements */
function initRippleEffect() {
  const buttons = Array.from(document.querySelectorAll('.btn'));

  buttons.forEach(btn => {
    // ensure relative positioning (CSS already sets it)
    btn.addEventListener('pointerdown', createRipple);
    // ensure keyboard activation also shows ripple
    btn.addEventListener('keydown', function (e) {
      if (e.key === 'Enter' || e.key === ' ') createRipple(e);
    });
  });

  function createRipple(e) {
    // allow anchor hrefs to still navigate — ripple is visual only
    const el = e.currentTarget;
    const rect = el.getBoundingClientRect();

    // compute coordinates relative to element
    let x = (e.clientX || rect.left + rect.width / 2) - rect.left;
    let y = (e.clientY || rect.top + rect.height / 2) - rect.top;

    const ripple = document.createElement('span');
    ripple.className = 'ripple';
    // size should cover the element
    const size = Math.max(rect.width, rect.height) * 1.2;
    ripple.style.width = ripple.style.height = size + 'px';
    ripple.style.left = (x - size / 2) + 'px';
    ripple.style.top = (y - size / 2) + 'px';
    el.appendChild(ripple);

    // remove after animation
    ripple.addEventListener('animationend', () => {
      ripple.remove();
    });

    // For keyboard events, briefly show ripple
    if (e.type === 'keydown') {
      setTimeout(() => ripple.remove(), 400);
    }
  }
}

/* try to detect video load error and mark hero */
function initVideoFallback() {
  const vid = document.getElementById('heroVideo');
  const hero = document.getElementById('hero');

  if (!vid || !hero) return;

  // if the video fails to load, add .no-video so CSS can change visuals
  vid.addEventListener('error', () => {
    hero.classList.add('no-video');
  });

  // also if metadata loads but readyState is low, check if it can play
  vid.addEventListener('loadedmetadata', () => {
    // some browsers might block autoplay — we don't change behavior, but we can detect play permission
    // If the video is paused and should be playing, don't force play; just show poster
    setTimeout(() => {
      if (vid.paused && !hero.classList.contains('no-video')) {
        // leave it — poster will show; optionally add class
        // hero.classList.add('no-video'); // uncomment if you'd like to force fallback when autoplay blocked
      }
    }, 250);
  });
}


