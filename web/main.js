function loadSupportedCurrencies() {
    eel.getAllSupportedCurrenciesExposed()(function(result) {
        // Process result (e.g., display in dropdown)
        let currencies = result;
        let currency1Select = document.getElementById("currency1");
        let currency2Select = document.getElementById("currency2");

        // Clear existing options
        currency1Select.innerHTML = "";
        currency2Select.innerHTML = "";

        // Add new options
        currencies.forEach(function(currency) {
            let option1 = document.createElement("option");
            let option2 = document.createElement("option");
            option1.text = currency;
            option1.value = currency;
            option2.text = currency;
            option2.value = currency;
            currency1Select.appendChild(option1);
            currency2Select.appendChild(option2);
        });
    });
}

function getExchangeRate(currency1, currency2) {
    eel.getExchangeRateExposed(currency1, currency2)(function(result) {
        // Display exchange rate in the app
        let modifier = document.getElementById("modifier");
        document.getElementById("result").innerText = result * modifier.value;
    });
}

// Load supported currencies when the page is loaded
window.onload = function() {
    loadSupportedCurrencies();
}