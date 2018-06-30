import requests


class FlightPlanAPIClient(object):
    """
    API Client class used to construct requests to FlightPlaneDatabase's Airport Information API
    """

    HOST = 'https://api.flightplandatabase.com/'

    def __init__(self, *args, **kwargs):
        self.http_session = requests.Session()

    def get(self, icao):
        url = u'{}nav/airport/{}'.format(self.HOST, icao)

        headers = {
            'Authorization': 'ENTER-API-KEY-HERE',
            'Accept': 'application/json',
            'X-Units': 'AVIATION',
        }

        response = self.http_session.get(url, headers=headers)
        json = response.json()
        return json
