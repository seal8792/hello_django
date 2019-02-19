from django.contrib import admin
from .models import Shop, Item

@admin.register(Shop)             # 장식자 : @는 함수나 클래스를 wrapping 하는 기능
class ShopAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'short_desc', 'address', 'created_at']
    list_display_links = ['name']
    search_fields = ['name']

    def short_desc(self, desc):
        return desc.desc[:20] + '...'

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'short_desc', 'shop', 'price', 'is_public']
    list_display_links = ['name']
    search_fields = ['name']

    def short_desc(self, desc):
        return desc.desc[:20] + '...'
