import ApplicationAdapter from './application';

export default ApplicationAdapter.extend({

  airportWeather(airportID) {
    const url = this.buildURL('airport', airportID) + "/airport_weather";
    return this.ajax(url, 'GET');
  },

});
