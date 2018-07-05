function validateICAO() {
    var inputElement = $('#icao-input');
    var value = inputElement.val();

    if (value.length < 3 || value.length > 4) {
        toggleSubmit(true);
    } else {
        toggleSubmit(false);
    }
}

function toggleSubmit(status) {
    document.getElementById("submit-btn").disabled = status;
}