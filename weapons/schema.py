from typing import List
from ninja import Schema, Field

class WeaponSchema(Schema):
    id: int
    name: str
    attack: dict
    defence: dict
    effects: dict
    req: dict
    scale: dict
    durability: int
    weight: int = Field(None)
    attack_types: List
    obtained: List
    aota_only: bool

class NotFoundSchema(Schema):
    message: str
