import DS from 'ember-data';
import { computed } from '@ember/object';

export default DS.Model.extend({
    username: DS.attr('string'),
    member: DS.belongsTo('member'),

    memberInstance: computed('member', function() {
      const {
        id,
      } = this.getProperties('id');

      let memberId = this.store.peekAll('member').filterBy('user.id', id.toString()).getEach('id').uniq();
      return this.store.peekRecord('member', memberId);
    }),
});

