jQuery(document).ready(function() {

	// Disable autocomplete
	jQuery('#id_search_search_input').attr('autocomplete', 'off');

	// Focus on search input if path is /
	if(window.location.pathname == '/') jQuery('#id_search_search_input').focus();

	// Catch keyup on search input
	jQuery('#id_search_search_input').keyup(function() {

		// Get search input value
		search = $(this).attr('value');

		// Clear result and return
		// if length of input is less than three characters
		if(search.length < 3) {
			jQuery('#id_search_result').html('');
			return;
		}

		// Send value in search input to ajax search and print result
		jQuery.post('/search/api/search/', {search: search}, function(data, textStatus) {
			if(textStatus == 'success')
				jQuery('#id_search_result').html(data);
			else
				jQuery('#id_search_result').html('error!');
		});
	});
});
