import os

from django.core.files.storage import FileSystemStorage
from django.db import models
from django.utils.datetime_safe import datetime
from pathlib import Path

uploads = 'media'


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
    banner_image = models.ImageField(max_length=200, upload_to=uploads)
    pub_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.banner_image


# homedata table has been created to load the data from database
class HomeData(models.Model):
    info_text = models.TextField(null=True)
    spotlight_text1 = models.TextField(null=True)
    spotlight_text2 = models.TextField(null=True)
    spotlight_text3 = models.TextField(null=True)
    slider_image = models.ImageField(max_length=200, upload_to=uploads)
    info_image = models.ImageField(max_length=200, upload_to=uploads)
    education_image = models.ImageField(max_length=200, upload_to=uploads)
    research_image = models.ImageField(max_length=200, upload_to=uploads)
    innovation_image = models.ImageField(max_length=200, upload_to=uploads)
    mission_image = models.ImageField(max_length=200, upload_to=uploads)
    policies_image = models.ImageField(max_length=200, upload_to=uploads)
    plans_image = models.ImageField(max_length=200, upload_to=uploads)
    pub_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.info_text


# about page data will be stored here
class AboutData(models.Model):
    about_text = models.TextField(null=True)
    pub_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.about_text
