import DS from 'ember-data';

export default DS.Model.extend({
    member: DS.belongsTo('member'),
    post: DS.belongsTo('post'),
    body: DS.attr('string'),
    datetimeCreated: DS.attr('date'),
    datetimeUpdated: DS.attr('date'),
});
