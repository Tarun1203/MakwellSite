// assets/js/script.js
// ============================================================================
// Makwell Site – Interaction Layer (Extended)
// - Mobile nav toggle (ARIA-friendly)
// - Close nav on link click / outside click
// - Sticky header shadow on scroll
// - Smooth scroll to in-page anchors with header offset
// - Tabs, Accordion, Modal, Toast helpers
// - Optional: simple fade slider if .slide elements exist
// ============================================================================

(function () {
  const qs = (sel, root = document) => root.querySelector(sel);
  const qsa = (sel, root = document) => Array.from(root.querySelectorAll(sel));

  // ---------- Mobile Nav Toggle ----------
  const header = qs('.site-header');
  const nav = qs('.primary-nav');
  const btn = qs('.nav-toggle');
  const list = qs('.nav-list');

  function setOpen(open) {
    if (!nav || !btn || !list) return;
    nav.setAttribute('aria-expanded', String(open));
    btn.setAttribute('aria-expanded', String(open));
    list.style.display = open ? 'flex' : '';
  }

  if (nav && btn && list) {
    btn.addEventListener('click', (e) => {
      e.stopPropagation();
      const open = nav.getAttribute('aria-expanded') === 'true';
      setOpen(!open);
    });

    list.addEventListener('click', (e) => {
      const a = e.target.closest('a');
      if (a) setOpen(false);
    });

    document.addEventListener('click', (e) => {
      if (!nav.contains(e.target) && nav.getAttribute('aria-expanded') === 'true') {
        setOpen(false);
      }
    });

    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && nav.getAttribute('aria-expanded') === 'true') {
        setOpen(false);
      }
    });
  }

  // ---------- Sticky Header Shadow ----------
  const onScroll = () => {
    if (!header) return;
    if (window.scrollY > 10) header.classList.add('is-scrolled');
    else header.classList.remove('is-scrolled');
  };
  onScroll();
  window.addEventListener('scroll', onScroll, { passive: true });

  // ---------- Smooth Anchor Scroll ----------
  const headerHeight = () => (header ? header.offsetHeight : 0);
  qsa('a[href^="#"]').forEach((link) => {
    link.addEventListener('click', (e) => {
      const id = link.getAttribute('href');
      if (!id || id === '#') return;
      const target = qs(id);
      if (!target) return;
      e.preventDefault();
      const y = target.getBoundingClientRect().top + window.scrollY - (headerHeight() + 8);
      window.scrollTo({ top: y, behavior: 'smooth' });
      history.pushState(null, '', id);
    });
  });

  // ---------- Tabs ----------
  qsa('.tabs').forEach((tabs) => {
    const buttons = qsa('.tab-btn', tabs);
    const panels = qsa('.tab-panel', tabs);
    function select(i) {
      buttons.forEach((b, idx) => b.setAttribute('aria-selected', String(idx === i)));
      panels.forEach((p, idx) => p.setAttribute('aria-hidden', String(idx !== i)));
    }
    buttons.forEach((b, i) => b.addEventListener('click', () => select(i)));
    select(0);
  });

  // ---------- Accordion ----------
  qsa('.accordion .accordion-item').forEach((item) => {
    const headerEl = qs('.accordion-header', item);
    if (!headerEl) return;
    headerEl.addEventListener('click', () => {
      const expanded = item.getAttribute('aria-expanded') === 'true';
      item.setAttribute('aria-expanded', String(!expanded));
    });
  });

  // ---------- Modal ----------
  function openModal(id) {
    const modal = qs(id);
    const backdrop = qs(`${id}-backdrop`) || qs('.modal-backdrop');
    if (!modal) return;
    modal.setAttribute('aria-hidden', 'false');
    if (backdrop) backdrop.setAttribute('aria-hidden', 'false');
  }
  function closeModal(id) {
    const modal = qs(id);
    const backdrop = qs(`${id}-backdrop`) || qs('.modal-backdrop');
    if (!modal) return;
    modal.setAttribute('aria-hidden', 'true');
    if (backdrop) backdrop.setAttribute('aria-hidden', 'true');
  }
  window.MakwellModal = { open: openModal, close: closeModal };

  qsa('[data-modal-open]').forEach((btn) => {
    btn.addEventListener('click', () => openModal(btn.getAttribute('data-modal-open')));
  });
  qsa('[data-modal-close]').forEach((btn) => {
    btn.addEventListener('click', () => closeModal(btn.getAttribute('data-modal-close')));
  });

  // Close modal on ESC
  document.addEventListener('keydown', (e) => {
    if (e.key !== 'Escape') return;
    qsa('.modal').forEach((m) => m.setAttribute('aria-hidden', 'true'));
    qsa('.modal-backdrop').forEach((b) => b.setAttribute('aria-hidden', 'true'));
  });

  // ---------- Toast ----------
  function toast(message, type = '') {
    const wrap = qs('.toast-wrap') || (() => {
      const w = document.createElement('div');
      w.className = 'toast-wrap';
      document.body.appendChild(w);
      return w;
    })();
    const el = document.createElement('div');
    el.className = `toast ${type}`.trim();
    el.textContent = message;
    wrap.appendChild(el);
    setTimeout(() => el.remove(), 3500);
  }
  window.toast = toast;

  // ---------- Optional Fade Slider ----------
  const slider = qs('.slider') || qs('.hero');
  if (slider) {
    const slides = qsa('.slide', slider);
    let idx = 0;
    if (slides.length > 1) {
      slides.forEach((s, i) => {
        s.style.position = 'absolute';
        s.style.inset = '0';
        s.style.opacity = i === 0 ? '1' : '0';
        s.style.transition = 'opacity 800ms ease';
      });
      slider.style.position = 'relative';
      setInterval(() => {
        const prev = idx;
        idx = (idx + 1) % slides.length;
        slides[prev].style.opacity = '0';
        slides[idx].style.opacity = '1';
      }, 6000);
    }
  }

  // ---------- Utility: data-scroll-to ----------
  qsa('[data-scroll-to]').forEach((el) => {
    el.addEventListener('click', () => {
      const id = el.getAttribute('data-scroll-to');
      const target = id ? qs(id) : null;
      if (!target) return;
      const y = target.getBoundingClientRect().top + window.scrollY - (headerHeight() + 8);
      window.scrollTo({ top: y, behavior: 'smooth' });
    });
  });
})();
