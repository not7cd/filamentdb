from django.db import models
from django.conf import settings
from django.urls import reverse


class OwnerProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    department = models.CharField(max_length=100)


class Material(models.Model):
    PLA = "PLA"
    PET = "PET"
    ABS = "ABS"
    ASA = "ASA"
    TPU = "TPU"
    PLASTIC_CHOICES = [
        (PLA, "PLA"),
        (PET, "PET"),
        (ABS, "ABS"),
        (ASA, "ASA"),
        (TPU, "TPU"),
    ]
    brand = models.CharField(max_length=200)
    plastic = models.CharField(max_length=50, choices=PLASTIC_CHOICES, default=PLA)
    density = models.FloatField()
    diameter = models.FloatField()
    description = models.CharField(max_length=500, blank=True)

    def get_absolute_url(self):
        return reverse("material-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return f"{self.brand} {self.plastic} {self.diameter} {self.description}"


class Variant(models.Model):
    name = models.CharField(max_length=200)
    material = models.ForeignKey(Material, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse("variant-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return f"{self.material} {self.name}"


class Spool(models.Model):
    pub_date = models.DateTimeField("date added", auto_now_add=True, blank=True)
    variant = models.ForeignKey(Variant, on_delete=models.CASCADE)
    mass_net = models.FloatField()
    comment = models.CharField(max_length=500, blank=True)
    owner = models.ForeignKey(OwnerProfile, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse("spool-detail", kwargs={"pk": self.pk})
