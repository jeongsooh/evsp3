"""
URL configuration for evsp2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

from dashboard.views import index, dashboard, logout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('logout/', logout),
    path('user/', include('user.urls')),
    path('dashboard/', dashboard),
    path('cpinfo/', include('cpinfo.urls')),
    path('cardinfo/', include('cardinfo.urls')),
    path('charginginfo/', include('charginginfo.urls')),
    path('ocpp/', include('ocpp.urls')),
    path('variables/', include('variables.urls')),
    path('clients/', include('clients.urls')),
]
