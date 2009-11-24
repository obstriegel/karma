from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

class Item(models.Model):

	user = models.ForeignKey(User, verbose_name=_('user'))

	name = models.CharField(_('name'), max_length=200)
	description = models.TextField(_('description'), default='', blank=True)
	
	def __unicode__(self):
		return self.name
		
	class Meta:
		verbose_name = _(u'item')
		verbose_name_plural = _(u'items')
		
	def in_categories(self):
		return ', '.join([unicode(c) for c in self.category_set.all()])

class Category(models.Model):
	name = models.CharField(_('name'), max_length=100)
	parent = models.ForeignKey('self', verbose_name=_('parent'), null=True, blank=True)
	items = models.ManyToManyField(Item, through='CategoryItems', verbose_name=_('items'), null=True, blank=True)
	
	def __unicode__(self):
		def __recurse(node):
			result = node.name
			if node.parent:	result = __recurse(node.parent) + '>%s' % result
			return result
		return __recurse(self)
		
	class Meta:
		verbose_name = _(u'category')
		verbose_name_plural = _(u'categories')
	
class CategoryItems(models.Model):
	item = models.ForeignKey(Item)
	category = models.ForeignKey(Category)

	def __unicode__(self):
		return u'Item in category'

	@models.permalink
	def get_absolute_url(self):
		return ('item', (self.id,))
		
	class Meta:
		verbose_name = _(u'item in category')
		verbose_name_plural = _(u'item in categories')
