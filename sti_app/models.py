from django.core.files.storage import FileSystemStorage
from django.db import models
from django.utils.datetime_safe import datetime

fs = FileSystemStorage(location='/media/photos')


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
    banner_image = models.ImageField(max_length=200, storage=fs)
    pub_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.banner_image


# homedata table has been created to load the data from database
class HomeData(models.Model):
    info_text = models.CharField(max_length=500)
    spotlight_text1 = models.CharField(max_length=500)
    spotlight_text2 = models.CharField(max_length=500)
    spotlight_text3 = models.CharField(max_length=500)
    slider_image = models.ImageField(max_length=200, storage=fs)
    info_image = models.ImageField(max_length=200, storage=fs)
    education_image = models.ImageField(max_length=200, storage=fs)
    research_image = models.ImageField(max_length=200, storage=fs)
    innovation_image = models.ImageField(max_length=200, storage=fs)
    mission_image = models.ImageField(max_length=200, storage=fs)
    policies_image = models.ImageField(max_length=200, storage=fs)
    plans_image = models.ImageField(max_length=200, storage=fs)
    pub_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.info_text, self.spotlight_text1, \
               self.spotlight_text2, self.spotlight_text3, \
               self.slider_image, self.info_image, self.education_image, self.research_image, \
               self.innovation_image, self.mission_image, self.policies_image, self.plans_image, self.pub_date


# about page data will be stored here
class AboutData(models.Model):
    about_text = models.CharField(max_length=500)
    pub_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.about_text