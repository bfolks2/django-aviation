import DS from 'ember-data';

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
});

