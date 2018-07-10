import Component from '@ember/component';
import TextArea from '@ember/component/text-area';
import { inject as service } from '@ember/service';
import { computed } from '@ember/object';


export default Component.extend({

  session: service(),
  store: service(),

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

  showButtons: computed('session.userID', function() {
    return this.get('session.userID') !== 0;
  }),


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
    },

    createComment() {
      this.disableAllButtons(true);
      this.set('createNewComment', true);
    },

    cancelComment() {
      this.set('createNewComment', false);
      this.disableAllButtons(false);
    },

    saveComment() {
      let user = this.get('store').peekRecord('user', this.get('session.userID'));
      let comment = this.get('store').createRecord('comment', {
        member: user.member,
        post: this.get('post'),
        body: this.get('newCommentBody'),
      });
      comment.save();

      this.set('createNewComment', false);
      this.disableAllButtons(false);
    },
  },

  disableAllButtons: function(bool) {
    this.get('disableAllButtons')(bool);
  }


});
