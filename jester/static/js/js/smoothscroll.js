jQuery(document).ready(function ($) {
    var section = $('.ck-section'),
        navigationItems = $('.ck-nav-wrapper a'),
        trigger = $('.ck-nav-trigger'),
        wrapper = $('.ck-nav-wrapper');
    updateNavigation();
    $(window).on('scroll', function () {
        event.preventDefault();
        updateNavigation();
    });

    //    smooth scroll to section
    navigationItems.on('click', function (event) {
        event.preventDefault();
        smoothScroll($(this.hash));
        wrapper.removeClass('move0');
        trigger.removeClass('move50');
        section.removeClass('move30');
    });
    //    smooth scroll to second section
    $('.cd-scroll-down').on('click', function (event) {
        event.preventDefault();
        smoothScroll($(this.hash));
    });
    function updateNavigation() {
        section.each(function () {
            $this = $(this);
            var activeSection = $('.ck-nav-wrapper a[href="#' + $this.attr('id') + '"]').data('number') - 1;
            if (($this.offset().top = $(window).height() / 2 < $(window).scrollTop() && ($this.height() - $(window).height() / 2 > $(window).scrollTop()))) {
                navigationItems.eq(activeSection).addClass('is-selected');
            } else {
                navigationItems.eq(activeSection).removeClass('is-selected');
            }

        }); 
    }

    function smoothScroll(target) {
        $('body,html').animate({
                'scrollTop': target.offset().top
            },
            600
        );
    }
});