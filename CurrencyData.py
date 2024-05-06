import requests
API_KEY = "7e50a8f6c133c6ce223a0d2b"

class Currency():
    def  __init__(self, currencyCode):
        self.currencyCode = currencyCode
    
    def getAllExchangeRates(self):
        URL = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{self.currencyCode}"

        response = requests.get(URL)
        if response.status_code == 200:
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
        exchangeRates = self.currency1.getAllExchangeRates()
        return exchangeRates[self.currency2.currencyCode]