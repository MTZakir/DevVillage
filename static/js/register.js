// Phone script

const phoneInputField = document.querySelector("#phone");
const phoneInput = window.intlTelInput(phoneInputField, {
    utilsScript:
    "https://cdnjs.cloudflare.com/ajax/libs/intl-tel-input/17.0.8/js/utils.js",
});


// Add a click event listener to each list item with the class "iti__country"
$(".iti__country").on("click", function() {
    // Get the dial code value from the clicked list item
    var dialCode = $(this).find(".iti__dial-code").text();

    // Set the dial code value to the phone field
    $("#phone").val(dialCode);
});



// ---------- Custom Multi-Select Tag field ----------

var dropdownInputField = document.getElementById("ms-input-field");
var dropdownSearch = document.getElementById("ms-search");
var dropdownMenu = document.getElementById("ms-dropdown");
var dropupMenu = document.getElementById("ms-tag-list");
var dropdownList = document.querySelectorAll(".option");
var hiddenList = document.getElementById("ms-hidden-list");


// Open dropdown when user types on search
dropdownSearch.addEventListener("focus", function(event) {
    dropdownMenu.classList.add("active");
});

// Close dropdown when not searching (Excluding dropdown, tags and input)
document.addEventListener("click", function(event) {
    if (!dropdownMenu.contains(event.target) && !dropupMenu.contains(event.target) && !dropdownInputField.contains(event.target) && event.target.tagName !== "LI") {
        dropdownMenu.classList.remove("active");
    }
});

// Open and close dropup menu (tag menu)
document.addEventListener("click", function(event) {
    openDropupMenu();
});

// Function to open or close dropup menu
function openDropupMenu() {
    var tagList = document.querySelectorAll(".tag");
    if (tagList.length > 0 && dropdownMenu.classList.contains("active")) {
        dropupMenu.classList.add("active");
    }
    else {
        dropupMenu.classList.remove("active");
    }
}

// Function to initialize the dropdown list
function initializeDropdownList() {
    dropdownList.forEach(function(option) {
        option.style.display = "block";
    });
};
initializeDropdownList()

// Sort dropdown list based on search input
dropdownSearch.addEventListener("keyup", function(event) {
    var searchTerm = dropdownSearch.value.toLowerCase();

    dropdownList.forEach(function(option) {
        var optionText = option.textContent.toLowerCase();
        var isSelected = false;

        // Looping through hidden list to find selected options and ignore them
        for (var i = 0; i < hiddenList.options.length; i++) {
            if (hiddenList.options[i].textContent.toLowerCase() === optionText && hiddenList.options[i].selected) {
                isSelected = true;
                break;
            };
        };

        // Displaying only non-selected options
        if (optionText.startsWith(searchTerm) && !isSelected) {
            option.style.display = "block";
        }
        else {
            option.style.display = "none";
        }
    });
});


// "Enter" behaviour of search field
dropdownSearch.addEventListener("keypress", function(event) {
    if (event.key === "Enter") {
        event.preventDefault();

        // Looping through the list and making sure only the first visible option is added
        var visibleOptions = [];
        dropdownList.forEach(function(option) {
            if (option.style.display == "block") {
                visibleOptions.push(option);
            }
        });

        // Adding the first element in the visible list of the dropdown as a tag
        var firstElement = visibleOptions[0];

        if (firstElement) {
            addTag(firstElement);
            openDropupMenu();
        }
    }
});

// "Backspace" behaviour of search field
dropdownSearch.addEventListener("keydown", function(event) {
    if (dropdownSearch.value === "" && event.key === "Backspace") {
        var tags = document.querySelectorAll(".tag");
        var lastTag = tags[tags.length - 1];

        if (lastTag) {
            deselectOption(lastTag.textContent.slice(0, -1));
            lastTag.remove();
        }
    }
});


// Add a tag on clicking an option
dropdownList.forEach(function(option) {
    option.addEventListener("click", function(event) {
        addTag(option)
    });
});

// Function to add a tag (pass in list option as parameter)
function addTag(option) {
    var tag = document.createElement("li");
    tag.className = "tag";
    tag.textContent = option.textContent;

    var tagCloseBtn = document.createElement("button");
    tagCloseBtn.className = "tag-close";
    tagCloseBtn.type = "button";
    tagCloseBtn.innerHTML = "&times;";

    tag.addEventListener("click", function(event) {
        tag.remove()
        deselectOption(option.textContent);
        option.style.display = "block";
    });

    tag.appendChild(tagCloseBtn);

    dropupMenu.appendChild(tag);

    option.style.display = "none";
    selectOption(option.textContent);
};


// Function for selecting the tags before form submission (pass in the selected option's text)
function selectOption(selectedOptionText) {
    var option;

    for (var i = 0; i < hiddenList.options.length; i++){
        option = hiddenList.options[i];

        if (option.textContent == selectedOptionText){
            option.selected = true;
        }
    }
};

// Function for deselecting the tags before form submission (pass in the deselected option's text)
function deselectOption(deselectedOptionText) {
    var option;

    for (var i = 0; i < hiddenList.options.length; i++){
        option = hiddenList.options[i];

        if (option.textContent == deselectedOptionText){
            option.selected = false;
        }
    }
};

