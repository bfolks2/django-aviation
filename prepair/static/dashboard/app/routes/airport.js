import Route from '@ember/routing/route';
import RSVP from 'rsvp';

export default Route.extend({
  model(params) {
    const airportID = params.airport_id

    let airportPromise = this.store.findRecord('airport', airportID);
    let runwaysPromise = this.store.query('runway', {
      'airport': airportID
    });
    let commsPromise = this.store.query('airport-comm', {
      'airport': airportID
    });

    return RSVP.hash({
      airport: airportPromise,
      runways: runwaysPromise,
      comms: commsPromise
    });
  }
});
