
from django.contrib import admin
from rest_framework.authtoken.views import obtain_auth_token
from core.views import obtain_api_token
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('api/key', obtain_api_token, name='view_api'),
    path('api/', include('news.urls')),
]
