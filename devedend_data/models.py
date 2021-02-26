from django.db import models

# Create your models here.
class data(models.Model):
    compny_name = models.CharField(max_length=100,primary_key=True)
    type = models.CharField(max_length=50)
    rate = models.FloatField()
    announcment = models.DateField()
    record = models.DateField()
    ex_devedend = models.DateField()
    dividend_fv =  models.FloatField()
    dividend_mp = models.FloatField()