from django.db import models
from django.utils.datetime_safe import datetime


# Create your models here.
# headermenu table has been created to load the data from database
class HeaderMenu(models.Model):
    menu_name = models.CharField(max_length=200)
    menu_link = models.CharField(max_length=200, default='#')
    pub_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.menu_name


# footermenu table has been created to load the data from database
class FooterMenu(models.Model):
    menu_name = models.CharField(max_length=200)
    menu_link = models.CharField(max_length=200, default='#')
    pub_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.menu_name


# banner table has been created to load the data from database
class Banner(models.Model):
    banner_title = models.CharField(null=True, max_length=200)
    banner_image = models.ImageField(max_length=200, upload_to='banner_image')
    pub_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.banner_title


# homedata table has been created to load the data from database
class HomeData(models.Model):
    home_info_text = models.TextField(null=True)
    home_info_image = models.ImageField(blank=True, upload_to='home_info_image')
    pub_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.home_info_text


class HomeSlider(models.Model):
    home_slider_title = models.TextField(null=True)
    home_slider_image = models.ImageField(blank=True, upload_to='home_slider_image')
    pub_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.home_slider_title


class HomeFramework(models.Model):
    home_framework_title = models.CharField(null=True, max_length=200)
    home_framework_image = models.ImageField(blank=True, upload_to='home_framework_image')
    pub_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.home_framework_title


class HomePlanPolicies(models.Model):
    home_plan_policies_title = models.CharField(null=True, max_length=200)
    home_plan_policies_image = models.ImageField(blank=True, upload_to='home_policies_image')
    pub_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.home_plan_policies_title


# about page data will be stored here


class AboutData(models.Model):
    about_text = models.TextField(null=True)
    pub_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.about_text


class Spotlight(models.Model):
    spotlight_image = models.ImageField(blank=True, upload_to='spotlight_image')
    spotlight_title = models.TextField(null=True)
    spotlight_text = models.TextField(null=True)
    pub_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.spotlight_title


# STI Indicators Tables

class Stage(models.Model):
    stage_title = models.CharField(primary_key=True, max_length=200)
    pub_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.stage_title


class Pillar(models.Model):
    stage_title = models.ForeignKey(Stage,
                                    on_delete=models.SET_NULL,
                                    blank=True,
                                    null=True,
                                    )
    pillar_title = models.CharField(max_length=200)
    pub_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return f"{self.pillar_title}, {self.stage_title}"

    def embed(self):
        return {
            "stage_title": self.stage_title.stage_title,
            "id": self.id,
            "pillar_title": self.pillar_title
        }


class Indicator(models.Model):
    stage_title = models.ForeignKey(Stage,
                                    on_delete=models.SET_NULL,
                                    blank=True,
                                    null=True,
                                    )
    pillar_title = models.ForeignKey(Pillar,
                                     on_delete=models.SET_NULL,
                                     blank=True,
                                     null=True,
                                     )
    indicator_title = models.TextField(null=True)
    pub_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.indicator_title

    def embed(self):
        return {
            "pillar_title_id": self.pillar_title.pillar_title,
            "id": self.id,
            "indicator_title": self.indicator_title
        }


class IndicatorDefinition(models.Model):
    indicator_title = models.ForeignKey(Indicator,
                                        on_delete=models.SET_NULL,
                                        blank=True,
                                        null=True,
                                        )
    indicator_description = models.TextField(null=True)
    indicator_image = models.ImageField(blank=True, upload_to='indicator_image')
    pub_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return f'{self.indicator_title}-----{self.indicator_description}'

    def embed(self):
        return {
            "indicator_title": self.indicator_title.indicator_title,
            "indicator_description": self.indicator_description,
            "indicator_image": str(self.indicator_image)
        }