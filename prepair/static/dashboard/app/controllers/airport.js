import Controller from '@ember/controller';
import { inject as service } from '@ember/service';
import { computed } from '@ember/object';

export default Controller.extend({

  session: service(),

  weatherID: null,
  isButtonDisabled: null,
  createNewPost: null,

  showButtons: computed('session.userID', function() {
    return this.get('session.userID') !== 0;
  }),

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
      this.set('createNewPost', false);
      this.disableAllButtons(false);
    },

    save() {
      // INSERT SAVING LOGIC
      this.set('createNewPost', false);
      this.disableAllButtons(false);
    },
  }

});
