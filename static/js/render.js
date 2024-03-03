$(document).ready(function(){
    let comp = $("#img-comp, #navbar-comp, #mainexp-comp, .socials"); 
    let ind = $("#img-ind, #navbar-ind, #mainexp-ind, .socials");
    comp.hide();
    $(".socials").show();

    $("#forCompanies").on("click", function(){
        ind.hide();
        ind.removeClass("fadeinanimation");
        comp.addClass("fadeinanimation");
        comp.show();
        document.documentElement.style.setProperty('--color', '#0276FA');
    })
    $("#forIndividuals").on("click", function(){
        comp.hide();
        comp.removeClass("fadeinanimation");
        ind.addClass("fadeinanimation");
        $(":root").css("--color", "#733DF0")
        ind.show();
        document.documentElement.style.setProperty('--main-color', '#733DF0');
    })
})