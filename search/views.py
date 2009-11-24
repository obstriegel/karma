from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.db.models import Q

from item.models import *

def api_search(request):
	if request.method == 'POST':
		data = request.POST['search']
		hits = Item.objects.all()
		for word in data.split():
			hits = hits & Item.objects.filter(
				Q(name__icontains=word) | Q(description__icontains=word)
			)
		if hits:
			return render_to_response(
				'search/result.html', {'hits': hits},
				context_instance=RequestContext(request)
			)
		else:
			return HttpResponse('No items')
	else:
		return HttpResponse('Error')
