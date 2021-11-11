from django.db import models
from django.contrib.auth.models import User


class Share(models.Model):
    scrip = models.CharField(max_length=20)
    quantity = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.scrip} - {self.quantity} - {self.user}"
