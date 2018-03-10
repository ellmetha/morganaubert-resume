/* eslint-env browser */
import 'babel-polyfill';

// Forces the evaluation of bootstrap plugins in the global context.
import 'bootstrap.native/dist/bootstrap-native-v4';

import controllers from './controllers';
import DOMRouter from './core/DOMRouter';


// Defines the router and initializes it!
const router = new DOMRouter(controllers);
(function runApp() {
  router.init();
}(window));
