from Test_data.get_url import GetUrl
from api_calls.ApiCalls import ApiCalls
from utilities.json_utils import JsonUtilities
import pytest
import requests


class TestOne:
    ap = ApiCalls()
    gd= GetUrl()
    ju = JsonUtilities()

    url= gd.Fetch_the_url()['url']
    q = gd.Fetch_the_url()['q']
    appid = gd.Fetch_the_url()['appid']

    @pytest.mark.first
    def test_fetch_json_and_check_data_is_for_4_days(self):

        response= self.ap.get_from_the_url(self.url,self.q,self.appid)
        assert response.status_code == 200, 'Response Not correct'
        dict_response= self.ju.convert_json_in_dictionary_format(response)


        Number_of_days_data= self.ju.time_difference_between_latest_and_oldest_date(dict_response)

        assert Number_of_days_data >= 4, 'The data is not available for 4 days'







