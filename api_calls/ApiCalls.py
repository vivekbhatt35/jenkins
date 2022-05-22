import json

import requests


class ApiCalls:

    def get_from_the_url(self,url,q,appid):
        response = requests.get(url, params={"q": q, "appid":appid})
        return response


