from django.db import models

class CentreonObjectStatus(models.Model):
    name = models.CharField(max_length=50)
    imported = models.BooleanField
    state= models.BooleanField

    def __str__(self):
        return self.name