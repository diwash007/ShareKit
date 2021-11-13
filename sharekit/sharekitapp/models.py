from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.urls import reverse
from nepse_func import scrips


class Share(models.Model):
    scrip = models.CharField(max_length=20, choices=scrips)
    quantity = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.scrip} - {self.quantity}"

    def get_absolute_url(self):
        return reverse('home')

class Demat(models.Model):
    boid = models.IntegerField()
    name = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=CASCADE)

    def __str__(self):
        return f"{self.boid} - {self.name}"

    def get_absolute_url(self):
        return reverse('ipo')
