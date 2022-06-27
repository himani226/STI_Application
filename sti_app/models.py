from django.db import models


# Create your models here.
class Menu(models.Model):
    menu_name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.menu_name
