function account_login() {
	
	// Get input values
	user = jQuery('#id_account_login_username').attr('value');
	pass = jQuery('#id_account_login_password').attr('value');

	// Send value in login inputs to ajax login
	jQuery.postJSON('/account/api/login/', { username: user, password: pass },
		function(data, textStatus) {
			if(textStatus == 'success') {
				if(data.error)
					jQuery('#id_account_login_dialog_message').html('Not found');
				else
					account_login_success();
			} else
				jQuery('#id_account_login_dialog_message').html('Unknown');
		});
}

function account_login_success() {
	//jQuery('#id_account_login_dialog').dialog('close');
	window.location.reload();
}

function account_login_show() {
	jQuery('#id_account_login_dialog').dialog('open');
}

jQuery(document).ready(function() {

	jQuery('#id_account_login_dialog').dialog({
		autoOpen: false,
		bgiframe: true,
		draggable: false,
		height: 300,
		modal: true,
		resizable: false,
		buttons: {
			'Login': function() {
				account_login();
			},
			Cancel: function() {
				$(this).dialog('close');
			}
		}
	});

	jQuery('#id_account_login_link').click(account_login_show);

	jQuery('#id_account_login_password').keydown(function(event) {
		if(event.keyCode == 13) {
			dlg = jQuery('#id_account_login_dialog');
			dlg.dialog('option', 'buttons')['Login'].apply(dlg);
		}
	});

})