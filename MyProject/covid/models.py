from django.db import models

# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=64)
    population = models.IntegerField()
    deaths = models.IntegerField()
    confirmed = models.IntegerField()
    recovered = models.IntegerField()
    class Meta:
        verbose_name = 'country'
        verbose_name_plural = 'countries'