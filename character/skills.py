from . import abilities
from . import animalsubtypes


class BaseSkill:
    applicable_subtype = []
    required_abilities = {}


class AllSkill(BaseSkill):
    applicable_subtype = [
        animalsubtypes.Brown,
        animalsubtypes.Grey,
        animalsubtypes.White
    ]


class BrownSkill(BaseSkill):
    applicable_subtype = [
        animalsubtypes.Brown
    ]

class GreySkill(BaseSkill):
    applicable_subtype = [
        animalsubtypes.Grey
    ]

class WhiteSkill(BaseSkill):
    applicable_subtype = [
        animalsubtypes.White
    ]

class SwimmingCharacterSkill(AllSkill):
    id = 'swim'
    name = 'Schwimmen'

    required_abilities = {
        abilities.DexterityCharacterAbility: 7,
        abilities.IntelligenceCharacterAbility: 4
    }


class EnduranceCharacterSkill(AllSkill):
    id = "endurance"
    name = "Resistenz"

    required_abilities = {
        abilities.DexterityCharacterAbility: 3,
        abilities.ResistanceCharacterAbility: 12
    }


class StealthCharacterSkill(BrownSkill):
    id = 'stealth'
    name = 'Schleichen'

    required_abilities = {
        abilities.IntelligenceCharacterAbility: 2,
        abilities.DexterityCharacterAbility: 2
    }


class TailCharacterSkill(BrownSkill):
    id = 'tail'
    name = 'Schwanzpeitsche'

    required_abilities = {
        abilities.DexterityCharacterAbility: 7,
        abilities.ResistanceCharacterAbility: 2,
        abilities.StrengthCharacterAbility: 2
    }


class GrasMovementCharacterSkill(BrownSkill):
    id = 'erasegras'
    name = 'Grasschlitzer'

    required_abilities = {
        abilities.DexterityCharacterAbility: 9,
        abilities.IntelligenceCharacterAbility: 4
    }


class BiteCharacterSkill(GreySkill):
    id = 'bite'
    name = 'Flammenbiss'

    required_abilities = {
        abilities.StrengthCharacterAbility: 4,
        abilities.DexterityCharacterAbility: 2
    }


class RunnerCharacterSkill(GreySkill):
    id = 'runner'
    name = 'Läufer'

    required_abilities = {
        abilities.StrengthCharacterAbility: 3,
        abilities.DexterityCharacterAbility: 6,
        abilities.IntelligenceCharacterAbility: 5
    }


class EarthquakeCharacterSkill(GreySkill):
    id = 'earthquake'
    name = 'Erdbeben'

    required_abilities = {
        # abilities.StrengthCharacterAbility: 15,
        abilities.DexterityCharacterAbility: 6
    }


class MagicalHealCharacterSkill(WhiteSkill):
    id = 'magical_heal'
    name = 'Magische Heilung'

    required_abilities = {
        abilities.IntelligenceCharacterAbility: 5
    }


class PlantingCharacterSkill(WhiteSkill):
    id = 'plant'
    name = 'Natur erwecken'

    required_abilities = {
        # abilities.IntelligenceCharacterAbility: 8,
        # abilities.ResistanceCharacterAbility: 4,
        abilities.DexterityCharacterAbility: 4
    }


class SaversCharacterSkill(WhiteSkill):
    id = 'robe'
    name = 'Schutzmantel'

    required_abilities = {
        abilities.IntelligenceCharacterAbility: 14,
        abilities.ResistanceCharacterAbility: 7
    }

FIGHT = [
    TailCharacterSkill,
    EarthquakeCharacterSkill,
    BiteCharacterSkill
]

ALL = [
    SwimmingCharacterSkill,  # included functionality
    EnduranceCharacterSkill,  # partly included functionality
    StealthCharacterSkill,  # MAGIC!
    TailCharacterSkill,
    GrasMovementCharacterSkill,  # included functionality
    BiteCharacterSkill,  # MAGIC!
    RunnerCharacterSkill,  # included functionality
    EarthquakeCharacterSkill,
    MagicalHealCharacterSkill,  # included functionality
    PlantingCharacterSkill,  # included functionality
    SaversCharacterSkill  # NO MAGIC!
]
