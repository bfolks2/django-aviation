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
    this.setProperties({
      isTextDisabled: true,
      showAddComment: true,
      showSaveCancel: false,
    });
  },

  actions: {
    edit() {
      this.setProperties({
        isTextDisabled: false,
        showAddComment: false,
        showSaveCancel: true,
      });
      this.disableAllButtons(true);
    },

    cancel() {
      this.setProperties({
        isTextDisabled: true,
        showAddComment: true,
        showSaveCancel: false,
      });
      this.disableAllButtons(false);
      this.get('post').rollbackAttributes();
    },

    save() {
      this.setProperties({
        isTextDisabled: true,
        showAddComment: true,
        showSaveCancel: false,
      });
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
