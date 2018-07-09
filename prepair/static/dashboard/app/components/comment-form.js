import Component from '@ember/component';

export default Component.extend({

  /**
   * The comment bound to this component.
   *
   * @argument comment
   * @type object
   * @default null
   */
  comment: null,

  /**
   * Variables for setting initial button states
   */
  isTextDisabled: null,
  isButtonDisabled: null,
  showSaveCancel: null,

  init() {
    this._super(...arguments);
    this.set('isTextDisabled', true);
    this.set('showSaveCancel', false);
  },

  actions: {
    edit() {
      this.set('isTextDisabled', false);
      this.set('showSaveCancel', true);
      this.disableAllButtons(true);
    },
    cancel() {
      this.set('isTextDisabled', true);
      this.set('showSaveCancel', false);
      this.disableAllButtons(false);
    },

    save() {
      this.set('isTextDisabled', true);
      this.set('showAddComment', true);
      this.set('showSaveCancel', false);
      this.disableAllButtons(false);
      //INSERT LOGIC TO SAVE NEW POST
    },

    delete() {
      this.disableAllButtons(false);
      //INSERT LOGIC TO DELETE POST
    }
  },

  disableAllButtons: function(bool) {
    this.get('disableAllButtons')(bool);
  }


});
