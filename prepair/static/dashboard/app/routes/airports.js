import Route from '@ember/routing/route';
import RSVP from 'rsvp';

export default Route.extend({
  model() {
    let airports = this.modelFor('application').airports;
    let runways = this.modelFor('application').runways;

    return RSVP.hash({
      airports: airports,
      runways: runways
    });
  }
});
