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
    path('availability', home.views.availability, name='availability'),
    path('cost', home.views.cost, name='cost'),
    path('legroom', home.views.legroom, name='legroom'),
    path('timeliness', home.views.timeliness, name='timeliness'),
    path('hiddenFees', home.views.hiddenFees, name='hiddenFees'),
    path('baggageFees', home.views.baggageFees, name='baggageFees'),
    path('travelRewards', home.views.travelRewards, name='travelRewards'),
    path('reimbursement', home.views.reimbursement, name='reimbursement'),
    path('connections', home.views.connections, name='connections'),
    path('foodEntertainment', home.views.foodEntertainment, name='foodEntertainment'),
    path('service', home.views.service, name='service'),
    path('familyOptions', home.views.familyOptions, name='familyOptions'),
    path('americanAvailability', home.views.americanAvailability, name='americanAvailability'),
    path('americanCost', home.views.americanCost, name='americanCost'),
    path('americanLegroom', home.views.americanLegroom, name='americanLegroom'),
    path('americanTimeliness', home.views.americanTimeliness, name='americanTimeliness'),
    path('americanHiddenFees', home.views.americanHiddenFees, name='americanHiddenFees'),
    path('americanBaggageFees', home.views.americanBaggageFees, name='americanBaggageFees'),
    path('americanTravelRewards', home.views.americanTravelRewards, name='americanTravelRewards'),
    path('americanReimbursement', home.views.americanReimbursement, name='americanReimbursement'),
    path('americanConnections', home.views.americanConnections, name='americanConnections'),
    path('americanFoodEntertainment', home.views.americanFoodEntertainment, name='americanFoodEntertainment'),
    path('americanService', home.views.americanService, name='americanService'),
    path('americanFamilyOptions', home.views.americanFamilyOptions, name='americanFamilyOptions'),
    path('unitedAvailability', home.views.unitedAvailability, name='unitedAvailability'),
    path('unitedCost', home.views.unitedCost, name='unitedCost'),
    path('unitedLegroom', home.views.unitedLegroom, name='unitedLegroom'),
    path('unitedTimeliness', home.views.unitedTimeliness, name='unitedTimeliness'),
    path('unitedHiddenFees', home.views.unitedHiddenFees, name='unitedHiddenFees'),
    path('unitedBaggageFees', home.views.unitedBaggageFees, name='unitedBaggageFees'),
    path('unitedTravelRewards', home.views.unitedTravelRewards, name='unitedTravelRewards'),
    path('unitedReimbursement', home.views.unitedReimbursement, name='unitedReimbursement'),
    path('unitedConnections', home.views.unitedConnections, name='unitedConnections'),
    path('unitedFoodEntertainment', home.views.unitedFoodEntertainment, name='unitedFoodEntertainment'),
    path('unitedService', home.views.unitedService, name='unitedService'),
    path('unitedFamilyOptions', home.views.unitedFamilyOptions, name='unitedFamilyOptions'),
    path('spiritAvailability', home.views.spiritAvailability, name='spiritAvailability'),
    path('spiritCost', home.views.spiritCost, name='spiritCost'),
    path('spiritLegroom', home.views.spiritLegroom, name='spiritLegroom'),
    path('spiritTimeliness', home.views.spiritTimeliness, name='spiritTimeliness'),
    path('spiritHiddenFees', home.views.spiritHiddenFees, name='spiritHiddenFees'),
    path('spiritBaggageFees', home.views.spiritBaggageFees, name='spiritBaggageFees'),
    path('spiritTravelRewards', home.views.spiritTravelRewards, name='spiritTravelRewards'),
    path('spiritReimbursement', home.views.spiritReimbursement, name='spiritReimbursement'),
    path('spiritConnections', home.views.spiritConnections, name='spiritConnections'),
    path('spiritFoodEntertainment', home.views.spiritFoodEntertainment, name='spiritFoodEntertainment'),
    path('spiritService', home.views.spiritService, name='spiritService'),
    path('spiritFamilyOptions', home.views.spiritFamilyOptions, name='spiritFamilyOptions'),
    path('react', home.views.react, name='react'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
