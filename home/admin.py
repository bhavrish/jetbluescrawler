from django.contrib import admin
from .models import AvailabilityBadModel, AvailabilityGoodModel, CostBadModel, CostGoodModel, LegroomBadModel, LegroomGoodModel, TimelinessBadModel, TimelinessGoodModel
# Register your models here.

admin.site.register(AvailabilityBadModel)
admin.site.register(AvailabilityGoodModel)
admin.site.register(CostBadModel)
admin.site.register(CostGoodModel)
admin.site.register(LegroomBadModel)
admin.site.register(LegroomGoodModel)
admin.site.register(TimelinessBadModel)
admin.site.register(TimelinessGoodModel)