import Controller from '@ember/controller';

export default Controller.extend({

  weatherID: null,

  init() {
    this.set('columnsForRunwayTable', [
      {
        "propertyName": "name",
        "title": "Runway Name",
      },
      {
        "propertyName": "surfaceTypePretty",
        "title": "Surface Type",
      },
      {
        "propertyName": "bearing",
        "title": "Bearing",
      },
      {
        "propertyName": "length",
        "title": "Length (ft)",
      },
      {
        "propertyName": "width",
        "title": "Width (ft)",
      },
    ]);

    this.set('columnsForCommTable', [
      {
        "propertyName": "frequencyPretty",
        "title": "Frequency",
      },
      {
        "propertyName": "typePretty",
        "title": "Type",
      },
    ]);

    this._super(...arguments);
  },

});
