from . import abilities
from . import animalsubtypes


class BaseSkill:
    applicable_subtype = []
    required_abilities = {}

class AllSkill(BaseSkill):
    applicable_subtype = [
        animalsubtypes.Schwarz,
        animalsubtypes.Grau,
        animalsubtypes.Weiss
    ]

class SchwarzSkill(BaseSkill):
    applicable_subtype = [
        animalsubtypes.Schwarz
    ]

class GrauSkill(BaseSkill):
    applicable_subtype = [
        animalsubtypes.Grau
    ]


class WeissSkill(BaseSkill):
    applicable_subtype = [
        animalsubtypes.Weiss
    ]

class SwimmingCharacterSkill(AllSkill):
    id = 'swim'
    name = 'Schwimmen'

    required_abilities = {
        abilities.DexterityCharacterAbility: 7,
        abilities.IntelligenceCharacterAbility: 4
    }


class StealthCharacterSkill(SchwarzSkill):
    id = 'stealth'
    name = 'Schleichen'

    required_abilities = {
        abilities.IntelligenceCharacterAbility: 2,
        abilities.DexterityCharacterAbility: 2
    }


class TailCharacterSkill(SchwarzSkill):
    id = 'tail'
    name = 'Schwanzpeitsche'

    required_abilities = {
        abilities.DexterityCharacterAbility: 7,
        abilities.ResistanceCharacterAbility: 2,
        abilities.StrengthCharacterAbility: 2
    }


class GrasMovementCharacterSkill(SchwarzSkill):
    id = 'erasegras'
    name = 'Grasschlitzer'

    required_abilities = {
        abilities.DexterityCharacterAbility: 9,
        abilities.IntelligenceCharacterAbility: 4
    }


class BiteCharacterSkill(GrauSkill):
    id = 'bite'
    name = 'Biss'

    required_abilities = {
        abilities.StrengthCharacterAbility: 4,
        abilities.DexterityCharacterAbility: 2
    }


class RunnerCharacterSkill(GrauSkill):
    id = 'runner'
    name = 'Läufer'

    required_abilities = {
        abilities.StrengthCharacterAbility: 3,
        abilities.DexterityCharacterAbility: 6,
        abilities.IntelligenceCharacterAbility: 5
    }


class EarthquakeCharacterSkill(GrauSkill):
    id = 'earthquake'
    name = 'Erdbeben'

    required_abilities = {
        abilities.StrengthCharacterAbility: 15,
        abilities.DexterityCharacterAbility: 6
    }


class MagicalHealCharacterSkill(WeissSkill):
    id = 'magical_heal'
    name = 'Magische Heilung'

    required_abilities = {
        abilities.IntelligenceCharacterAbility: 5
    }


class PlantingCharacterSkill(WeissSkill):
    id = 'plant'
    name = 'Natur erwecken'

    required_abilities = {
        abilities.IntelligenceCharacterAbility: 8,
        abilities.ResistanceCharacterAbility: 4,
        abilities.DexterityCharacterAbility: 4
    }


class SaversCharacterSkill(WeissSkill):
    id = 'robe'
    name = 'Schutzmantel'

    required_abilities = {
        abilities.IntelligenceCharacterAbility: 14,
        abilities.ResistanceCharacterAbility: 7
    }


ALL = [
    SwimmingCharacterSkill,
    StealthCharacterSkill,
    TailCharacterSkill,
    GrasMovementCharacterSkill,
    BiteCharacterSkill,
    RunnerCharacterSkill,
    EarthquakeCharacterSkill,
    MagicalHealCharacterSkill,
    PlantingCharacterSkill,
    SaversCharacterSkill
]
