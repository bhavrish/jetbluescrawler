"""jetBlueWebApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf import settings
#from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
import home.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home.views.home, name='home'),
    path('availabilitybad', home.views.availabilitybad, name='availabilitybad'),
    path('availabilitygood', home.views.availabilitygood, name='availabilitygood'),
    path('costbad', home.views.costbad, name='costbad'),
    path('costgood', home.views.costgood, name='costgood'),
    path('legroombad', home.views.legroombad, name='legroombad'),
    path('legroomgood', home.views.legroomgood, name='legroomgood'),
    path('timelinessbad', home.views.timelinessbad, name='timelinessbad'),
    path('timelinessgood', home.views.timelinessgood, name='timelinessgood'),
    path('americanavailabilitybad', home.views.americanavailabilitybad, name='americanavailabilitybad'),
    path('americanavailabilitygood', home.views.americanavailabilitygood, name='americanavailabilitygood'),
    path('americancostbad', home.views.americancostbad, name='americancostbad'),
    path('americancostgood', home.views.americancostgood, name='americancostgood'),
    path('americanlegroombad', home.views.americanlegroombad, name='americanlegroombad'),
    path('americanlegroomgood', home.views.americanlegroomgood, name='americanlegroomgood'),
    path('americantimelinessbad', home.views.americantimelinessbad, name='americantimelinessbad'),
    path('americantimelinessgood', home.views.americantimelinessgood, name='americantimelinessgood'),
    path('unitedavailabilitybad', home.views.unitedavailabilitybad, name='unitedavailabilitybad'),
    path('unitedavailabilitygood', home.views.unitedavailabilitygood, name='unitedavailabilitygood'),
    path('unitedcostbad', home.views.unitedcostbad, name='unitedcostbad'),
    path('unitedcostgood', home.views.unitedcostgood, name='unitedcostgood'),
    path('unitedlegroombad', home.views.unitedlegroombad, name='unitedlegroombad'),
    path('unitedlegroomgood', home.views.unitedlegroomgood, name='unitedlegroomgood'),
    path('unitedtimelinessbad', home.views.unitedtimelinessbad, name='unitedtimelinessbad'),
    path('unitedtimelinessgood', home.views.unitedtimelinessgood, name='unitedtimelinessgood'),
    path('spiritavailabilitybad', home.views.spiritavailabilitybad, name='spiritavailabilitybad'),
    path('spiritavailabilitygood', home.views.spiritavailabilitygood, name='spiritavailabilitygood'),
    path('spiritcostbad', home.views.spiritcostbad, name='spiritcostbad'),
    path('spiritcostgood', home.views.spiritcostgood, name='spiritcostgood'),
    path('spiritlegroombad', home.views.spiritlegroombad, name='spiritlegroombad'),
    path('spiritlegroomgood', home.views.spiritlegroomgood, name='spiritlegroomgood'),
    path('spirittimelinessbad', home.views.spirittimelinessbad, name='spirittimelinessbad'),
    path('spirittimelinessgood', home.views.spirittimelinessgood, name='spirittimelinessgood'),
    path('react', home.views.react, name='react'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
