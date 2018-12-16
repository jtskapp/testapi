$('#calendar').datepicker({
		});


// $(document).ready(function() {
// 	$('#toggle-menu').on('click', function () {
// 			console.log('toggled');
// 			// console.log($('#sidebar-collapse').hasClass('hide'));
// 			$('#sidebar-collapse').css('left','-250px');
// 			$('#main').css('left','-250px');
// 			});
// });

$(function () {
    $('#toggle-menu').on('click', function () {
			console.log($('#children').hasClass('collapse in'));
    // if ($('.navbar').is(':visible')) {
    //     $('.sidebar').animate({'width': '0px'}, 'slow', function () {
    //         $('.sidebar').hide();
    //     });
    //     $('.main-page').animate({'padding-left': '0px'}, 'slow');
    // } else {
    //     $('.sidebar').show();
    //     $('.sidebar').animate({'width': '240px'}, 'slow');
    //     $('.main-page').animate({'padding-left': '240px'}, 'slow');
    // }
    });
});


!function ($) {
    $(document).on("click","ul.nav li.parent > a ", function(){
			 	var elem = $(this).find('span');
				if (!elem.hasClass("collapsed")) {
					console.log('expanded');
					elem.find('svg').attr('data-icon', 'minus');
				} else {
					console.log('collapsed');
					elem.find('svg').attr('data-icon', 'plus');
				}
    });
}

(window.jQuery);
	$(window).on('resize', function () {

  if ($(window).width() > 768) {
		console.log('windows ' + $(window).width() + ' > 768');
		$('#sidebar-collapse').collapse('show');
	}
})

$(window).on('resize', function () {
  if ($(window).width() <= 767) {
		console.log('windows ' + $(window).width() + ' <= 767');
		$('#sidebar-collapse').collapse('hide');
	}
})


$(document).on('click', '.panel-heading span.clickable', function(e){
  var $this = $(this);
	if(!$this.hasClass('panel-collapsed')) {
		$this.parents('.panel').find('.panel-body').slideUp();
		$this.addClass('panel-collapsed');
		$this.find('em').removeClass('fa-toggle-up').addClass('fa-toggle-down');
	} else {
		$this.parents('.panel').find('.panel-body').slideDown();
		$this.removeClass('panel-collapsed');
		$this.find('em').removeClass('fa-toggle-down').addClass('fa-toggle-up');
	}
})
