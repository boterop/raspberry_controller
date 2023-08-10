import requests
import json


class API:
    def request(url):
        return json.loads(requests.get(url).content)
