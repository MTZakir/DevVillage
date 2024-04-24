// Popup Hide / Display
var applyButton = document.getElementById("apply");
var applyPopup = document.getElementById("popup");
var backdrop = document.getElementById("backdrop");

applyButton.addEventListener("click", function(event) {
    if (!applyPopup.classList.contains('active')) {
        applyPopup.style.display = 'block';
        backdrop.style.display = 'block';

        setTimeout(function() {
            applyPopup.classList.add("active");
            backdrop.classList.add("active");
        }, 100);
    }

    event.stopPropagation();
});

document.addEventListener("click", function(event) {
    if (!applyPopup.contains(event.target)) {
        applyPopup.classList.remove("active");
        backdrop.classList.remove("active");

        setTimeout(function() {
            applyPopup.style.display = 'none';
            backdrop.style.display = 'none';
        }, 360);
    }
});


// Number input field
var pay_field = document.getElementById("pay_range");
var pay_left = document.getElementById("pay_left");
var pay_right = document.getElementById("pay_right");

pay_left.addEventListener("click", function(event) {
    var currentValue = parseInt(pay_field.value);
    var minValue = parseInt(pay_field.min);
    var stepValue = parseInt(pay_field.step);
    var newValue = currentValue - stepValue;
    if (newValue >= minValue) {
        pay_field.checkValidity();
        pay_field.value = newValue;
    }
});

pay_right.addEventListener("click", function(event) {
    var currentValue = parseInt(pay_field.value);
    var maxValue = parseInt(pay_field.max);
    var stepValue = parseInt(pay_field.step);
    var newValue = currentValue + stepValue;
    if (newValue <= maxValue) {
        pay_field.checkValidity();
        pay_field.value = newValue;
    }
});



// Form Error Validation
var form_submit_btn = document.getElementById("submit-btn");
var file_input = document.getElementById("resume");
var file_label = document.querySelector("label[for='resume']");

form_submit_btn.addEventListener("click", function(event) {
    var error_tag = document.getElementById("file_error");

    if (!file_input.checkValidity() && !error_tag) {
        file_label.insertAdjacentHTML('afterend', '<span class="error-message" id="file_error">Please select a file.</span>');
    }
});
