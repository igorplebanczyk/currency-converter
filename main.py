import eel
from exchange import ExchangeData, getAllSupportedCurrencies

# Initialize the Eel library
eel.init('web')

@eel.expose
def getAllSupportedCurrenciesExposed():
    return getAllSupportedCurrencies()

@eel.expose
def getExchangeDataExposed(currency1, currency2, amount):
    exchange_data = ExchangeData(currency1, currency2, amount)
    return (exchange_data.getExchangeRate(), exchange_data.getLatestUpdate(), exchange_data.getNextUpdate())

def main():
    eel.start('index.html', size=(800, 600), mode='opera', port=7000)

if __name__ == "__main__":
    main()
