"""
URL configuration for agro_hakaton project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view

# 42.87553136327577, 74.61888691483664

urlpatterns = [
    path('api_schema/', get_schema_view(title='API Schema'), name='schema_url'),
    path('swagger-ui/', TemplateView.as_view(
        template_name='swagger-ui.html',
        extra_context={'schema_url': 'openapi-schema'}
    ), name='swagger-ui'),
    path('admin/', admin.site.urls),
    path('api/users/', include('apps.users.urls')),
    path('api/place/', include('apps.place.urls')),
    path('api/admin_panel/', include('apps.admin_panel.urls')),
    path('api/reating/', include('apps.reating.urls')),
    path('api/transport/', include('apps.transport.urls')),
]
