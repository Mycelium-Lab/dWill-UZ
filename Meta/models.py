from django.db import models

class Wallet(models.Model):
    from1 = models.CharField(max_length=255)
    to1 = models.CharField(max_length=255)
    date = models.DateField()
    amount = models.CharField(max_length=255)

