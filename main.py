from CurrencyData import Currency, ExchangeData

def main():
    currency1 = Currency("USD")
    currency2 = Currency("EUR")
    exchangeData = ExchangeData(currency1, currency2)
    exchangeRate = exchangeData.getExchangeRate()
    print(f"1 {currency1.currencyCode} = {exchangeRate} {currency2.currencyCode}")

if __name__ == "__main__":
    main()