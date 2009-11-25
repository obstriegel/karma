from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from models import *
from forms import *

def view(request, id):
	item = get_object_or_404(Item, id=id)
	return render_to_response('item/view.html', {'item': item}, context_instance=RequestContext(request))

def add(request):
	form = ItemAddForm(auto_id='id_item_%s')
	return render_to_response('item/add.html', {'form': form}, context_instance=RequestContext(request))

from django.utils import simplejson

def api_add(request):

	def noerror():
		return HttpResponse(simplejson.dumps({}), mimetype='application/json')
	def error(err):
		return HttpResponse(simplejson.dumps({'error':err}), mimetype='application/json')

	if request.method == 'POST':

		if request.user.is_authenticated():
			name = request.POST.get('name', '')
			desc = request.POST.get('description', '')
			if name:
				Item(user=request.user, name=name, description=desc).save()
				return noerror()
		else:
			return error('auth')

	else:
		raise Http404
