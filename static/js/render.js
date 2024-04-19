function setColor(){
    var url = window.location.href;
    
    if (url.includes("comp") || url.includes("org")){
        $(":root").css("--color", '#0276FA');
        $(":root").css("--alt-color", '#733DF0');
        $(":root").css("--hover-color", '#7e47ff');
        $(":root").css("--hover-alt", '#2880ed');
    }
    
    else{
        $(":root").css("--color", '#733DF0');
        $(":root").css("--alt-color", '#0276FA');
        $(":root").css("--hover-color", '#2880ed');
        $(":root").css("--hover-alt", '#7e47ff');
    }
}

function ratingCalc(){
    $('.Stars').each(function() {
        var ratingValue = parseFloat($(this).data('rating'));
        $(this).css("--rating", ratingValue);
    });
}

function confColor(){
    $("#organization, .confcard:eq(0)").on("click", function() {
        $(":root").css("--color-conf", "#0276FA");
        $("#leftimg").fadeOut(200, function(){
            $("#leftimg").attr("src", "static/images/homecomp.jpg").fadeIn(200)
        })
        $('.confcard:eq(0)').css('border' ,'1px solid var(--color-conf)')
        $('.confcard:eq(0) p').css('color' ,'var(--color-conf)'); 
        $('.confcard:eq(0) .logo').css('color', 'var(--color-conf)');
        $('.confcard:eq(1) p').css('color' ,'#fff'); 
        $('.confcard:eq(1)').css('border' ,'1px solid #0f0f0f'); 
        $('.confcard:eq(1) .logo').css('color', '#fff');
        updateButtonState();
    });
    
    $("#individual, .confcard:eq(1)").on("click", function() {
        $(":root").css("--color-conf", "#733DF0");
        $("#leftimg").fadeOut(200, function(){
            $("#leftimg").attr("src", "static/images/homepage1.jpg").fadeIn(200)
        })
        $('.confcard:eq(1)').css('border' ,'1px solid var(--color-conf)')
        $('.confcard:eq(1) p').css('color' ,'var(--color-conf)'); 
        $('.confcard:eq(1) .logo').css('color', 'var(--color-conf)');
        $('.confcard:eq(0) p').css('color' ,'#fff'); 
        $('.confcard:eq(0)').css('border' ,'1px solid #0f0f0f'); 
        $('.confcard:eq(0) .logo').css('color', '#fff');
        updateButtonState();
    });
}

function redirect() {
    if ($("#organization").is(":checked")) {
        $('#bttnconf').off('click').on('click', function() {
            window.location.href = orgRegisterUrl;
        });
    } 
    
    else if ($('#individual').is(":checked")) {
        $('#bttnconf').off('click').on('click', function() {
            window.location.href = userRegisterUrl;
        });
    }
}

function checkRadio(id){
    $(id).prop('checked', true);
    redirect();
}

function updateButtonState() {
    if ($('input[name="confirmation"]:checked').length > 0) {
        $('#bttnconf').prop('disabled', false);
        $('#bttnconf').css('background-color', 'var(--color-conf)')
    } 
    
    else {
        $('#bttnconf').prop('disabled', true);
    }
}

function submitForm(){
    var otp = "";
    $("#verify-bttn").click(function(){
        $('.otpfield').each(function(){
            otp += $(this).val();
        })
        $('#combinedotp').val(otp);
        $("#submit-form").submit();
    })
}

function otpfields(){
    $('.otpfield:not(:first)').prop('disabled', true);

    $('.otpfield').keyup(function(e) {
        var key = e.keyCode || e.which;
        var maxLength = parseInt($(this).attr('maxlength'));
        var currentLength = $(this).val().length;

        // If a number is entered and the field is full, move focus to the next field
        if (((key >= 48 && key <= 57) || (key >= 96 && key <= 105)) && currentLength >= maxLength) {
            $(this).next('.otpfield').prop('disabled', false).focus();
        }
        // If backspace is pressed and the field is empty, move focus to the previous field
        else if (key == 8 && currentLength == 0) {
            $(this).prev('.otpfield').prop('disabled', false).focus();
        }

        // Disable next fields if the current field is empty
        if (currentLength === 0) {
            $(this).nextAll('.otpfield').prop('disabled', true).val('');
        }
    });
}

$(document).ready(function() {
    setColor();
    ratingCalc();
    confColor();
    redirect();
    otpfields();
    submitForm();
    $('#bttnconf').css('background-color', '#733DF0');
});

const dropdown = document.querySelector(".dropdown")
const tilted_container = document.querySelector(".tilted-container")
const icon = document.querySelector(".icon")

icon.addEventListener("click", function(event){
    dropdown.classList.add("active");
    tilted_container.classList.add("active");
});

document.addEventListener("click", function(event){
    if (!dropdown.contains(event.target) && !icon.contains(event.target)){
        dropdown.classList.remove("active");
        tilted_container.classList.remove("active");
    }
})