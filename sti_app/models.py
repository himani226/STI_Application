from django.db import models


# Create your models here.
class Menus(models.Model):
    menu_name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
