// DOM Content Loaded
document.addEventListener('DOMContentLoaded', function() {
    // Initialize all functionality
    initMobileMenu();
    initSlider();
    initScrollEffects();
    initProductCards();
});

// Mobile Menu Functionality
function initMobileMenu() {
    const navToggle = document.querySelector('.nav-toggle');
    const navMenu = document.querySelector('.nav-menu');

    if (navToggle && navMenu) {
        navToggle.addEventListener('click', function() {
            navMenu.classList.toggle('active');
            navToggle.classList.toggle('active');
        });

        // Close menu when clicking on a link
        const navLinks = document.querySelectorAll('.nav-menu a');
        navLinks.forEach(link => {
            link.addEventListener('click', function() {
                navMenu.classList.remove('active');
                navToggle.classList.remove('active');
            });
        });

        // Close menu when clicking outside
        document.addEventListener('click', function(event) {
            if (!navToggle.contains(event.target) && !navMenu.contains(event.target)) {
                navMenu.classList.remove('active');
                navToggle.classList.remove('active');
            }
        });
    }
}

// Slider Functionality
function initSlider() {
    const slides = document.querySelectorAll('.slide');
    const navDots = document.querySelectorAll('.nav-dot');
    const prevBtn = document.getElementById('prevBtn');
    const nextBtn = document.getElementById('nextBtn');

    let currentSlide = 0;
    const totalSlides = slides.length;
    let autoSlideInterval;

    // Function to show specific slide
    function showSlide(index) {
        // Remove active class from all slides and dots
        slides.forEach(slide => slide.classList.remove('active'));
        navDots.forEach(dot => dot.classList.remove('active'));

        // Add active class to current slide and dot
        if (slides[index]) {
            slides[index].classList.add('active');
        }
        if (navDots[index]) {
            navDots[index].classList.add('active');
        }

        currentSlide = index;
    }

    // Function to go to next slide
    function nextSlide() {
        const next = (currentSlide + 1) % totalSlides;
        showSlide(next);
    }

    // Function to go to previous slide
    function prevSlide() {
        const prev = (currentSlide - 1 + totalSlides) % totalSlides;
        showSlide(prev);
    }

    // Auto slide functionality
    function startAutoSlide() {
        autoSlideInterval = setInterval(nextSlide, 5000); // Change slide every 5 seconds
    }

    function stopAutoSlide() {
        clearInterval(autoSlideInterval);
    }

    // Event listeners for navigation buttons
    if (nextBtn) {
        nextBtn.addEventListener('click', function() {
            stopAutoSlide();
            nextSlide();
            startAutoSlide();
        });
    }

    if (prevBtn) {
        prevBtn.addEventListener('click', function() {
            stopAutoSlide();
            prevSlide();
            startAutoSlide();
        });
    }

    // Event listeners for navigation dots
    navDots.forEach((dot, index) => {
        dot.addEventListener('click', function() {
            stopAutoSlide();
            showSlide(index);
            startAutoSlide();
        });
    });

    // Keyboard navigation
    document.addEventListener('keydown', function(event) {
        if (event.key === 'ArrowLeft') {
            stopAutoSlide();
            prevSlide();
            startAutoSlide();
        } else if (event.key === 'ArrowRight') {
            stopAutoSlide();
            nextSlide();
            startAutoSlide();
        }
    });

    // Pause auto-slide on hover
    const sliderContainer = document.querySelector('.slider-container');
    if (sliderContainer) {
        sliderContainer.addEventListener('mouseenter', stopAutoSlide);
        sliderContainer.addEventListener('mouseleave', startAutoSlide);
    }

    // Touch/Swipe support for mobile
    let touchStartX = 0;
    let touchEndX = 0;

    if (sliderContainer) {
        sliderContainer.addEventListener('touchstart', function(event) {
            touchStartX = event.changedTouches[0].screenX;
        });

        sliderContainer.addEventListener('touchend', function(event) {
            touchEndX = event.changedTouches[0].screenX;
            handleSwipe();
        });
    }

    function handleSwipe() {
        const swipeThreshold = 50;
        const diff = touchStartX - touchEndX;

        if (Math.abs(diff) > swipeThreshold) {
            stopAutoSlide();
            if (diff > 0) {
                nextSlide(); // Swipe left - next slide
            } else {
                prevSlide(); // Swipe right - previous slide
            }
            startAutoSlide();
        }
    }

    // Start auto-slide
    startAutoSlide();

    // Initialize first slide
    showSlide(0);
}

