import Component from '@ember/component';
import TextArea from '@ember/component/text-area';

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
      this.get('post').rollbackAttributes();
      this.disableAllButtons(false);
    },

    save() {
      this.setProperties({
        isTextDisabled: true,
        showAddComment: true,
        showSaveCancel: false,
      });
      let postRecord = this.get('post');
      postRecord.save();
      this.disableAllButtons(false);
    },

    delete() {
      let postRecord = this.get('post');
      postRecord.destroyRecord();
      this.disableAllButtons(false);
    }
  },

  disableAllButtons: function(bool) {
    this.get('disableAllButtons')(bool);
  }


});
