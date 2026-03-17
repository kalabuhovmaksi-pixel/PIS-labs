$(document).ready(function () {
    $('.one-post').hover(
        function (event) {
            $(event.currentTarget)
                .find('.one-post-shadow')
                .stop()
                .animate({ opacity: 0.2 }, 300);
        },
        function (event) {
            $(event.currentTarget)
                .find('.one-post-shadow')
                .stop()
                .animate({ opacity: 0 }, 300);
        }
    );
});
