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

$(document).ready(function() {
    setColor();
    confColor();
    redirect();
    $('#bttnconf').prop('disabled', true);
    $('#bttnconf').css('background-color', '#733DF0');
});