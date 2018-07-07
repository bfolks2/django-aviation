import Service from '@ember/service';

export default Service.extend({

  userID: null,
  airportID: null,

  initializeVariables() {
    this.setProperties({
      userID: window.user_id,
      airportID: window.airport_pk,
    });
  }
});
