import pytest
from Test_data.fetch_json_data import FetchData
from Test_data.get_url import GetUrl
from api_calls.ApiCalls import ApiCalls
from utilities.File_Operations import FileOperation
from utilities.json_utils import JsonUtilities


class TestTwo():
    ap = ApiCalls()
    gd = GetUrl()
    ju = JsonUtilities()
    fd = FetchData()
    file = FileOperation()
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
        self.file.write_to_file(Total_days)

    @pytest.mark.parametrize('tota',file.read_from_file())
    def test_for_the_number_of_days(self,tota):
        assert self.ju.check_Hourly_Update_for_days(tota)