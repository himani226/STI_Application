from django.contrib import admin
from .models import HeaderMenu, FooterMenu, Banner, HomeData, HomeSlider, HomePlanPolicies, Spotlight, \
    AboutData, Stage, Pillar, Indicator, IndicatorDefinition

# Register your models here.
admin.site.register(HeaderMenu),
admin.site.register(FooterMenu),
admin.site.register(Banner),
admin.site.register(HomeData),
admin.site.register(HomeSlider),
admin.site.register(HomePlanPolicies),
admin.site.register(Spotlight),
admin.site.register(AboutData),
admin.site.register(Stage),


class PillarAdmin(admin.ModelAdmin):
    list_display = ("stage_title", "pillar_title")


admin.site.register(Pillar, PillarAdmin),


class IndicatorAdmin(admin.ModelAdmin):
    list_display = ("stage_title", "pillar_title", "indicator_title")


admin.site.register(Indicator, IndicatorAdmin),


class IndicatordefAdmin(admin.ModelAdmin):
    list_display = ("indicator_title", "indicator_description")


admin.site.register(IndicatorDefinition, IndicatordefAdmin),
