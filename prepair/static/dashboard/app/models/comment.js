import DS from 'ember-data';
import { computed } from '@ember/object';
import _moment from 'ember-moment/computeds/moment';
import locale from 'ember-moment/computeds/locale';
import format from 'ember-moment/computeds/format';

export default DS.Model.extend({
    member: DS.belongsTo('member'),
    post: DS.belongsTo('post'),
    body: DS.attr('string'),
    datetimeCreated: DS.attr('date'),
    datetimeUpdated: DS.attr('date'),

    datetimeCreatedFormatted: format(
      locale(
          _moment('datetimeCreated'),
          'moment.locale'
      ),
      'MMMM DD, YYYY HH:mm'
    ),

    datetimeUpdatedFormatted: format(
      locale(
          _moment('datetimeUpdated'),
          'moment.locale'
      ),
      'MMMM DD, YYYY HH:mm'
    )

});
