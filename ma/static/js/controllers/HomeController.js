/* eslint-env browser, jquery */

import ScrollReveal from 'scrollreveal/dist/scrollreveal';
import jQueryEasing from 'jquery.easing/js/jquery.easing.min'; // eslint-disable-line no-unused-vars


export default {
  init() {
    // Collapse the navbar on scroll
    $(window).scroll(() => {
      if ($('.navbar').offset().top > 50) {
        $('.navbar-fixed-top').addClass('top-nav-collapse');
      } else {
        $('.navbar-fixed-top').removeClass('top-nav-collapse');
      }
    });

    // jQuery for page scrolling feature - requires jQuery Easing plugin
    $(() => {
      function updateNavbarBorder(anchorId, timeout) {
        window.setTimeout(
          () => {
            $('.navbar-morganaubert.top-nav-collapse').removeClass(
                (index, css) => (css.match(/\banchor\S+/g) || []).join(' '));
            const anchorIdPart = anchorId.substring(1);
            $('.navbar-morganaubert.top-nav-collapse').addClass(`anchor-${anchorIdPart}`);
          },
          timeout);
      }

      $('a.goto').click((ev) => {
        const anchorId = $(ev.currentTarget).attr('href');

        updateNavbarBorder(anchorId, 1000);

        $('html, body').stop().animate({
          scrollTop: $(anchorId).offset().top,
        }, 1500, 'easeInOutExpo');

        ev.preventDefault();
      });

      $('.navbar-nav').on('activate.bs.scrollspy', () => {
        const anchorId = $('.navbar-nav li.active > a').attr('href');
        updateNavbarBorder(anchorId, 200);
      });

      window.sr = new ScrollReveal();
      // eslint-disable-next-line no-undef
      sr.reveal('.avatar-wrapper');
      // eslint-disable-next-line no-undef
      sr.reveal(
          '.interest-icon-wrapper',
          { origin: 'left', rotate: { z: 15 }, distance: '20px', delay: 50 });
    });
  },
};
