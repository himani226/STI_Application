from django.contrib import admin
from .models import HeaderMenu, FooterMenu, Banner, HomeData, HomeSlider, HomeFramework, HomePlanPolicies, Spotlight, \
    AboutData, Stage, Pillar, Indicator, IndicatorDefinition

# Register your models here.
admin.site.register(HeaderMenu),
admin.site.register(FooterMenu),
admin.site.register(Banner),
admin.site.register(HomeData),
admin.site.register(HomeSlider),
admin.site.register(HomeFramework),
admin.site.register(HomePlanPolicies),
admin.site.register(Spotlight),
admin.site.register(AboutData),
admin.site.register(Stage),
admin.site.register(Pillar),
admin.site.register(Indicator),
admin.site.register(IndicatorDefinition),
