import Controller from '@ember/controller';
import { computed } from '@ember/object';

export default Controller.extend({

  init() {
    this.set('columnsForDataTable', [
      {
        "propertyName": "icao",
        "title": "ICAO",
        "sortedBy": "icao",
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

