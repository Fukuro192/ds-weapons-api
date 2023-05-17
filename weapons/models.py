from django.db import models

# Create your models here.
class Weapon(models.Model):
    name = models.CharField(max_length=50)
    attack = models.JSONField()
    defence = models.JSONField()
    effects = models.JSONField()
    req = models.JSONField()
    scale = models.JSONField()
    durability = models.IntegerField()
    weight = models.IntegerField(null=True)
    attack_types = models.JSONField()
    obtained = models.JSONField()
    aota_only = models.BooleanField()
