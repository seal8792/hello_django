from django.contrib import admin
from .models import Shop

@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'desc', 'address']
    list_display_links = ['name']
    search_fields = ['name']

    def desc(self, post):
        return post.content[:20] + '...'

