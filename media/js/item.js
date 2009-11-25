jQuery(document).ready(function() {

	// If path is url of add
	if(window.location.pathname == '/item/add/') {
		
		// Focus on search input 
		jQuery('#id_item_add_form #id_name').focus();
		
		jQuery('#id_item_add_form #id_item_name').addClass('text ui-widget-content ui-corner-all');
		jQuery('#id_item_add_form #id_item_description').addClass('text ui-widget-content ui-corner-all');
		jQuery('#id_item_add_form #id_item_add_submit').addClass('ui-widget-content ui-corner-all');
	}

	jQuery('#id_item_add_submit').click(function() {

		// Get input values
		name = jQuery('#id_item_add_form #id_item_name').attr('value');
		desc = jQuery('#id_item_add_form #id_item_description').attr('value');
		
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
