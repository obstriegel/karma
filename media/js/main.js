// IE HTML5 fixes
document.createElement('header');
document.createElement('nav');
document.createElement('article');
document.createElement('section');
document.createElement('footer');

jQuery.postJSON = function(url, data, callback) { jQuery.post(url, data, callback, 'json'); };

jQuery(document).ready(function() {

});
