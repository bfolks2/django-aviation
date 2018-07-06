import DS from 'ember-data';

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
});
