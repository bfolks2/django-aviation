import DS from 'ember-data';
import { computed } from '@ember/object';
import _moment from 'ember-moment/computeds/moment';
import locale from 'ember-moment/computeds/locale';
import format from 'ember-moment/computeds/format';
import { inject as service } from '@ember/service';

export default DS.Model.extend({
    session: service(),

    member: DS.belongsTo('member'),
    post: DS.belongsTo('post'),
    body: DS.attr('string'),
    datetimeCreated: DS.attr('date'),
    datetimeUpdated: DS.attr('date'),

    userName: computed('member', function() {
      return this.get('member.user.username');
    }),

    userID: computed('member', function() {
      return this.get('member.user.id');
    }),

    allowUserEditDelete: computed('userID', 'session.userID', function() {
      const {
        userID,
        'session.userID': sessionID
      } = this.getProperties('userID', 'session.userID');

      return userID == sessionID;
    }),

    datetimeCreatedFormatted: format(
      locale(
          _moment('datetimeCreated'),
          'moment.locale'
      ),
      'MMMM DD, YYYY, h:mm a'
    ),

    datetimeUpdatedFormatted: format(
      locale(
          _moment('datetimeUpdated'),
          'moment.locale'
      ),
      'MMMM DD, YYYY, h:mm a'
    ),

    hasUpdate: computed('datetimeCreatedFormatted', 'datetimeUpdatedFormatted', function() {
      const {
        datetimeCreatedFormatted,
        datetimeUpdatedFormatted
      } = this.getProperties('datetimeCreatedFormatted', 'datetimeUpdatedFormatted');

      return datetimeCreatedFormatted !== datetimeUpdatedFormatted;
    }),

});
