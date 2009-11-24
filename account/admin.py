from django.contrib import admin
from models import *

class UserProfileAdmin(admin.ModelAdmin):
	pass

admin.site.register(UserProfile, UserProfileAdmin)

class LocationAdmin(admin.ModelAdmin):
	pass

admin.site.register(Location, LocationAdmin)
