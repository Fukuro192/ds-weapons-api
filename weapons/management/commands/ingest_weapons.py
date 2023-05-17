import json
from django.conf import settings
from django.core.management.base import BaseCommand

from weapons.models import Weapon

class Command(BaseCommand):
    help = 'Create Dark Souls Weapons from JSON file'

    def handle(self, *args, **kwargs):
        # set the path to the datafile
        datafile = settings.BASE_DIR / 'data' / 'weapons.json'
        assert datafile.exists()

        # load the datafile
        with open(datafile, 'r') as f:
            data = json.load(f)

        weapons = [Weapon(
            name = weapon.get("name", None),
            attack = weapon.get("attack", None),
            defence = weapon.get("defence", None),
            effects = weapon.get("effects", None),
            req = weapon.get("req", None),
            scale = weapon.get("scale", None),
            durability = weapon.get("durability", None),
            weight = weapon.get("weight", None),
            attack_types = weapon.get("attackTypes", None),
            obtained = weapon.get("obtained", None),
            aota_only = weapon.get("aotaOnly", None),
        ) for weapon in data]

        Weapon.objects.bulk_create(weapons)
