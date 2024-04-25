var token_form = document.getElementById("token_form");
var submit_btn = document.getElementById("buy");

submit_btn.addEventListener("click", function(event) {
    var confirmed = window.confirm("Are you sure you want to make this purchase?")

    if (confirmed) {
        token_form.submit();
    }
});