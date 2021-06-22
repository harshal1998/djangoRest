from django.db import models


# Create your models here.
class demo(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    address = models.CharField(max_length=50,default='thane')
    marks = models.IntegerField(default=50)

    def __str__(self):
        return self.name
