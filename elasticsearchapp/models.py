from django.db import models

# Create your models here.
class Car(models.Model):
 name = models.CharField(max_length=15)
 color = models.CharField(max_length=15)
 description = models.TextField()
 type = models.IntegerField(choices=[
  (1, "Sedan"),
  (2, "Truck"),
  (4, "SUV"),
 ])

