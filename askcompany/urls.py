
from django.contrib import admin
from django.http import HttpResponseRedirect
from django.urls import include, path

def root(request):
    return HttpResponseRedirect('/blog/')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('shop/', include('shop.urls')),
    path('', root),
]
