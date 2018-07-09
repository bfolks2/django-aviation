import Component from '@ember/component';
import TextArea from '@ember/component/text-area';

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
    this.setProperties({
      isTextDisabled: true,
      showSaveCancel: false,
    });
  },

  actions: {
    edit() {
      this.setProperties({
        isTextDisabled: false,
        showSaveCancel: true,
      });
      this.disableAllButtons(true);
    },
    cancel() {
      this.setProperties({
        isTextDisabled: true,
        showSaveCancel: false,
      });
      this.disableAllButtons(false);
      this.get('comment').rollbackAttributes();
    },

    save() {
      this.setProperties({
        isTextDisabled: true,
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
