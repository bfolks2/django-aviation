import Component from '@ember/component';

export default Component.extend({

  /**
   * The post bound to this component.
   *
   * @argument post
   * @type object
   * @default null
   */
  post: null,

  /**
   * Variables for setting initial button states
   */
  isTextDisabled: null,
  isButtonDisabled: null,
  showAddComment: null,
  showSaveCancel: null,

  init() {
    this._super(...arguments);
    this.set('isTextDisabled', true);
    this.set('showAddComment', true);
    this.set('showSaveCancel', false);
  },

  actions: {
    edit() {
      this.set('isTextDisabled', false);
      this.set('showAddComment', false);
      this.set('showSaveCancel', true);
      this.disableAllButtons(true);
    },

    cancel() {
      this.set('isTextDisabled', true);
      this.set('showAddComment', true);
      this.set('showSaveCancel', false);
      this.disableAllButtons(false);
    }
  },

  disableAllButtons: function(bool) {
    this.get('disableAllButtons')(bool);
  }


});
