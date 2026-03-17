$(document).ready(function () {
    var $window = $(window);
    var $back = $('.layer-back');
    var $front = $('.layer-front');

    $window.on('scroll', function () {
        var scrollTop = $window.scrollTop();

        // дальний фон двигается медленнее
        var backOffset = scrollTop * 0.2;
        // ближний слой — чуть быстрее
        var frontOffset = scrollTop * 0.4;

        $back.css('transform', 'translateY(' + backOffset + 'px)');
        $front.css('transform', 'translateY(' + frontOffset + 'px)');
    });
});
