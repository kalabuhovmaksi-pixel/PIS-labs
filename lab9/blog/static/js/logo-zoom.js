$(document).ready(function () {
    var originalWidth = $('#logo').width();

    $('#logo').hover(
        function () {
            $('#logo').stop().animate(
                { width: originalWidth + 20 },
                200
            );
        },
        function () {
            $('#logo').stop().animate(
                { width: originalWidth },
                200
            );
        }
    );
});
