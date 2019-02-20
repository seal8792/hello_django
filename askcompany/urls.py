from django.conf import settings
from django.http import HttpResponseRedirect
from django.contrib import admin
from django.urls import include, path

def root(request):
    return HttpResponseRedirect('/blog/')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('shop/', include('shop.urls')),
    path('', root),
]
if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
    