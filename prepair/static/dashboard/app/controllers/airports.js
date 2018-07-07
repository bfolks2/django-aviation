import Controller from '@ember/controller';

export default Controller.extend({

  init() {
    this.set('columnsForDataTable', [
      {
        "propertyName": "icao",
        "title": "ICAO",
        "sortedBy": "icao",
        "className": "icao-column"
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

