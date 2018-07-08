import Route from '@ember/routing/route';
import RSVP from 'rsvp';
import { inject as service } from '@ember/service';

export default Route.extend({
  session: service(),

  model(params) {
    const windowID = this.get('session.airportID');
    const airportID = params.airport_id;

    let runwaysPromise = this.store.query('runway', {
      'airport': airportID
    });
    let commsPromise = this.store.query('airport-comm', {
      'airport': airportID
    });
    let postsPromise = this.store.query('post', {
      'airport': airportID
    });
    let commentsPromise = this.store.findAll('comment');
    let membersPromise = this.store.findAll('member');
    let usersPromise = this.store.findAll('user');

    // Nested Promises to make sure the weather is updated/resolved before getting the airport data
    // let adapter = this.get('store').adapterFor('airport');
    // let weatherPromise = adapter.airportWeather(airportID, windowID);
    //
    // let airportPromise = new Promise((resolve) => {
    //   weatherPromise.then(() => {
    //     let embedPromise = this.store.findRecord('airport', airportID);
    //     resolve(embedPromise);
    //   });
    // });
    let airportPromise = this.store.findRecord('airport', airportID);

    return RSVP.hash({
      runways: runwaysPromise,
      comms: commsPromise,
      airport: airportPromise,
      posts: postsPromise,
      comments: commentsPromise,
      members: membersPromise,
      users: usersPromise

    });
  }
});
