from django.contrib import admin

from models import *

class CategoryItemsInline(admin.TabularInline):
	model = CategoryItems
	extra = 2
	
class ItemAdmin(admin.ModelAdmin):
	list_display = ('name', 'in_categories')
	inlines = (CategoryItemsInline,)

admin.site.register(Item, ItemAdmin)
	
class CategoryAdmin(admin.ModelAdmin):
	pass

admin.site.register(Category, CategoryAdmin)