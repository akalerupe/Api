from django.db import models


# Create your views here.
class Hero(models.Model):
    """Model definition for MODELNAME."""
    name=models.CharField(max_length=50,blank=True)
    alias=models.CharField(max_length=500,blank=True)

    def __str__(self):
        return self.name
