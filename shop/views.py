from django.shortcuts import render
from .models import Shop

def index(request):
    # 전체 SHOP 목록을 가져올 예정임
    qs = Shop.objects.all()
    return render(request, 'shop/shop_list.html', {
        'shop_list':qs,
        })

def shop_detail(request, pk):
    shop = Shop.objects.get(pk=pk)
    return render(request, 'shop/shop_detail.hkml', {
        'shop' : shop,
    })
 