from typing import List, Optional
from ninja import NinjaAPI
from weapons.models import Weapon
from weapons.schema import WeaponSchema, NotFoundSchema

api = NinjaAPI()

@api.get("/weapons", response=List[WeaponSchema])
def weapons(request, name: Optional[str] = None):
    if name:
        return Weapon.objects.filter(name__icontains=name)
    return Weapon.objects.all()


@api.get("/weapons/{weapon_id}", response={200: WeaponSchema, 404: NotFoundSchema})
def weapon(request, weapon_id: int):
    try:
        weapon = Weapon.objects.get(pk=weapon_id)
        return weapon
    except Weapon.DoesNotExist as e:
        return 404, {"message": "Weapon does not exist"}
