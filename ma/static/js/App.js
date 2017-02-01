import 'babel-polyfill';

// Forces the evaluation of jQuery and Twitter Bootstrap code in the global context
import '!!script!jquery/dist/jquery.min';
import '!!script!bootstrap/dist/js/bootstrap.min';

import controllers from './controllers';
import DOMRouter from './core/DOMRouter';


// Defines the router and initializes it!
let router = new DOMRouter(controllers);
$(document).ready(function(ev) { router.init(); });
