function setCookie(key, value) {
    var expires = new Date();
    expires.setTime(expires.getTime() + (1 * 24 * 60 * 60 * 1000));
    document.cookie = key + '=' + value + ';expires=' + expires.toUTCString();
}

function getCookie(key) {
    var keyValue = document.cookie.match('(^|;) ?' + key + '=([^;]*)(;|$)');
    return keyValue ? keyValue[2] : null;
}


$(document).ready(function(){

    // Remove header when someone clicks on it.

    if (getCookie('disclaimer') == null) {
        $('#disclaimer-button').on('click', function(){
            $('#disclaimer').slideUp("normal", function() { $(this).remove(); } );
            setCookie('disclaimer','0');
        });
    }
    else if (getCookie('disclaimer') == 0) {
        $('#disclaimer').addClass('hidden');
    }




});