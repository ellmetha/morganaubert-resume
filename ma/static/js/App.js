/* eslint-env browser, jquery */
import 'babel-polyfill';

// Forces the evaluation of jQuery in the global context
import 'bootstrap';

import controllers from './controllers';
import DOMRouter from './core/DOMRouter';


// Defines the router and initializes it!
const router = new DOMRouter(controllers);
$(document).ready(() => { router.init(); });
