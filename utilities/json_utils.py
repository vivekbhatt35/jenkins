import datetime
import json

import pytest


class JsonUtilities:

    def convert_json_in_dictionary_format(self,response):
        dict_response = json.loads(response.text)
        return dict_response

    def time_difference_between_latest_and_oldest_date(self,response):
        day_list = []


        for i in response['list']:
            dte = i['dt_txt']
            date_obj = datetime.datetime.strptime(dte, "%Y-%m-%d %H:%M:%S")
            day_list.append(date_obj.date())

        max_day = max(day_list)
        min_day = min(day_list)

        days = max_day - min_day
        return days.days


    def Get_All_dates(self, dict_response):

        global day_list
        day_list=[]
        for i in dict_response['list']:
             dte = i['dt_txt']
             date_obj = datetime.datetime.strptime(dte, "%Y-%m-%d %H:%M:%S")
             day_list.append(date_obj.timetuple())

        x = []
        for k in day_list:
            x.append(k.tm_mday)
        unique_days = list(set(x))
        return unique_days


    def check_Hourly_Update_for_days(self,unique_day):
        Day = []
        for i in day_list:
            if i.tm_mday == unique_day:
                Day.append(i.tm_hour)

            Unique_hours = list(set(Day))

        if len(Unique_hours) == 24:
            print(f"Day {unique_day} has data for 24 Hrs")
            Day = []
            return True

        else:
            print(f"The Day {unique_day} do not have entries for 24 Hours")
            Day = []
            return False

    def check_temp_within_range(self,dict_response):
        for i in dict_response['list']:
            return (i['main']['temp'] >= i['main']['temp_min']) and (i['main']['temp'] <= i['main']['temp_max'])



    def confirm_description_for_weatherID(self,dict_response,id,Expected_text):
        for i in dict_response['list']:
            if i['weather'][0]['id'] == id:
                return i['weather'][0]['description'] == Expected_text
