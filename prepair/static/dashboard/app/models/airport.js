import DS from 'ember-data';
import { computed } from '@ember/object';

export default DS.Model.extend({
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

});
