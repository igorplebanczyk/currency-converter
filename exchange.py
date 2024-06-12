import requests

API_KEY = "7e50a8f6c133c6ce223a0d2b"

def getAllSupportedCurrencies():
        url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/codes"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        if data["result"] == "success":
            return data["supported_codes"]
        else:
            raise Exception(f"Failed to fetch data: {data['error']}")       
    
class ExchangeData():
    __cache = {}

    def __init__(self, currency1, currency2, amount):
        self.currency1 = currency1
        self.currency2 = currency2
        self.amount = amount

        self.__url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/pair/{self.currency1}/{self.currency2}/{self.amount}"
        
        if len(ExchangeData.__cache) > 100:
            self.clearCache()

        if self.__url in ExchangeData.__cache:
            self.readFromCache()
        else:
            self.response = requests.get(self.__url)
            self.response.raise_for_status()
            self.data = self.response.json()
            self.writeToCache()

    def readFromCache(self):
        self.data = ExchangeData.__cache[self.__url]

    def writeToCache(self):
        ExchangeData.__cache[self.__url] = self.data

    def clearCache(self):
        ExchangeData.__cache = {}

    
    def getExchangeRate(self):
        if self.data["result"] == "success":
            return self.data["conversion_result"]
        else:
            raise Exception(f"Failed to fetch data: {self.data['error']}")
    
    def getLatestUpdate(self):
        if self.data["result"] == "success":
            return self.data["time_last_update_utc"][5:-9]
        else:
            raise Exception(f"Failed to fetch data: {self.data['error']}")
    
    def getNextUpdate(self):
        if self.data["result"] == "success":
            return self.data["time_next_update_utc"][5:-9]
        else:
            raise Exception(f"Failed to fetch data: {self.data['error']}")