import Controller from '@ember/controller';
import TextArea from '@ember/component/text-area';
import { inject as service } from '@ember/service';
import { computed } from '@ember/object';

export default Controller.extend({

  session: service(),

  weatherID: null,
  isButtonDisabled: null,
  createNewPost: null,
  newBody: null,

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
    makeHome() {
      const {
        'session.userID': userID,
        'model.airport': airport,
      } = this.getProperties('session.userID','model.airport');

      let user = this.store.peekRecord('user', userID);
      let member = user.memberInstance;

      member.setProperties({'homeAirport': airport});
      member.save()
    },

    createNew() {
      this.disableAllButtons(true);
      this.set('createNewPost', true);
    },

    cancelNew() {
      this.setProperties({
        newBody: null,
        createNewPost: false,
      });
      this.disableAllButtons(false);
    },

    saveNew() {
      let user = this.store.peekRecord('user', this.get('session.userID'));
      let post = this.store.createRecord('post', {
        member: user.member,
        airport: this.get('model.airport'),
        body: this.get('newBody'),
      });
      post.save();

      this.setProperties({
        newBody: null,
        createNewPost: false,
      });
      this.disableAllButtons(false);
    },
  }

});
