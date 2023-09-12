from django.db import models


class Weapons(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    attack_rating = models.IntegerField()
    scaling = models.IntegerField()
    requirements = models.IntegerField()
    amount = models.IntegerField()
    description = models.TextField()
