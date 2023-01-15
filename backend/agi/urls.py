# --------------------------------------------------------------
# Django  imports
# --------------------------------------------------------------
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls', namespace="core")),
    path('', include('users.urls', namespace="users")),
   
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += [path("__debug__/", include('debug_toolbar.urls')),]


admin.site.site_header  =  "AGI demo (admin)"  
admin.site.site_title  =  "AGI demo"
admin.site.index_title  =  "AGI demo"