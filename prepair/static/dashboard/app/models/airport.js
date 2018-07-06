import DS from 'ember-data';

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
    comms: DS.hasMany('airport-comm')
});
