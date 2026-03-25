$(document).ready(function () {
    var $window = $(window);
    var $back = $('.layer-back');
    var $front = $('.layer-front');

    $window.on('scroll', function () {
        var scrollTop = $window.scrollTop();

        var backOffset = scrollTop * 0.2;
        var frontOffset = scrollTop * 0.4;

        $back.css('transform', 'translateY(' + backOffset + 'px)');
        $front.css('transform', 'translateY(' + frontOffset + 'px)');
    });
});
