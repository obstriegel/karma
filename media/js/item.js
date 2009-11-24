jQuery(document).ready(function() {

	// Only focus on search input if path is url of add
	if(window.location.pathname == '/item/add/') jQuery('#id_item_add_form #id_name').focus();

	jQuery('#id_item_add_submit').click(function() {

		// Get input values
		name = jQuery('#id_name').attr('value');
		desc = jQuery('#id_description').attr('value');
		
		// Send value in add inputs to ajax add
		jQuery.postJSON('/item/api/add/', {name: name, description: desc},
		function(data, textStatus) {
			if(textStatus == 'success') {
				if(data.error == 'auth')
					account_login_show();
				else
					window.location = '/';
			} else
				alert('error!');
		});

		return false;
	});		
});
