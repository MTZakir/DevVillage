var app_accept = document.getElementById("accept-btn");
var app_reject = document.getElementById("reject-btn");
var app_form = document.getElementById("app_form");
var app_form_input = document.getElementById("app_form_input");

app_accept.addEventListener("click", function() {
    var confirmed = window.confirm("Are you sure you want to accept this user? The payment for the first 15 days of this contract will be made to the user once accepted.")

    if (confirmed) {
        app_form_input.value += "-1";
        app_form.submit();
    }
});

app_reject.addEventListener("click", function() {
    var confirmed = window.confirm("Are you sure you want to reject this user?")

    if (confirmed) {
        app_form_input.value += "-0";
        app_form.submit();
    }
})