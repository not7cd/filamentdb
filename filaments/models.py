from django.db import models
from django.conf import settings


class OwnerProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    department = models.CharField(max_length=100)


class Material(models.Model):
    brand = models.CharField(max_length=200)
    plastic = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    diameter = models.FloatField()


class Variant(models.Model):
    name = models.CharField(max_length=200)
    material = models.ForeignKey(Material, on_delete=models.CASCADE)


class Spool(models.Model):
    pub_date = models.DateTimeField('date added')
    variant = models.ForeignKey(Variant, on_delete=models.CASCADE)
    mass_net = models.FloatField()
    owner = models.OneToOneField(OwnerProfile, on_delete=models.CASCADE)


