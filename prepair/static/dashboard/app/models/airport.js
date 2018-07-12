import DS from 'ember-data';
import { inject as service } from '@ember/service';
import { computed } from '@ember/object';

export default DS.Model.extend({
    session: service(),

    icao: DS.attr('string'),
    name: DS.attr('string'),
    region: DS.attr('string'),
    elevation: DS.attr('number'),
    metar: DS.attr('string'),
    taf: DS.attr('string'),
    sunrise: DS.attr('date'),
    sunset: DS.attr('date'),
    runways: DS.hasMany('runway'),
    comms: DS.hasMany('airport-comm'),
    members: DS.hasMany('member'),
    posts: DS.hasMany('post'),

    runwayCount: computed('runways.[]', function () {
      return (this.store.peekAll('runway').filterBy('airport.id', this.get('id')).length);
    }),

    hasWeather: computed('metar', 'taf', function () {
      const {
        metar,
        taf
      } = this.getProperties('metar', 'taf');

      return (metar || taf);
    }),

    hasPosts: computed('posts', function () {
      return this.get('posts').length > 0;
    }),

    isCurrentUserHome: computed('session.userID', 'members.[]', function() {
      const {
        id,
        'session.userID': userID,
      } = this.getProperties('id', 'session.userID');

      let peekMembers = this.store.peekAll('member').filterBy('homeAirport.id', id).filterBy('user.id', userID.toString());
      return peekMembers.length > 0;
    }),

});
