from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('catalog/', include('apps.catalog.urls', namespace='catalog')),
    path('accounts/', include('apps.accounts.urls', namespace='accounts')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
