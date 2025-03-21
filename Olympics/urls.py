"""
URL configuration for Olympics project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from Olympics.view import homepage_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('soldier/', include('soldier.urls')),
    path('homepage/', homepage_view, name='homepage'),
    path('api/', include('api.urls')),
    path('equipment/', include('equipment.urls')),
    path('statistic/', include('statistic.urls')),

    path('', include('tasks.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)