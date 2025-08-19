document.addEventListener('DOMContentLoaded', function () {
  console.log('MAKWELL: Auto-fit image system loading...');

  // Mobile Menu Toggle
  const hamburger = document.querySelector('.hamburger');
  const navMenu = document.querySelector('.nav-menu');

  if (hamburger && navMenu) {
    hamburger.addEventListener('click', function () {
      hamburger.classList.toggle('active');
      navMenu.classList.toggle('active');
    });

    document.querySelectorAll('.nav-link').forEach((link) => {
      link.addEventListener('click', function () {
        hamburger.classList.remove('active');
        navMenu.classList.remove('active');
      });
    });

    document.addEventListener('click', function (e) {
      if (!hamburger.contains(e.target) && !navMenu.contains(e.target)) {
        hamburger.classList.remove('active');
        navMenu.classList.remove('active');
      }
    });
  }

  // Auto-fit images system
  function initAutoFitImages() {
    const imageContainers = document.querySelectorAll(
      '.product-image, .category-card-image, .banner-image, .showcase-image, .product-image-large'
    );

    imageContainers.forEach((container) => {
      const img = container.querySelector('img');
      const icon = container.querySelector('i');

      if (img) {
        container.classList.add('image-loading');

        img.onload = function () {
          container.classList.remove('image-loading');
          container.classList.remove('fallback');
          if (icon) icon.style.display = 'none';
        };

        img.onerror = function () {
          container.classList.remove('image-loading');
          container.classList.add('fallback');
          img.style.display = 'none';
          if (icon) icon.style.display = 'block';
        };

        if (img.complete && img.naturalHeight !== 0) {
          container.classList.remove('image-loading');
          if (icon) icon.style.display = 'none';
        }
      }
    });
  }

  // Navigation color locking
  function lockNavigationColors() {
    const navbar = document.querySelector('.navbar');
    if (navbar) {
      navbar.style.setProperty('background', 'var(--color-nav-bg)', 'important');

      const navLinks = document.querySelectorAll('.nav-link');
      navLinks.forEach((link) => {
        link.style.setProperty('color', 'var(--color-nav-text)', 'important');
      });

      const logoText = document.querySelectorAll('.nav-logo h2, .nav-logo-text h2');
      logoText.forEach((text) => {
        text.style.setProperty('color', 'var(--color-nav-text)', 'important');
      });
    }
  }

  // Initialize systems
  initAutoFitImages();
  lockNavigationColors();

  // Scroll handler (only shadow changes, no color changes)
  window.addEventListener('scroll', function () {
    const navbar = document.querySelector('.navbar');
    const currentScrollY = window.scrollY;

    if (navbar) {
      if (currentScrollY > 50) {
        navbar.style.setProperty('box-shadow', '0 4px 20px rgba(65, 105, 225, 0.2)', 'important');
      } else {
        navbar.style.setProperty('box-shadow', '0 4px 20px rgba(65, 105, 225, 0.1)', 'important');
      }
      lockNavigationColors();
    }
  });
});
