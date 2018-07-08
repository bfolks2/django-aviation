import DS from 'ember-data';

export default DS.Model.extend({
    user: DS.attr('number'),
    homeAirport: DS.belongsTo('airport'),
    posts: DS.hasMany('post'),
    comments: DS.hasMany('comment'),
});
