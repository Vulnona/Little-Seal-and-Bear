import random

class BaseCharacterAbility:
   #base character ability to inherit from
    value = 0

class StrengthCharacterAbility(BaseCharacterAbility):
    id = 'strength'
    name = 'Stärke'

class ResistanceCharacterAbility(BaseCharacterAbility):
    id = 'resistance'
    name = 'Ausdauer'

class DexterityCharacterAbility(BaseCharacterAbility):
    id = 'dexterity'
    name = 'Geschicklichkeit'

class IntelligenceCharacterAbility(BaseCharacterAbility):
    id = 'intelligence'
    name = 'Intelligenz'

ALL = [
    StrengthCharacterAbility,
    ResistanceCharacterAbility,
    DexterityCharacterAbility,
    IntelligenceCharacterAbility
]

class CharacterAbilities:
    def __init__(self):
        for ability in ALL:
            setattr(self, ability.id, ability())
    def randomize(self):
        for ability in ALL:
            getattr(self, ability.id).value = random.randint(0, 4)
