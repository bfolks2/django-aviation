import DS from 'ember-data';
import { computed } from '@ember/object';

export const SURFACETYPE_OPTIONS = {
  ASP: 1,
  CON: 2,
  GRS: 3,
  OTHER: 4,
};

export default DS.Model.extend({
    airport: DS.belongsTo('airport'),
    name: DS.attr('string'),
    surfaceType: DS.attr('number', {defaultValue: SURFACETYPE_OPTIONS}),
    length: DS.attr('number'),
    width: DS.attr('number'),
    bearing: DS.attr('number'),

    surfaceTypePretty: computed('surfaceType', function () {
      switch (parseInt(this.get('surfaceType'))) {
        case 1:
          return "Asphalt";
        case 2:
          return "Concrete";
        case 3:
          return "Grass";
        case 4:
          return "Other";
      }
    }),

});
