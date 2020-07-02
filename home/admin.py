from django.contrib import admin
from .models import JetblueAggregateModel, JetblueCondensedModel, AmericanAggregateModel, AmericanCondensedModel, UnitedAggregateModel, UnitedCondensedModel, SpiritAggregateModel, SpiritCondensedModel
# Register your models here.

admin.site.register(JetblueAggregateModel)
admin.site.register(JetblueCondensedModel)
admin.site.register(AmericanAggregateModel)
admin.site.register(AmericanCondensedModel)
admin.site.register(UnitedAggregateModel)
admin.site.register(UnitedCondensedModel)
admin.site.register(SpiritAggregateModel)
admin.site.register(SpiritCondensedModel)