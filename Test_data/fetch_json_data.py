import pytest

from Test_data.get_url import GetUrl
from api_calls.ApiCalls import ApiCalls
import json

from utilities.json_utils import JsonUtilities


class FetchData():
    global Total_list
    ap = ApiCalls()
    gd = GetUrl()
    ju = JsonUtilities()
    global Total_days
    url = gd.Fetch_the_url()['url']
    q = gd.Fetch_the_url()['q']
    appid = gd.Fetch_the_url()['appid']

