import configparser

config = configparser.RawConfigParser()
config.read('./Configurations/config.ini')

baseURL = config.get('commoninfo', 'baseURL')
username = config.get('commoninfo', 'username')
password = config.get('commoninfo', 'password')

# print(baseURL, username, password)

class ReadConfig:

    @staticmethod
    def getApplicationURL():
        return baseURL

    @staticmethod
    def getUsername():
        return username

    @staticmethod
    def getPassword():
        return password
