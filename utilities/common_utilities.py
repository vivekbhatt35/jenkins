import configparser

class CommonUtils:

    def getConfig(self):
        config = configparser.ConfigParser()
        config.read(r'C:\Users\rsi\PycharmProjects\LondonWeather\utilities\properties.ini')
        return config