// Scroll Effects
function initScrollEffects() {
    // Smooth scrolling for navigation links
    const navLinks = document.querySelectorAll('a[href^="#"]');

    navLinks.forEach(link => {
        link.addEventListener('click', function(event) {
            event.preventDefault();

            const targetId = this.getAttribute('href');
            const targetSection = document.querySelector(targetId);

            if (targetSection) {
                const headerHeight = document.querySelector('.header').offsetHeight;
                const targetPosition = targetSection.offsetTop - headerHeight;

                window.scrollTo({
                    top: targetPosition,
                    behavior: 'smooth'
                });
            }
        });
    });

    // Header background on scroll
    const header = document.querySelector('.header');
    if (header) {
        window.addEventListener('scroll', function() {
            if (window.scrollY > 100) {
                header.style.background = 'rgba(255, 255, 255, 0.98)';
                header.style.backdropFilter = 'blur(15px)';
            } else {
                header.style.background = 'rgba(255, 255, 255, 0.95)';
                header.style.backdropFilter = 'blur(10px)';
            }
        });
    }

    // Intersection Observer for animations
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, observerOptions);

    // Observe elements for scroll animations
    const animateElements = document.querySelectorAll('.product-card, .blog-header');
    animateElements.forEach(element => {
        element.style.opacity = '0';
        element.style.transform = 'translateY(30px)';
        element.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
        observer.observe(element);
    });
}

// Product Cards Functionality
function initProductCards() {
    const productButtons = document.querySelectorAll('.product-btn');

    productButtons.forEach(button => {
        button.addEventListener('click', function() {
            const productCard = this.closest('.product-card');
            const productTitle = productCard.querySelector('.product-title').textContent;

            // For now, just show an alert. In a real implementation, 
            // this would navigate to a product details page
            alert(`Learn more about ${productTitle}`);

            // Example of how you might track clicks for analytics
            if (typeof gtag !== 'undefined') {
                gtag('event', 'product_click', {
                    'product_name': productTitle,
                    'event_category': 'engagement'
                });
            }
        });
    });

    // Add hover effects programmatically
    const productCards = document.querySelectorAll('.product-card');
    productCards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-8px)';
            this.style.boxShadow = '0 12px 40px rgba(0, 0, 0, 0.2)';
        });

        card.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0)';
            this.style.boxShadow = '0 4px 20px rgba(0, 0, 0, 0.1)';
        });
    });
}

// Blog functionality
function initBlogSection() {
    const viewAllBtn = document.querySelector('.view-all-btn');

    if (viewAllBtn) {
        viewAllBtn.addEventListener('click', function() {
            // In a real implementation, this would navigate to the blog page
            window.location.href = '#blogs';
        });
    }
}

// Utility Functions
function debounce(func, wait, immediate) {
    let timeout;
    return function() {
        const context = this, args = arguments;
        const later = function() {
            timeout = null;
            if (!immediate) func.apply(context, args);
        };
        const callNow = immediate && !timeout;
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
        if (callNow) func.apply(context, args);
    };
}

// Performance optimization for scroll events
const debouncedScrollHandler = debounce(function() {
    // Any scroll-based functionality can go here
}, 10);

window.addEventListener('scroll', debouncedScrollHandler);

// Error handling
window.addEventListener('error', function(event) {
    console.error('JavaScript error:', event.error);
});

// Initialize blog section
document.addEventListener('DOMContentLoaded', function() {
    initBlogSection();
});

// Accessibility improvements
document.addEventListener('keydown', function(event) {
    // Add keyboard navigation for product cards
    if (event.key === 'Enter' || event.key === ' ') {
        const focusedElement = document.activeElement;
        if (focusedElement.classList.contains('product-btn')) {
            event.preventDefault();
            focusedElement.click();
        }
    }
});

// Preload images for better performance
function preloadImages() {
    const imageUrls = [
        'assets/images/logo.jpg'
        // Add other image URLs here
    ];

    imageUrls.forEach(url => {
        const img = new Image();
        img.src = url;
    });
}

// Call preload on page load
window.addEventListener('load', preloadImages);

// Service Worker registration (for PWA capabilities)
if ('serviceWorker' in navigator) {
    window.addEventListener('load', function() {
        navigator.serviceWorker.register('/service-worker.js')
            .then(function(registration) {
                console.log('SW registered: ', registration);
            })
            .catch(function(registrationError) {
                console.log('SW registration failed: ', registrationError);
            });
    });
}
