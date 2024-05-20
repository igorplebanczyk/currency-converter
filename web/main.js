let updateTimesContainer; // Declare the update times container variable globally

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
        // Display exchange rate in the app
        document.getElementById("result").innerText = result[0];

        // Display last and next update times
        if (!updateTimesContainer) {
            updateTimesContainer = document.createElement("div");
            updateTimesContainer.className = "update-time-container";
            document.body.appendChild(updateTimesContainer);
        } else {
            // Clear previous content
            updateTimesContainer.innerHTML = "";
        }

        latestUpdateTime = document.createElement("div");
        latestUpdateTime.className = "update-time";

        nextUpdateTime = document.createElement("div");
        nextUpdateTime.className = "update-time";

        updateTimesContainer.appendChild(latestUpdateTime);
        updateTimesContainer.appendChild(nextUpdateTime);

        latestUpdateTime.innerText = `Last updated: ${result[1]}`;
        nextUpdateTime.innerText = `Next update: ${result[2]}`;
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

// Load supported currencies and attach event listener to the switch button when the page is loaded
window.onload = function() {
    loadSupportedCurrencies();
    document.querySelector('.switch-button').addEventListener('click', switchCurrencies)
}