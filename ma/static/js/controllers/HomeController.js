/* eslint-env browser, jquery */

import ScrollReveal from 'scrollreveal/dist/scrollreveal';
import jQueryEasing from 'jquery.easing/jquery.easing.min'; // eslint-disable-line no-unused-vars


export default {
  init() {
    // Hide collapse menu on mobile when a menu item is clicked
    const navMain = $('.navbar-collapse');
    navMain.on('click', 'a:not([data-toggle])', null, () => {
      navMain.collapse('hide');
    });

    // Collapse the navbar on scroll
    $(window).scroll(() => {
      if ($('.navbar').offset().top > 50) {
        $('.fixed-top').addClass('top-nav-collapse');
      } else {
        $('.fixed-top').removeClass('top-nav-collapse');
      }
    });

    // jQuery for page scrolling feature - requires jQuery Easing plugin
    $(() => {
      function updateNavbarBorder(anchorId, timeout) {
        window.setTimeout(() => {
          $('.navbar-morganaubert.top-nav-collapse')
            .removeClass((index, css) => (css.match(/\banchor\S+/g) || []).join(' '));
          const anchorIdPart = anchorId.substring(1);
          $('.navbar-morganaubert.top-nav-collapse').addClass(`anchor-${anchorIdPart}`);
        }, timeout);
      }

      $('a.goto').click((ev) => {
        const anchorId = $(ev.currentTarget).attr('href');

        updateNavbarBorder(anchorId, 1000);

        $('html, body').stop().animate({
          scrollTop: $(anchorId).offset().top,
        }, 1500, 'easeInOutExpo');

        ev.preventDefault();
      });

      $('[data-spy="scroll"]').each(function refreshScrollSpy() {
        $(this).scrollspy('refresh');
      });
      $(window).on('activate.bs.scrollspy', () => {
        const anchorId = $('.navbar-nav li > a.active').attr('href');
        updateNavbarBorder(anchorId, 200);
      });

      window.sr = new ScrollReveal();
      // eslint-disable-next-line no-undef
      sr.reveal('.avatar-wrapper');
      // eslint-disable-next-line no-undef
      sr.reveal(
        '.interest-icon-wrapper',
        {
          origin: 'left', rotate: { z: 15 }, distance: '20px', delay: 50,
        },
      );
    });
  },
};
