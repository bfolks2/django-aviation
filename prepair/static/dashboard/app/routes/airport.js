import Route from '@ember/routing/route';
import RSVP from 'rsvp';

export default Route.extend({
  model(params) {
    let airportPromise = this.store.findRecord('airport', params.airport_id);

    return RSVP.hash({
      airport: airportPromise,
    });
  }
});
