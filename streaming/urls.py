"""
URL configuration for streaming project.

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
from django import views
from django.contrib import admin
from django.urls import path,include
from films.api.router import router_media,router_mediaviews,router_mediarating,router_mediarandom, router_mediaorder, router_mediafilter

urlpatterns = [
    path('admin/', admin.site.urls),
    path('films/',include('films.urls')),
    path('',include('authentication.urls')),

    path('api/media/',include(router_media.urls)),
    path('api/mediaviews/',include(router_mediaviews.urls)),
    path('api/mediarating/',include(router_mediarating.urls)),
    path('api/media/random/',include(router_mediarandom.urls)),
    path('api/media/order/',include(router_mediaorder.urls)),
    path('api/media/filter/',include(router_mediafilter.urls)),



]
