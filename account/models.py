from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

class UserProfile(models.Model):
	
	user = models.ForeignKey(User, verbose_name=_('user'))
	
	phone = models.IntegerField(_(u'phone'), null=True, blank=True)

	class Meta:
		verbose_name = _(u'user profile')
		verbose_name_plural = _(u'user profiles')
	
	def __unicode__(self):
		return unicode(self.user)
	
class Location(models.Model):
	
	user = models.ForeignKey(User, verbose_name=_('user'))
	
	address1 = models.CharField(_(u'address1'), max_length=64, default='', blank=True)
	address2 = models.CharField(_(u'address2'), max_length=64, default='', blank=True)
	zipcode  = models.IntegerField(_(u'zipcode'), null=True, blank=True)
	city     = models.CharField(_(u'city'), max_length=32, default='', blank=True)
	country  = models.CharField(_(u'country'), max_length=32)
	
	phone = models.IntegerField(_(u'phone'), null=True, blank=True)
	
	class Meta:
		verbose_name = _(u'location')
		verbose_name_plural = _(u'locations')

	def __unicode__(self):
		return u'Location'