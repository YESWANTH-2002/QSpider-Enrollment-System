// enrollment/static/enrollment/script.js

document.addEventListener('DOMContentLoaded', function () {
    // Example: Disable submit button if the checkbox is not checked
    const feeCheckbox = document.getElementById('id_has_paid_fees');
    const submitButton = document.querySelector('button[type="submit"]');

    feeCheckbox.addEventListener('change', function () {
        submitButton.disabled = !feeCheckbox.checked;
    });
});
