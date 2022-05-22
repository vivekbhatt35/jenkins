import pytest

from Test_data.get_url import GetUrl
from api_calls.ApiCalls import ApiCalls
from utilities.json_utils import JsonUtilities


class TestFive:
    ap = ApiCalls()
    gd = GetUrl()
    ju = JsonUtilities()

    url = gd.Fetch_the_url()['url']
    q = gd.Fetch_the_url()['q']
    appid = gd.Fetch_the_url()['appid']
    id =800
    Expected_text = "clear sky"

    @pytest.mark.fifth
    def test_check_description_for_weatherID_800(self):
        response = self.ap.get_from_the_url(self.url, self.q, self.appid)
        assert response.status_code == 200, 'Response Not correct'
        dict_response = self.ju.convert_json_in_dictionary_format(response)
        assert self.ju.confirm_description_for_weatherID(dict_response, self.id, self.Expected_text)