import pdb

import pytest

from Test_data.get_url import GetUrl
from api_calls.ApiCalls import ApiCalls
from utilities.json_utils import JsonUtilities


class TestThree:
    ap = ApiCalls()
    gd= GetUrl()
    ju = JsonUtilities()

    url= gd.Fetch_the_url()['url']
    q = gd.Fetch_the_url()['q']
    appid = gd.Fetch_the_url()['appid']

    @pytest.mark.first
    def test_temp_should_not_be_out_than_limits(self):

        response= self.ap.get_from_the_url(self.url,self.q,self.appid)
        assert response.status_code == 200, 'Response Not correct'
        dict_response= self.ju.convert_json_in_dictionary_format(response)
        #pdb.set_trace()
        assert self.ju.check_temp_within_range(dict_response)

