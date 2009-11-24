from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.utils import simplejson
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout

def logout(request):
	from django.contrib.auth import logout
	logout(request)
	return HttpResponseRedirect(reverse('index'))

def api_login(request):

	def noerror():
		return HttpResponse(simplejson.dumps({}), mimetype='application/json')
	def error(err):
		return HttpResponse(simplejson.dumps({'error':err}), mimetype='application/json')

	if request.method == 'POST':

		username = request.POST.get('username', '')
		password = request.POST.get('password', '')
		create   = request.POST.get('create', 'false')

		data = dict()

		if create == 'true':
			user = User.objects.create_user(username, '', password)
			user.save()
			return noerror()
		
		if username and password:
			user = authenticate(username=username, password=password)
			if user and user.is_active:
				login(request, user)
				return noerror()
			else:
				return error('auth')
				
		return error('unknown')

	else:
		raise Http404
