"""
URL configuration for prj_hp project.

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
from django.urls import path
from app_hp.views import test, img_brand, home, cont, lthome, ie, txhome, achi, orgs
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test', test),
    path('images/brand', img_brand),
    path('', home),
    path('contact', cont),
    path('lt-home', lthome),
    path('Indo-European', ie),
    path('tx-home', txhome),
    path('achievements', achi),
    path('organizations', orgs)
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
