from .name_generator import NameGenerator
from . import abilities
from . import animalsubtypes
from . import skills
from . import animaltypes


class Character:
    abilities=abilities.CharacterAbilities()
    skills=[]

    def __init__(self, name=None, animaltype=None, animalsubtype=None, level=0, exp=10):
        self.name=name
        self.animaltype=animaltype
        self.animalsubtype=animalsubtype
        self.level=level
        self.exp=exp

    def create(self, name, animaltype, animalsubtype, level, exp=10):
        self.name=name
        self.animaltype=animaltype
        self.animalsubtype=animalsubtype
        self.level=level
        self.exp=exp

    def getName(self):
        return self.name

    def setName(self, name):
        self.name=str(name)

    def getlevel(self):
        level=str(self.level)
        return level

    def settype(self, type):
        self.animaltype=str(type)

    def gettype(self):
        #type=str(self.animaltype)
        return self.animaltype

    def setsubtype(self, animalsubtype):
        self.animalsubtype=animalsubtype
        self.update_applicable_skills()

    def getsubtype(self):
        return str(self.animalsubtype)

    def getexp(self):
        return self.exp

    def gainexp(self, points):
        self.exp+=points

    def lowerexp(self, points):
        self.exp-=points

    def spend_ability_points(self, inputability):
        for ability in abilities.ALL:
            if str(ability.id)==inputability:
                getattr(self.abilities, ability.id).value+=1
                self.update_applicable_skills()
                break

    def lost_ability_points(self, inputability):
        for ability in abilities.ALL:
            if str(ability.id)==inputability:
                getattr(self.abilities, ability.id).value-=1
                self.update_applicable_skills()
                break

    def abilityvalue(self, inputability):
        for ability in abilities.ALL:
            if str(ability.id)==inputability:
                return getattr(self.abilities, ability.id).value

    def LevelUp(self):
        self.level=self.level+1

    def randomize_name(self):
        name=NameGenerator.generate_name(2, 5)
        self.setName(name)
        print(self.name)

    def update_applicable_skills(self):
        self.skills = []
        for skill in skills.ALL:
            cont = True
            for subtype in skill.applicable_subtype:
                if (self.animalsubtype==subtype):
                    cont=False
                    break
            if cont:
                continue
            cont = False

            for required_ability, min_value in skill.required_abilities.items():
                print("In condition")
                if getattr(self.abilities, required_ability.id).value < min_value:
                    cont = True
                    break
            if cont:
                continue
            self.skills.append(skill)


# für den Charakterbogen

    def __str__(self):
        content = [
            '# Charakter Bogen',
            '',
            '  - Name: ' + self.name,
            '  - Tierart: ' + str(self.animaltype),
            '  - Farbe: ' + str(self.animalsubtype),
            '',
            '## Statuswerte',
            ''
        ]

        for ability in abilities.ALL:
            content.append('  - ' + ability.name + ': ' + str(getattr(self.abilities, ability.id).value))

        content.extend([
            '',
            '## Fähigkeiten',
            ''
        ])

        if not self.skills:
            content.append('Keine Fähigkeiten verfügbar.')
        else:
            for skill in self.skills:
                content.append('  - ' + skill.name)

        return '\n'.join(content)
