/**
 * Meowtown Cattery — shared JavaScript
 * Mobile menu, FAQ accordion, scroll animations, footer year
 */
(function () {
    'use strict';

    // Footer year
    var yearEl = document.getElementById('year');
    if (yearEl) {
        yearEl.textContent = new Date().getFullYear();
    }

    // Mobile menu toggle
    var menuToggle = document.querySelector('.menu-toggle');
    var navOverlay = document.querySelector('.nav-overlay');
    if (menuToggle && navOverlay) {
        menuToggle.addEventListener('click', function () {
            var isOpen = navOverlay.classList.toggle('is-open');
            menuToggle.setAttribute('aria-expanded', isOpen);
            document.body.style.overflow = isOpen ? 'hidden' : '';
        });

        // Close on nav link click (mobile)
        navOverlay.querySelectorAll('a').forEach(function (link) {
            link.addEventListener('click', function () {
                navOverlay.classList.remove('is-open');
                menuToggle.setAttribute('aria-expanded', 'false');
                document.body.style.overflow = '';
            });
        });

        // Close on escape
        document.addEventListener('keydown', function (e) {
            if (e.key === 'Escape' && navOverlay.classList.contains('is-open')) {
                navOverlay.classList.remove('is-open');
                menuToggle.setAttribute('aria-expanded', 'false');
                document.body.style.overflow = '';
            }
        });
    }

    // FAQ accordion — one open at a time
    var faqList = document.querySelector('.faq-list');
    if (faqList) {
        var items = faqList.querySelectorAll('.faq-item');
        function setAria(item, open) {
            var btn = item.querySelector('.faq-question');
            if (btn) btn.setAttribute('aria-expanded', open);
        }
        items.forEach(function (item) {
            var btn = item.querySelector('.faq-question');
            if (!btn) return;
            btn.addEventListener('click', function () {
                var wasOpen = item.classList.contains('is-open');
                items.forEach(function (other) {
                    other.classList.remove('is-open');
                    setAria(other, false);
                });
                if (!wasOpen) {
                    item.classList.add('is-open');
                    setAria(item, true);
                }
            });
        });
        if (items.length) {
            items[0].classList.add('is-open');
            setAria(items[0], true);
        }
    }

    // Scroll animations — Intersection Observer
    var animated = document.querySelectorAll('.animate-on-scroll');
    if (animated.length && 'IntersectionObserver' in window) {
        var observer = new IntersectionObserver(
            function (entries) {
                entries.forEach(function (entry) {
                    if (entry.isIntersecting) {
                        entry.target.classList.add('is-visible');
                    }
                });
            },
            { rootMargin: '0px 0px -40px 0px', threshold: 0.01 }
        );
        animated.forEach(function (el) {
            observer.observe(el);
        });
    }

})();
