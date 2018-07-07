import Route from '@ember/routing/route';
import { inject as service } from '@ember/service';

export default Route.extend({
  session: service(),

  beforeModel() {
    const session = this.get('session');
    session.initializeVariables();
  },

  afterModel() {
    const airportID = this.get('session.airportID');
    if (airportID != 0) {
      this.transitionTo('airport', airportID);
    } else {
      this.transitionTo('airports');
    }
  }
});
