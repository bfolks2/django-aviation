import Controller from '@ember/controller';

export default Controller.extend({

  init() {
    this.set('columnsForDataTable', [
      {
        "propertyName": "icao",
        "title": "ICAO",
        "className": "icao-column",
        "component": "models-table/link-to-airport",
      },
      {
        "propertyName": "name",
        "title": "Name",
      },
      {
        "propertyName": "region",
        "title": "Region",
      },
      {
        "propertyName": "elevation",
        "title": "Elevation (MSL, ft)",
      },
      {
        "propertyName": "runwayCount",
        "title": "Number of Runways"
      },
    ]);

    this._super(...arguments);
  },

});

