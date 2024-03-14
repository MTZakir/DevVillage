function setColor(){
    var url = window.location.href;
    
    if (url.includes("homecomp")){
        $(":root").css("--color", '#0276FA');
    }
    
    else{
        $(":root").css("--color", '#733DF0');
    }
}

$(document).ready(function() {
    setColor();
});