function myFunction(x) {
  if (x.matches) { // If media query matches
    console.log('Small Media Screen Detected');
    if ($('#sidebarCollapse').find('[data-fa-i2svg]').hasClass('fa-angle-double-left')) {
      $('#sidebarCollapse').find('[data-fa-i2svg]').toggleClass('fa-angle-double-right')
    }
  } else {
    console.log('Large Media Screen Detected');
    if ($('#sidebarCollapse').find('[data-fa-i2svg]').hasClass('fa-angle-double-right')) {
      $('#sidebarCollapse').find('[data-fa-i2svg]').toggleClass('fa-angle-double-left')
    }
  }
}

$(document).ready(function () {

    $("#sidebar").mCustomScrollbar({
        theme: "minimal"
    });

      $('#sidebarCollapse').on('click', function () {
        // toggle fontawesome icon
        console.log('click');
        // console.log($(this).find('[data-fa-i2svg]').first().val())
        $(this)
             .find('[data-fa-i2svg]')
             .toggleClass('fa-angle-double-right')
             .toggleClass('fa-angle-double-left');

        $('#sidebar, #content, #navbar-top').toggleClass('active');
        $('.collapse.in').toggleClass('in');
        $('a[aria-expanded=true]').attr('aria-expanded', 'false');
      });

      var x = window.matchMedia("(max-width: 768px)")
      myFunction(x) // Call listener function at run time
      x.addListener(myFunction) // Attach listener function on state changes

});
