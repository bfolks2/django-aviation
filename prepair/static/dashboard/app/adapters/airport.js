import ApplicationAdapter from './application';

export default ApplicationAdapter.extend({

  airportWeather(airportID, windowID) {
    const url = this.buildURL('airport', airportID) + "/airport_weather?window=" +  windowID;
    return this.ajax(url, 'GET');
  },

});
