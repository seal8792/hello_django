from django.contrib import admin
from .models import Shop, Item

@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'desc', 'address']
    list_display_links = ['name']
    search_fields = ['name']

    def desc(self, post):
        return post.content[:20] + '...'

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'desc', 'price', 'is_public']
    list_display_link = ['name', 'price']
    search_fields = ['name']