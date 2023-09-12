from django.contrib import admin
from django.urls import path, include, re_path
from api.views import handle_unknown_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^api/?', include(('api.urls', 'api'), namespace='api')),
    re_path(r'.*', handle_unknown_urls.as_view(), name='handle_unknown_urls'),
]
