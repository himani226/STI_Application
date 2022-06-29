from django.contrib import admin
from .models import HeaderMenu, FooterMenu, Banner, HomeData, AboutData

# Register your models here.
admin.site.register(HeaderMenu),
admin.site.register(FooterMenu),
admin.site.register(Banner),
admin.site.register(HomeData),
admin.site.register(AboutData)