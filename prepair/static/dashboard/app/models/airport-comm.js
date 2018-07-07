import DS from 'ember-data';
import { computed } from '@ember/object';

export const TYPE_OPTIONS = {
  CTAF: 1,
  UNICOM: 2,
  ATIS: 3,
  GROUND: 4,
  TOWER: 5,
  APPROACH: 6,
  DEPARTURE: 7,
  CLEARANCE: 8,
};

export default DS.Model.extend({
    airport: DS.belongsTo('airport'),
    frequency: DS.attr('number'),
    type: DS.attr('number', {defaultValue: TYPE_OPTIONS}),

    typePretty: computed('type', function () {
      switch (parseInt(this.get('type'))) {
        case 1:
          return "Common Traffic Advisory Frequency (CTAF)";
        case 2:
          return "Universal Communications (UNICOM)";
        case 3:
          return "Weather (ATIS)";
        case 4:
          return "Ground";
        case 5:
          return "Tower";
        case 6:
          return "Approach";
        case 7:
          return "Departure";
        case 8:
          return "Clearance";
      }
    }),

    frequencyPretty: computed('frequency', function () {
      const freq = this.get('frequency');
      return parseFloat(Math.round(freq * 100) / 100).toFixed(2);
    }),
});

