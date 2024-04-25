var wallet_input = document.getElementById("wallet_input");
var wallet_holder = document.getElementById("wallet_holder");
var wallet_form = document.getElementById("wallet_form");
var error_msg = document.getElementById("error_msg");
var list = [];
var canSubmit = true;

wallet_input.addEventListener("input", function(event) {
    var currentChar = wallet_input.value.charAt(wallet_input.value.length - 1);
    
    // If empty input, do nothing
    if (wallet_input.value == "") {
        list = [];
        wallet_holder.classList.remove("active");
        error_msg.classList.remove("active");
    }

    // Backspace activity
    if (event.inputType === "deleteContentBackward") {
        if (wallet_input.value == "") {
            list = [];
        }
        else {
            list.pop();
        }
        return;
    }

    // Append datatype of current char in list
    if (!isNaN(parseInt(currentChar))) {
        list.push("Integer");
    }
    else {
        list.push("Else");
    }

    // If list contains non-integer, error
    if (list.includes("Else")) {
        canSubmit = false;
        wallet_holder.classList.add("active");
        error_msg.classList.add("active");
    }
    else {
        canSubmit = true;
        wallet_holder.classList.remove("active");
        error_msg.classList.remove("active");
    }
});


wallet_form.addEventListener("submit", function(event) {
    
    if (!canSubmit) {
        event.preventDefault();
    }

});