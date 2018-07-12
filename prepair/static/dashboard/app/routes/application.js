import Route from '@ember/routing/route';
import { inject as service } from '@ember/service';

export default Route.extend({
  session: service(),

  beforeModel() {
    const session = this.get('session');
    session.initializeVariables();
  },

  model() {
    let airportsPromise = this.store.findAll('airport');
    let runwaysPromise = this.store.findAll('runway');

    return {
      airports: airportsPromise,
      runways: runwaysPromise
    };
  },

  afterModel() {
    const {
      'session.airportID': airportID,
      'session.baseRedirect': baseRedirect
    } = this.getProperties('session.airportID', 'session.baseRedirect')

    if (airportID !== 0) {
      this.transitionTo('airport', airportID);
    } else if (baseRedirect === 1) {
      this.transitionTo('airports');
    }
  }
});
