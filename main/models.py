from django.db import models

# Create your models here.



class Car(models.Model):
    brand = models.CharField(max_length=120)
    model = models.CharField(max_length=120)
    description = models.TextField()

    def __str__(self) -> str:
        return self.brand