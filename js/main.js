// Hovedscript for STNG Studios — jQuery-baseret interaktivitet. Lavet med AI, kig i documentation/samtaler/session-004_2026-02-07.md

$(document).ready(function () {

  // ============================================
  // STICKY NAVBAR — transparent til solid ved scroll
  // Lavet med AI, kig i documentation/samtaler/session-004_2026-02-07.md
  // ============================================
  var $header = $('.site-header');
  var heroHeight = $('.hero').outerHeight() || 300;

  $(window).on('scroll', function () {
    if ($(window).scrollTop() > 50) {
      $header.addClass('scrolled');
    } else {
      $header.removeClass('scrolled');
    }
  });

  // ============================================
  // HAMBURGER-MENU — åbn/luk mobilmenu
  // Lavet med AI, kig i documentation/samtaler/session-004_2026-02-07.md
  // ============================================
  var $hamburger = $('.hamburger');
  var $navMenu = $('.nav-menu');
  var $navOverlay = $('.nav-overlay');

  $hamburger.on('click', function () {
    var isActive = $navMenu.hasClass('active');

    $hamburger.toggleClass('active');
    $navMenu.toggleClass('active');
    $navOverlay.toggleClass('active');

    // Opdatér aria-expanded for tilgængelighed
    $hamburger.attr('aria-expanded', !isActive);

    // Forhindre scroll på body når menuen er åben
    $('body').css('overflow', isActive ? '' : 'hidden');
  });

  // Luk menu når overlay klikkes
  $navOverlay.on('click', function () {
    $hamburger.removeClass('active');
    $navMenu.removeClass('active');
    $navOverlay.removeClass('active');
    $hamburger.attr('aria-expanded', 'false');
    $('body').css('overflow', '');
  });

  // Luk menu når et link klikkes
  $navMenu.find('a').on('click', function () {
    $hamburger.removeClass('active');
    $navMenu.removeClass('active');
    $navOverlay.removeClass('active');
    $hamburger.attr('aria-expanded', 'false');
    $('body').css('overflow', '');
  });

  // ============================================
  // BILLEDKARRUSEL — auto-rotation + manuel navigation
  // Lavet med AI, kig i documentation/samtaler/session-004_2026-02-07.md
  // ============================================
  var currentSlide = 0;
  var totalSlides = $('.carousel-slide').length;
  var autoPlayInterval = null;
  var autoPlayDelay = 4000;

  function goToSlide(index) {
    if (index < 0) index = totalSlides - 1;
    if (index >= totalSlides) index = 0;

    currentSlide = index;

    // Flyt alle slides med transform
    $('.carousel-slide').css('transform', 'translateX(-' + (currentSlide * 100) + '%)');

    // Opdatér aktiv dot
    $('.carousel-dot').removeClass('active');
    $('.carousel-dot[data-slide="' + currentSlide + '"]').addClass('active');
  }

  function nextSlide() {
    goToSlide(currentSlide + 1);
  }

  function startAutoPlay() {
    if (autoPlayInterval) clearInterval(autoPlayInterval);
    autoPlayInterval = setInterval(nextSlide, autoPlayDelay);
  }

  function stopAutoPlay() {
    if (autoPlayInterval) {
      clearInterval(autoPlayInterval);
      autoPlayInterval = null;
    }
  }

  // Klik på dots
  $('.carousel-dot').on('click', function () {
    var slideIndex = parseInt($(this).data('slide'));
    goToSlide(slideIndex);
    stopAutoPlay();
    startAutoPlay();
  });

  // Pause ved hover (kun desktop)
  $('.carousel-container').on('mouseenter', function () {
    stopAutoPlay();
  });

  $('.carousel-container').on('mouseleave', function () {
    startAutoPlay();
  });

  // Touch/swipe support til mobil
  var touchStartX = 0;
  var touchEndX = 0;

  $('.carousel-track').on('touchstart', function (e) {
    touchStartX = e.originalEvent.touches[0].clientX;
  });

  $('.carousel-track').on('touchend', function (e) {
    touchEndX = e.originalEvent.changedTouches[0].clientX;
    var diff = touchStartX - touchEndX;

    if (Math.abs(diff) > 50) {
      if (diff > 0) {
        goToSlide(currentSlide + 1);
      } else {
        goToSlide(currentSlide - 1);
      }
      stopAutoPlay();
      startAutoPlay();
    }
  });

  // Start karrusel
  startAutoPlay();

  // ============================================
  // SCROLL-ANIMATIONER — elementer glider ind fra siderne (kun desktop)
  // Lavet med AI, kig i documentation/samtaler/session-004_2026-02-07.md
  // ============================================
  if (window.matchMedia('(min-width: 1024px)').matches) {
    var observerOptions = {
      root: null,
      rootMargin: '0px',
      threshold: 0.2
    };

    // Genafspilelig scroll-animation: .visible tilføjes/fjernes ved scroll. Lavet med AI, kig i documentation/samtaler/session-004_2026-02-07.md
    var observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          $(entry.target).addClass('visible');
        } else {
          $(entry.target).removeClass('visible');
        }
      });
    }, observerOptions);

    // Observér elementer med slide-in klasser
    $('.slide-in-left, .slide-in-right').each(function () {
      observer.observe(this);
    });
  }

});
