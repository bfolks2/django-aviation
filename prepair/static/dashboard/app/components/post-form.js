import Component from '@ember/component';
import { inject as service } from '@ember/service';

export default Component.extend({

  session: service(),

  /**
   * The posts bound to this component.
   *
   * @argument posts
   * @type object
   * @default null
   */
  posts: null,

  /**
   * The airport bound to this component.
   *
   * @argument airport
   * @type object
   * @default null
   */
  airport: null,

  /**
   * The user in the active session.
   *
   * @argument userID
   * @type object
   * @default null
   */
  userID: null,

  init() {
    this._super(...arguments);
    this.set('userID', this.get('session.userID'));
  },

});
