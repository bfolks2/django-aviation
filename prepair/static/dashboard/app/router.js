import EmberRouter from '@ember/routing/router';
import config from './config/environment';

const Router = EmberRouter.extend({
  location: config.locationType,
  rootURL: config.rootURL
});

Router.map(function() {
  this.route('airports');
  this.route('airport', {path: 'airport/:airport_id'});
});

export default Router;
