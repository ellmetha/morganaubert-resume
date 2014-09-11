// Collapse the navbar on scroll
$(window).scroll(function() {
    if ($('.navbar').offset().top > 50) {
        $('.navbar-fixed-top').addClass('top-nav-collapse');
    } else {
        $('.navbar-fixed-top').removeClass('top-nav-collapse');
    }
});

// jQuery for page scrolling feature - requires jQuery Easing plugin
$(function() {
    $('a.goto').click(function(ev) {
        var anchor_id = $(this).attr('href');
        $('html, body').stop().animate({
            scrollTop: $(anchor_id).offset().top
        }, 1500, 'easeInOutExpo');

        ev.preventDefault();
    });
});
