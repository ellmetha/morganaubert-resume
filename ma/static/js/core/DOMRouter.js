class DOMRouter {
  constructor(controllers) {
    this.controllers = (controllers === undefined) ? {} : controllers;
  }

  /**
   * Initializes the router object and executes the appropriate actions.
   */
  async init() {
    if (document.body) {
      const controllerCodename = document.body.getAttribute('data-controller');
      const action = document.body.getAttribute('data-action');
      if (controllerCodename && this.controllers[controllerCodename]) {
        const controller = await this.controllers[controllerCodename]();
        controller.init();
        if (controller[action] === 'function') { controller[action](); }
      }
    }
  }
}


export default DOMRouter;
