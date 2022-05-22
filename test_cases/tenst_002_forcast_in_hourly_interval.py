import pytest
from Test_data.fetch_json_data import FetchData
from Test_data.get_url import GetUrl
from api_calls.ApiCalls import ApiCalls
from utilities.json_utils import JsonUtilities


class TestTwo():
    ap = ApiCalls()
    gd = GetUrl()
    ju = JsonUtilities()
    fd = FetchData()
    url = gd.Fetch_the_url()['url']
    q = gd.Fetch_the_url()['q']
    appid = gd.Fetch_the_url()['appid']


    @pytest.mark.second
    def test_check_hourly_update_available(self):
        response = self.ap.get_from_the_url(self.url, self.q, self.appid)
        assert response.status_code == 200, 'Response Not correct'
        dict_response = self.ju.convert_json_in_dictionary_format(response)
        Total_days = []
        Total_days=self.ju.Get_All_dates(dict_response)

        j=0
        for i in Total_days:

            if self.ju.check_Hourly_Update_for_days(i):
                pass
            else:
                j += 1
        assert j == 0

