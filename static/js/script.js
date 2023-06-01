$(document).ready(function () {
    let windowWidth = $(window).width();

    // init dropdown
    let dropdown = new bootstrap.Dropdown(document.querySelector('.dropdown-toggle'))

    hideShowNavbar(windowWidth, dropdown);
    fixDaysCounterPosition(windowWidth);

    // restart functions on windows resize
    $(window).resize(function () {
        windowWidth = $(window).width();
        hideShowNavbar(windowWidth, dropdown);
        fixDaysCounterPosition(windowWidth);
    });
});


/**
 * - Hide/show navbar on scroll up/down if screen width is less than 768px.
 * - Hide dropdown menu on scroll down.
 *
 * Based on the following example:
 * https://bootstrap-menu.com/_bootstrap4/detail-smart-hide.html
 */
function hideShowNavbar(windowWidth, dropdown) {

    // if width is less than 768px activate smart scroll
    if (windowWidth < 768) {
        // add smart scroll that fixes the navbar
        $('.navbar').addClass('smart-scroll');
        // add padding top to show content behind navbar
        $('body').css('padding-top', $('.navbar').outerHeight() + 'px')
        let last_scroll_top = 0;

        // add scroll event handler that detects scroll up/down
        $(window).on('scroll', function () {
            let scroll_top = $(this).scrollTop();
            if (scroll_top < last_scroll_top) {
                $('.smart-scroll').removeClass('scrolled-down').addClass('scrolled-up');
            }
            else {
                // add scrolled-down class that hides the navbar
                $('.smart-scroll').removeClass('scrolled-up').addClass('scrolled-down');
                // hide dropdown menu if it is open
                dropdown.hide();
            }
            last_scroll_top = scroll_top;
        });
    } else {
        $('.smart-scroll').removeClass('scrolled-up').removeClass('scrolled-down');
        // remove scroll event handler for screens larger than 768px
        $(window).off('scroll');
        // remove smart scroll that fixes the navbar
        $('.navbar').removeClass('smart-scroll');
        // remove padding top from body
        $('body').css('padding-top', '0');
    }
}

/**
 * Fix absolute position of days counter on screens larger than 400px.
 * Days counter is located on every card.
 */
function fixDaysCounterPosition(windowWidth) {
    if (windowWidth > 440) {
        $('.days-counter').removeClass('card-subtitle').addClass('position-absolute top-0 end-0 pt-2 pe-3')
    } else {
        $('.days-counter').removeClass('position-absolute top-0 end-0 pt-2 pe-3').addClass('card-subtitle')
    }
}
