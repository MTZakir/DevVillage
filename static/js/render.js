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

function dropDownClick() {
    const $dropdown = $(".dropdown");
    const $tilted_container = $(".tilted-container");
    const $icon = $(".icon");

    $icon.on("click", function() {
        if ($dropdown.hasClass("active")) {
            $dropdown.removeClass("active");
            $dropdown.css("display", "none");
            $tilted_container.removeClass("active");
            $tilted_container.css('display', 'none')
        } else {
            $dropdown.addClass("active");
            $dropdown.css("display", "flex");
            $tilted_container.addClass("active");
            $tilted_container.css('display', 'block')
        }
    });

    $(document).on("click", function(event) {
        if (!($dropdown.is(event.target) || $dropdown.has(event.target).length || $icon.is(event.target) || $icon.has(event.target).length)) {
            $dropdown.css('display', 'none')
            $dropdown.removeClass("active");
            $tilted_container.removeClass("active");
            $tilted_container.css('display', 'none')
        }
    });
}

function statusColor(){
    $('.status').each(function() {
        var status = $(this).text().trim();
        if (status === 'Completed') {
            // Set the color of the text to green for completed status
            $(this).css('color', '#1A7229');
            $(this).css('font-size', '1.042vw');
            $(this).css('font-weight', '300');
        } else if (status === 'Ongoing') {
            // Set the color of the text to the specified rgba color for ongoing status
            $(this).css('color', 'rgba(255, 255, 255, 0.70)');
            $(this).css('font-size', '1.042vw');
            $(this).css('font-weight', '300');
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
    dropDownClick();
    statusColor();
    $('#bttnconf').css('background-color', '#733DF0');
});

document.addEventListener("DOMContentLoaded", function() {
    //handling of different navbar urls
    const currentURL = window.location.pathname;

    const contrcthstrybtn = document.querySelector(".contract-history-btn button")
    const contrcthstryspan = document.querySelector(".contract-history-btn span")
    
    const reviewbtn = document.querySelector(".review-btn button")
    const reviewspan = document.querySelector(".review-btn span")

    const contrcthstrycont = document.querySelector(".contrct-cards-container")
    const reviewcont = document.querySelector(".review-cards-container")

    const cardCont = document.querySelectorAll(".cards-container")
    const card = document.querySelectorAll(".cards")

    const expertList = document.querySelectorAll(".expertise-and-about ul li");
    const about = document.querySelector(".expertise-and-about p");
    const expandExpt = document.querySelector(".see-more-expertise");
    const expandAbout = document.querySelector(".see-more-about");
    const exprt_expand_icon = document.querySelector(".see-more-expertise .bi-chevron-down");
    const about_expand_icon = document.querySelector(".see-more-about .bi-chevron-down");
    
    if (contrcthstrybtn && contrcthstrybtn.classList) {
        contrcthstrybtn.classList.add("active");
    }

    if (contrcthstryspan && contrcthstryspan.classList) {
        contrcthstryspan.classList.add("active");
    }

    if (currentURL === "/acc_info/profile/individual") {
        //handling long list of expertise
        const expert_list_length = expertList.length;
        let isExpandedExprt = false;
        if (expertList.length <= 3) {
            expandExpt.style.display = "none";
        }
        else{
            for (let i = 3; i < expertList.length; i++) {
                expertList[i].style.display = 'none';
            }
        }

        expandExpt.addEventListener('click', () => {
            isExpandedExprt = !isExpandedExprt;
            if (isExpandedExprt) {
                for (let i = 3; i < expertList.length; i++) {
                    expertList[i].style.display = 'block';
                }
                exprt_expand_icon.classList.replace("bi-chevron-down", "bi-chevron-up");
            }
            else {
                for (let i = 3; i < expertList.length; i++) {
                    expertList[i].style.display = 'none';
                }
                exprt_expand_icon.classList.replace("bi-chevron-up", "bi-chevron-down");
            }
        });

        //handling large about test
        const about_text = about.textContent;

        let isExpandedAbout = false;

        if (about_text.length < 800) {
            expandAbout.style.display = "none";
        }
        else{
            // if the text content length exceeds 800 characters, replace with elilipsis

            about.textContent = about_text.slice(0, 730) + '...';

            console.log(about.textContent);
        }

        expandAbout.addEventListener('click', () => {
            isExpandedAbout = !isExpandedAbout;
            if (isExpandedAbout) {
                about.textContent = about_text;
                about_expand_icon.classList.replace("bi-chevron-down", "bi-chevron-up");
            }
            else {
                about.textContent = about_text.slice(0, 730) + '...';
                about_expand_icon.classList.replace("bi-chevron-up", "bi-chevron-down");
            }
        });

        //handling the scroll functionality of contract/review card containers
        const scrollLeftBtn = document.getElementById('scroll-left');
        const scrollRightBtn = document.getElementById('scroll-right');

        scrollLeftBtn.addEventListener('click', () => {
            contrcthstrycont.scrollBy({ left: -500, behavior: 'smooth' });
            reviewcont.scrollBy({ left: -572, behavior: 'smooth' });
        });

        scrollRightBtn.addEventListener('click', () => {
            contrcthstrycont.scrollBy({ left: 500, behavior: 'smooth' });
            reviewcont.scrollBy({ left: 572, behavior: 'smooth' });
        });

        //drag scroll implementation
        let isDown = false;
        let startX;
        let scrollLeft;
        let timer;

        cardCont.forEach(function(container) {

            container.addEventListener('mousedown', (e) => {
                isDown = true;
                scrollLeft = container.scrollLeft;
                startX = e.pageX;
                // e.preventDefault();
            });
        
            window.addEventListener('mouseup', () => {
                isDown = false;
                container.classList.remove('active')
                card.forEach(function(card) {
                    card.style.cursor = 'pointer';
                    card.style.pointerEvents  = 'auto';
                });
            });
            
            window.addEventListener('mouseleave', () => {
                isDown = false;
                container.classList.remove('active')
                card.forEach(function(card) {
                    card.style.cursor = 'pointer';
                    card.style.pointerEvents  = 'auto';
                });
            });

            window.addEventListener('mousemove', (e) => {
                if (!isDown) return;
                container.classList.add('active')

                card.forEach(function(card) {
                    card.style.cursor = 'grabbing';
                    card.style.pointerEvents  = 'none';
                });
                
                e.preventDefault();
            
                const x = e.pageX;
                const offset_from_initial_click = (x - startX) * 2;
            
                container.scrollLeft = scrollLeft - offset_from_initial_click;
            });
        });

        //handling button toggle between contract history and review buttons
        contrcthstrybtn.addEventListener("mouseover", () => {
            contrcthstryspan.classList.add('hovered');
        });
        
        contrcthstrybtn.addEventListener("mouseout", () => {
            contrcthstryspan.classList.remove('hovered');
        });

        reviewbtn.addEventListener("mouseover", () => {
            reviewspan.classList.add('hovered');
        });
        
        reviewbtn.addEventListener("mouseout", () => {
            reviewspan.classList.remove('hovered');
        });

        contrcthstrybtn.addEventListener("click", () => {
            contrcthstrybtn.classList.add("active");
            contrcthstryspan.classList.add("active");
            reviewbtn.classList.remove("active");
            reviewspan.classList.remove("active");

            contrcthstrycont.style.display = "flex";
            reviewcont.style.display = "none";
        });

        reviewbtn.addEventListener("click", () => {
            contrcthstrybtn.classList.remove("active");
            contrcthstryspan.classList.remove("active");
            reviewbtn.classList.add("active");
            reviewspan.classList.add("active");

            reviewcont.style.display = "flex";
            contrcthstrycont.style.display = "none";
        });
    }

    var url = window.location.href;
    var rootStyles = getComputedStyle(document.documentElement);
    
    if (url.includes("comp") || url.includes("org")) {
        document.documentElement.style.setProperty("--color", '#0276FA');
        document.documentElement.style.setProperty("--alt-color", '#733DF0');
        document.documentElement.style.setProperty("--hover-color", '#7e47ff');
        document.documentElement.style.setProperty("--hover-alt", '#2880ed');
    } else {
        document.documentElement.style.setProperty("--color", '#733DF0');
        document.documentElement.style.setProperty("--alt-color", '#0276FA');
        document.documentElement.style.setProperty("--hover-color", '#2880ed');
        document.documentElement.style.setProperty("--hover-alt", '#7e47ff');
    }
    
    const primaryColor = rootStyles.getPropertyValue('--color');
    console.log(currentURL);
    if (currentURL === "/discover/individual" || currentURL === "/discover/companies") {
        const discover_nav_option = document.querySelector(".discover-nav-option");
        discover_nav_option.style.color = primaryColor;
    }
    
    if (currentURL === "/dashboard/individual") {
        const discover_nav_option = document.querySelector(".dashboard-nav-option");
        discover_nav_option.style.color = primaryColor;
    }
});