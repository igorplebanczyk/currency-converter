import eel
from exchange import Currency, ExchangeData, getAllSupportedCurrencies

# Initialize the Eel library
eel.init('web')

@eel.expose
def getAllSupportedCurrenciesExposed():
    return getAllSupportedCurrencies()

@eel.expose
def getExchangeRateExposed(currency1, currency2):
    currency1_obj = Currency(currency1)
    currency2_obj = Currency(currency2)
    exchange_data = ExchangeData(currency1_obj, currency2_obj)
    return exchange_data.getExchangeRate()

def main():
    eel.start('index.html', size=(800, 600), mode='opera', port=7000)

if __name__ == "__main__":
    main()
