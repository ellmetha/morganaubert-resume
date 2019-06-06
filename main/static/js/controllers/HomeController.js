/* eslint-env browser */

import bsn from 'bootstrap.native/dist/bootstrap-native-v4';
import ScrollReveal from 'scrollreveal/dist/scrollreveal';

import getElementOffset from '../core/getElementOffset';
import scrollTo from '../core/scrollTo';


export default {
  init() {
    const elNavbar = document.querySelector('.navbar');

    // Collapses the navbar on scroll.
    // --
    window.addEventListener('scroll', () => {
      if (getElementOffset(elNavbar).top > 50) {
        elNavbar.classList.add('top-nav-collapse');
      } else {
        elNavbar.classList.remove('top-nav-collapse');
      }
    });


    // Page scrolling feature initialization.
    // --

    function _updateNavbarBorder(anchorId, timeout) {
      window.setTimeout(() => {
        let clsToRemove = null;
        for (let i = 0; i < elNavbar.classList.length; i += 1) {
          if (elNavbar.classList[i].match(/\banchor\S+/g)) { clsToRemove = elNavbar.classList[i]; }
        }
        if (clsToRemove) { elNavbar.classList.remove(clsToRemove); }
        elNavbar.classList.add(`anchor-${anchorId}`);
      }, timeout);
    }

    const navLinks = document.body.querySelectorAll('a.goto');
    for (let i = 0; i < navLinks.length; i += 1) {
      navLinks[i].onclick = function scrollToSection(ev) {
        const anchorId = this.href.split('#')[1];
        const elTarget = document.getElementById(anchorId);
        _updateNavbarBorder(anchorId, 1000);
        ev.preventDefault();
        scrollTo(elTarget, 1500, 'easeInOutCubic');
      };
    }


    // ScrollReveal initialization.
    // --

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


    // ScrollSpy initialization.
    // --

    new bsn.ScrollSpy(document.body, { target: '.fixed-top' });
    document.body.addEventListener('activate.bs.scrollspy', () => {
      const anchorId = document.querySelector('.navbar-nav li > a.active').href.split('#')[1];
      _updateNavbarBorder(anchorId, 200);
    });
  },
};
