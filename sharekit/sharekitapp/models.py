from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from nepse_func import scrips


class Share(models.Model):
    scrip = models.CharField(max_length=20, choices=scrips)
    quantity = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.scrip} - {self.quantity} - {self.user}"

    def get_absolute_url(self):
        return reverse('home')
