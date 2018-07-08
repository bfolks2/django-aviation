import Route from '@ember/routing/route';
import RSVP from 'rsvp';

export default Route.extend({

  model(params) {
    const airportID = params.airport_id;

    let runwaysPromise = this.store.query('runway', {
      'airport': airportID
    });
    let commsPromise = this.store.query('airport-comm', {
      'airport': airportID
    });

    let adapter = this.get('store').adapterFor('airport');
    let weatherPromise = adapter.airportWeather(airportID);

    let airportPromise = new Promise((resolve) => {
      weatherPromise.then(() => {
        let embedPromise = this.store.findRecord('airport', airportID);
        resolve(embedPromise);
      });
    });

    return RSVP.hash({
      runways: runwaysPromise,
      comms: commsPromise,
      airport: airportPromise
    });
  }
});
