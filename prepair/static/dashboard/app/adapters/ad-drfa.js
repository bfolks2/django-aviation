import DRF from "./drf";
import config from '../config/environment';

const HEADERS = {
  'X-CSRFTOKEN': 'fakecsrftoken' //document.getElementById('csrfmiddlewaretokennav').value
};

export default DRF.extend({
  namespace: config.adapterPrefix,
  addTrailingSlashes: false,
  headers: HEADERS
});
