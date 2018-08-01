function setCookie(key, value) {
    var expires = new Date();
    expires.setTime(expires.getTime() + (1 * 24 * 60 * 60 * 1000));
    document.cookie = key + '=' + value + ';expires=' + expires.toUTCString();
}

function getCookie(key) {
    var keyValue = document.cookie.match('(^|;) ?' + key + '=([^;]*)(;|$)');
    return keyValue ? keyValue[2] : null;
}

// replace non-existent images with generic one
function imgError(image) {
    image.onerror = "";
    image.src = "https://openclassrooms-student-center.github.io/alumnis/images/oc-logo.svg";
    return true;
}

$(document).ready(function () {

    // Remove header when someone clicks on it.

    if (getCookie('disclaimer') == null) {
        $('#disclaimer-button').on('click', function () {
            $('#disclaimer').slideUp("normal", function () {
                $(this).remove();
            });
            setCookie('disclaimer', '0');
        });
    }
    else if (getCookie('disclaimer') == 0) {
        $('#disclaimer').addClass('hidden');
    }


});


// pagination system
var studentsRowsPerPage = 5;
var currentPage = 0;
var studentRows;


// hide and display students rows
function displayOrHideElements(firstElt, lastElt) {
    studentRows.css("display", "none");
    studentRows.slice(firstElt, lastElt).css("display", "block")
}

// define new current page and go to this page
function goToPage(page) {
    var firstElt = (studentsRowsPerPage * page);
    var lastElt = firstElt + studentsRowsPerPage;
    displayOrHideElements(firstElt, lastElt);
    currentPage = page;
    $(".page_link").removeClass("active");
    $("#id" + page).addClass("active");
}

// go to the previous page if current page is not the first one
function goToPrevious() {
    if (currentPage > 0) {
        goToPage(currentPage - 1);
    }
}

// go to next page if current page is not the last one
function goToNext() {
    studentRows = $(".students-row");
    var nbPages = Math.ceil(studentRows.length / studentsRowsPerPage);
    if (currentPage < nbPages) {
        goToPage(currentPage + 1);
    }
}


// create pagination after page load and do the pagination job for first current page
$(document).ready(function () {
    studentRows = $(".students-row");
    var nbPages = Math.ceil(studentRows.length / studentsRowsPerPage);

    var nav = '<li><a href=\"javascript:goToPrevious();\">&laquo;</a></li>';
    for (var i = 0; nbPages > i; i++) {
        nav += '<li id="id' + i + '" class="page_link';
        if (i === currentPage) {
            nav += ' active';
        }
        nav += '"><a href="javascript:goToPage(' + i + ')" >' + (i + 1) + '</a></li>';
    }
    nav += '<li><a href=\"javascript:goToNext();\">&raquo;</a></li>';
    $('.pagination').html(nav);
    goToPage(currentPage);
});

