from furl import furl
import requests
import os

from typing import List, Union, Dict
"""
The application is to make it easy for people to compare data sets.
Most likely in my applicaation, I will need the categories, sources, releases, and series ids
in the database from a daily job. The actual datasets will we stored in digital ocean spaces
and will be refreshed when new data comes out (celery?). I still need to figure out the cadence.

1. Categories model and function
2. Tags model and api call
3. Sources model and api call
4. Releases model and call
5. Series model and call
6. Observations in spaces wrapper
7. Celery set up
8. Frontend...
"""

# Root of the tree to get all categories
# http://api.stlouisfed.org/fred/category/children?category_id=0&api_key=a999a6feb32c96927b37ba0debbbe8da


class FredWrapper:

    FRED_API_KEY = os.getenv('FRED_API_KEY')

    def __init__(self, api_key=FRED_API_KEY):
        self.api_key = api_key
        self.url = 'https://api.stlouisfed.org/fred/'
        self.file_type = 'json'

    def _build_url(self, endpoint: str, args: Dict[str, str]=None):
        if endpoint.startswith('/'):
            raise ValueError('Endpoint cannot begin with /!')
        f = furl(self.url + endpoint)
        if args:
            for name, value in args.items():
                f[name] = value
        return f.url

    def _get_request(self, url: str) -> requests.Response:
        return requests.get(url)

    def get_category(self, category_id: int) -> Dict[str, List[Dict[str, Union[str, int]]]]:
        url = self._build_url('category/')
        return self._get_request(url).json()


