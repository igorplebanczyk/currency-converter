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
            option1.text = currency[1]; // Full currency name
            option1.value = currency[0]; // Currency code
            option2.text = currency[1]; // Full currency name
            option2.value = currency[0]; // Currency code
            currency1Select.appendChild(option1);
            currency2Select.appendChild(option2);
        });
    });
}

function getExchangeRate(currency1, currency2, amount) {
    eel.getExchangeDataExposed(currency1, currency2, amount)(function(result) {
        document.getElementById("result").innerText = result[0];
        document.getElementById("last-updated").innerText = `Last updated: ${result[1]}`;
        document.getElementById("next-update").innerText = `Next update: ${result[2]}`;
    });
}

function switchCurrencies() {
    let currency1Select = document.getElementById("currency1");
    let currency2Select = document.getElementById("currency2");

    // Swap the selected values
    let temp = currency1Select.value;
    currency1Select.value = currency2Select.value;
    currency2Select.value = temp;

    // Trigger the onchange event for both selectors to update the displayed exchange rate
    currency1Select.dispatchEvent(new Event('change'));
    currency2Select.dispatchEvent(new Event('change'));
}

window.onload = function() {
    loadSupportedCurrencies();
    document.querySelector('.currency-converter__button--switch').addEventListener('click', switchCurrencies);
}
