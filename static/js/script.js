$(document).ready(function () {
    var navbarHeight = $('#mainNavbar').outerHeight();
  
    $('#messages').css('top', navbarHeight + 'px');
  
    $('#mainNavbar').on('shown.bs.collapse', function () {
      var newNavbarHeight = $('#mainNavbar').outerHeight();
      $('#messages').css('top', newNavbarHeight + 'px');
    }).on('hidden.bs.collapse', function () {
      var newNavbarHeight = $('#mainNavbar').outerHeight();
      $('#messages').css('top', newNavbarHeight + 'px');
    });
  });

$(document).ready(function () {
    $('.alert').each(function () {
        var $alert = $(this);
        var countdown = $alert.find('.countdown');
        var timeLeft = parseInt(countdown.text());

        var timerId = setInterval(function () {
            timeLeft -= 1;
            countdown.text(timeLeft);

            if (timeLeft <= 0) {
                clearInterval(timerId);
                $alert.fadeOut('slow', function () {
                    $(this).remove();
                });
            }
        }, 1000);
    });
});
