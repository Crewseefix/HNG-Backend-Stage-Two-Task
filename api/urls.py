from django.urls import path, re_path
from api import views
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

app_name = 'api'

urlpatterns = [
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('schema/docs/', SpectacularSwaggerView.as_view(url_name='api:schema')),
    path('', views.CreateEndpoint.as_view(), name='Create'),
    re_path(r'(?P<user_id>[^/]+)/?$', views.RUDEndpoint.as_view(), name='RUD'),
]
