from django.db import connections
from django.db import models

# Create your models here.

class Shows(models.Model):
    movie_name = models.TextField(db_column='movie name', blank=False, null=False,primary_key=True)  # Field renamed to remove unsuitable characters.
    theatre_name = models.TextField(db_column='theatre name', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    theatre_location = models.TextField(db_column='theatre location', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    release_date = models.TextField(db_column='release date', blank=True, null=True)  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'shows'
