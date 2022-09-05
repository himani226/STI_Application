from django.db import models
from django.utils.datetime_safe import datetime


# Create your models here.
# headermenu table has been created to load the data from database
class HeaderMenu(models.Model):
    menu_name = models.CharField(max_length=200)
    menu_link = models.CharField(max_length=200, default='#', blank=True)
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
    home_stage_image = models.ImageField(blank=True, upload_to='home_stage_image')
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
        return f'{self.stage_title}---{self.pillar_title}'

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
    pub_date = models.DateTimeField(default=datetime.now, blank=True)

    def embed(self):
        return {
            "indicator_title": self.indicator_title.indicator_title,
            "indicator_description": self.indicator_description
        }


class \
        TechnologyArea(models.Model):
    technology_area_name = models.CharField(primary_key=True, max_length=200)
    pub_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.technology_area_name


class TechnologyAreaDetail(models.Model):
    technology_area_name = models.ForeignKey(TechnologyArea,
                                    on_delete=models.SET_NULL,
                                    blank=True,
                                    null=True,
                                    )
    technology_name = models.CharField(max_length=200,blank=True)
    inventor_detail = models.CharField(max_length=200,blank=True)
    institute = models.CharField(max_length=200,blank=True)
    technology_abstract = models.TextField(blank=True)
    technology_status = models.CharField(max_length=200,blank=True)
    technology_transferred = models.CharField(max_length=200,blank=True)
    pub_date = models.DateTimeField(default=datetime.now,blank=True)

    def __str__(self):
        return self.technology_name

    def embed(self):
        return {

            "technology_area_name_id": self.technology_area_name.technology_area_name,
            "technology_name": self.technology_name,
            "inventor_detail": self.inventor_detail,
            "institute": self.institute,
            "technology_abstract": self.technology_abstract,
            "technology_status": self.technology_status,
            "technology_transferred": self.technology_transferred,
        }

class Contributor(models.Model):
    contributor_title = models.CharField(null=True, max_length=200)
    contributor_image = models.ImageField(max_length=200, upload_to='contributor_image')
    pub_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.contributor_title