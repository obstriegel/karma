from django import forms

from models import *

class ItemAddForm(forms.ModelForm):
	class Meta:
		model = Item
		exclude = ('user',)