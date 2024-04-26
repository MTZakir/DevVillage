// TRIPLE INPUT

var threeFieldInputs = document.querySelectorAll(".three-field");
var scope = document.getElementById("scope");
var deliverables = document.getElementById("deliverables");
var tech_stack = document.getElementById("tech_stack");
var notes = document.getElementById("notes");

// Create an array to hold the input values for each group of three inputs
var inputsLists = [[], [], [], []];

// Iterate over each group of three inputs
threeFieldInputs.forEach(function(input, index) {
    // Attach an input event listener to each input field
    input.addEventListener('input', function(event) {
        var inputIndex = Array.from(input.parentNode.children).indexOf(input);
        var groupIndex = Math.floor(index / 3);
        inputsLists[groupIndex][inputIndex] = input.value;

        
        var filteredList = inputsLists[groupIndex].filter(Boolean);

        var formattedList = '[' + filteredList.join(',') + ']';


        switch (groupIndex) {
            case 0:
                scope.value = formattedList;
                break;
            case 1:
                deliverables.value = formattedList;
                break;
            case 2:
                tech_stack.value = formattedList;
                break;
            case 3:
                notes.value = formattedList;
                break;
        }
    });
});





// Image upload field

var image_field = document.getElementById("contract_img");
var image_label = document.getElementById("contract_img_label");
var origialText = image_label.textContent;

image_field.addEventListener("change", function() {
    if (image_field.files.length > 0) {
        image_label.textContent = image_field.files[0].name;

        image_label.addEventListener("click", function(event) {
            event.preventDefault()

            image_field.value = '';
            image_label.textContent = origialText;
        });
    }
    else {
        image_label.textContent = origialText;
    }
});