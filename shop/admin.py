from django.contrib import admin
from .models import Shop, Item

@admin.register(Shop)             # 장식자 : @는 함수나 클래스를 wrapping 하는 기능
class ShopAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'desc', 'address']
    list_display_links = ['name']
    search_fields = ['name']

    # def desc(self, post):
    #     return post.desc[:20] + '...'

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'desc', 'price', 'is_public']
    list_display_links = ['name']
    search_fields = ['name']

    # def desc(self, desc):
    #     return desc.content[:20] + '...'
