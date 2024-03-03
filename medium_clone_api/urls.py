from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title='Medium Clone API',
        default_version='v1',
        description='API endpoint for medium clone',
        contact=openapi.Contact(email='someemail@gmail.com'),
        license=openapi.License(name='MIT License'),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [

    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    path(settings.ADMIN_URL, admin.site.urls),
]

admin.site.site_header = 'Medium Clone API Admin'

admin.site.site_title = 'Medium Clone API Admin'

admin.site.index_title = 'Welcome to Medium Clone API'
