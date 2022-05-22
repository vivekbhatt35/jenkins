from utilities.common_utilities import CommonUtils

class GetUrl(CommonUtils):

    def Fetch_the_url(self):
        value={}
        value['url']= self.getConfig()['API']['url']
        value['q']=self.getConfig()['API']['q']
        value['appid'] =self.getConfig()['API']['appid']
        return value
