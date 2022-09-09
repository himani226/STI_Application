from django.contrib import admin
from .models import HeaderMenu, FooterMenu, Banner, HomeData, HomeSlider, HomePlanPolicies, Spotlight, \
     Stage, Pillar, Indicator, IndicatorDefinition, TechnologyArea, TechnologyAreaDetail, Contributor

# Register your models here.
admin.site.register(HeaderMenu),
admin.site.register(FooterMenu),
admin.site.register(Banner),
admin.site.register(HomeData),
admin.site.register(HomeSlider),
admin.site.register(HomePlanPolicies),
admin.site.register(Spotlight),
admin.site.register(Stage),
admin.site.register(Contributor),


class PillarAdmin(admin.ModelAdmin):
    list_display = ("stage_title", "pillar_title")


admin.site.register(Pillar, PillarAdmin),


class IndicatorAdmin(admin.ModelAdmin):
    list_display = ("stage_title", "pillar_title", "indicator_title")


admin.site.register(Indicator, IndicatorAdmin),


class IndicatordefAdmin(admin.ModelAdmin):
    class Media:
        css = {
            "all": ("css/content.css",)
        }
        js = ("js/content.js",)

    list_display = ("indicator_title",)


admin.site.register(IndicatorDefinition, IndicatordefAdmin),
admin.site.register(TechnologyArea),


class TechAdmin(admin.ModelAdmin):
    list_display = ("technology_name", "institute","inventor_detail","technology_area_name")


admin.site.register(TechnologyAreaDetail, TechAdmin),
