import Controller from '@ember/controller';

export default Controller.extend({

  weatherID: null,
  isButtonDisabled: null,
  createNewPost: null,

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
        "title": "Bearing (°)",
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
    this.setProperties({
      isButtonDisabled: false,
      createNewPost: false,
    });
  },

  disableAllButtons: function(bool) {
    this.set('isButtonDisabled', bool);
  },

  actions: {
    create() {
      this.disableAllButtons(true);
      this.set('createNewPost', true);
    },

    cancel() {
      this.setProperties({
        isTextDisabled: true,
      });
      this.set('createNewPost', false);
      this.disableAllButtons(false);
    },

    save() {
      this.setProperties({
        isTextDisabled: true,
      });
      // INSERT SAVING LOGIC
      this.set('createNewPost', false);
      this.disableAllButtons(false);
    },
  }

});
