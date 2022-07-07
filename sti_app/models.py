import os

from django.core.files.storage import FileSystemStorage
from django.db import models
from django.utils.datetime_safe import datetime
from pathlib import Path


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
