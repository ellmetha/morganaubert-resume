const controllers = {
  home: () => import('./HomeController').then(module => module.default),
};

export default controllers;
