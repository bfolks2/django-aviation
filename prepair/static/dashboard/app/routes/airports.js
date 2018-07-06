import Route from '@ember/routing/route';
import RSVP from 'rsvp';

export default Route.extend({
  model() {
    let airportsPromise = this.store.findAll('airport');
    let runwaysPromise = this.store.findAll('runway');

    return RSVP.hash({
      airports: airportsPromise,
      runways: runwaysPromise
    });
  }
});
