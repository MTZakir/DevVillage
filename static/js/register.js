// Phone script

const phoneInputField = document.querySelector("#phone");
const phoneInput = window.intlTelInput(phoneInputField, {
    utilsScript:
    "https://cdnjs.cloudflare.com/ajax/libs/intl-tel-input/17.0.8/js/utils.js",
});



// Select field color correction

const selectElement = document.getElementById('expertise');

selectElement.addEventListener('change', function() {
    // Get the selected option
    const selectedOption = selectElement.options[selectElement.selectedIndex];

    // Check if the selected option is "Select Field of Proficiency"
    if (selectedOption.value === '') {
        selectElement.style.color = '#ffffff69';
    }
    else {
        selectElement.style.color = '#ffffffc1';
    }
});

// Add a click event listener to each list item with the class "iti__country"
$(".iti__country").on("click", function() {
    // Get the dial code value from the clicked list item
    var dialCode = $(this).find(".iti__dial-code").text();
    
    // Log the dial code value
    console.log("Selected dial code:", dialCode);

    // Set the dial code value to the phone field
    $("#phone").val(dialCode);
});