import Controller from '@ember/controller';
import { computed } from '@ember/object';

export default Controller.extend({
  currentPageNumber: 1,
  pageToJumpTo: 1,
  pageSize: 25,

  pagesCount: computed('model.airports.meta.count', function() {
    return Math.ceil(this.get('model.airports.meta.count') / 25);
  }),

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

  actions: {
    next(jumpMethod, currentPageNumber, pagesCount) {
      currentPageNumber = parseInt(currentPageNumber);
      if (currentPageNumber >= pagesCount) {
        return;
      }

      let newPageNumber = currentPageNumber + 1;

      jumpMethod(newPageNumber);
      this.set('pageToJumpTo', newPageNumber);
    },

    prev(jumpMethod, currentPageNumber) {
      currentPageNumber = parseInt(currentPageNumber);
      if (currentPageNumber <= 1) {
        return;
      }

      let newPageNumber = currentPageNumber - 1;

      jumpMethod(newPageNumber);
      this.set('pageToJumpTo', newPageNumber);
    },
  }
});

