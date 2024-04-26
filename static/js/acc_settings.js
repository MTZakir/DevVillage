var pfp_input = document.getElementById("update-bttn-text");
var pfp_msg = document.getElementById("pfp_msg");
var input_fields = document.querySelectorAll(".personal-input-fields");
var save_btn = document.getElementById("save_btn");
var original_list = []
var current_list = []

original_list.push(pfp_input.value)
current_list.push(pfp_input.value)

input_fields.forEach(function(input_field) {
    original_list.push(input_field.value)
    current_list.push(input_field.value)

    input_field.addEventListener("input", function(event) {
        // Gives the index value of the currently used input field
        var index_of_input = Array.from(input_fields).indexOf(input_field);

        current_list[index_of_input + 1] = input_field.value;

        change_checker()
    });
});

pfp_input.addEventListener("change", function() {
    if (pfp_input.files.length > 0) {
        pfp_msg.textContent = pfp_input.files[0].name;
        pfp_msg.style.display = "block";

        // Change has been made - File added
        current_list[0] = pfp_input.value;
        change_checker()
    }
    else {
        pfp_msg.style.display = "none";

        // Change has been made - File removed
        current_list[0] = pfp_input.value;
        change_checker()
    }
});

pfp_msg.addEventListener("click", function() {
    current_list[0] = '';
    change_checker()
    pfp_input.value = '';
    pfp_msg.textContent = '';
});

// Function to check for any change, if change > save btn = active
function change_checker() {
    for (var i = 0; i < current_list.length - 1; i++) {
        if (current_list[i] != original_list[i]) {
            save_btn.classList.add("active");
            save_btn.disabled = false;
            break;
        }
        else {
            save_btn.classList.remove("active");
            save_btn.disabled = true;
        }
    }
}