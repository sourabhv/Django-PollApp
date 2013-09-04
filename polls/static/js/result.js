(function($) {
	var $choices = $('#result').children('div');
	var total_votes = 0;
	$choices.each( function () {
		total_votes += $(this).data('votes');
	});

	$choices.each( function () {
		var ratio = ( $(this).data('votes') * 100.0 ) / total_votes;
		$(this).children('.meter').css('width', ratio + '%');
	});

})(jQuery);