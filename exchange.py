import requests

API_KEY = "7e50a8f6c133c6ce223a0d2b"

def getAllSupportedCurrencies(codes: bool = True, names: bool = True):
        url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/codes"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        if data["result"] == "success":
            if codes:
                return [currency[0] for currency in data["supported_codes"]]
            elif names:
                return [currency[1] for currency in data["supported_codes"]]
            else:
                return data["supported_codes"]
        else:
            raise Exception(f"Failed to fetch data: {data['error']}")

class Currency():
    def  __init__(self, currencyCode):
        self.currencyCode = currencyCode
        self.__singleCurrencyExchangeRatesUrl = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{self.currencyCode}"
    
    def getSingleCurrencyExchangeRates(self):
        response = requests.get(self.__singleCurrencyExchangeRatesUrl)
        response.raise_for_status()
        data = response.json()
        if data["result"] == "success":
            return data["conversion_rates"]
        else:
            raise Exception(f"Failed to fetch data: {data['error']}")
        
    
class ExchangeData():
    def __init__(self, currency1: Currency, currency2: Currency):
        self.currency1 = currency1
        self.currency2 = currency2
    
    def getExchangeRate(self):
        exchangeRates = self.currency1.getSingleCurrencyExchangeRates()
        return exchangeRates[self.currency2.currencyCode]