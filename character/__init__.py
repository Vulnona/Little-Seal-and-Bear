from .name_generator import NameGenerator
from . import abilities
from . import animalsubtypes
from . import skills
from . import animaltypes


class Character:
    abilities=abilities.CharacterAbilities()

    def __init__(self, name=None, animaltype=None, animalsubtype=None, level=0, exp=10, skills=[]):
        self.name=name
        self.animaltype=animaltype
        self.animalsubtype=animalsubtype
        self.level=level
        self.exp=exp
        self.skills = skills
        self.update_skills(self.skills)

    def get_str(self):
        return self.abilities.__getattribute__('strength').value

    def get_dext(self):
        return self.abilities.__getattribute__('dexterity').value

    def get_resi(self):
        return self.abilities.__getattribute__('resistance').value

    def get_int(self):
        return self.abilities.__getattribute__('intelligence').value

    def get_Name(self):
        return self.name

    def set_Name(self, name):
        self.name=str(name)

    def get_skills(self):
        return self.skills

    def set_skill(self, input_skill):
        self.skills.append(input_skill)

    def get_level(self):
        level=str(self.level)
        return level

    def set_type(self, type):
        self.animaltype=str(type)

    def get_type(self):
        return self.animaltype

    def set_subtype(self, animalsubtype):
        self.animalsubtype=animalsubtype
        self.update_applicable_skills()
        self.update_skills(self.skills)

    def get_subtype(self):
        return str(self.animalsubtype)

    def get_exp(self):
        return self.exp

    def gain_exp(self, points):
        self.exp+=points

    def lower_exp(self, points):
        self.exp-=points

    def spend_ability_points(self, input_ability):
        for ability in abilities.ALL:
            if str(ability.id)==input_ability:
                getattr(self.abilities, ability.id).value+=1
                self.update_applicable_skills()
                self.update_skills(self.skills)
                break

    def lost_ability_points(self, input_ability):
        for ability in abilities.ALL:
            if str(ability.id)==input_ability:
                getattr(self.abilities, ability.id).value-=1
                self.update_applicable_skills()
                self.update_skills(self.skills)
                break

    def ability_value(self, input_ability):
        for ability in abilities.ALL:
            if str(ability.id)==input_ability:
                return getattr(self.abilities, ability.id).value

    def LevelUp(self):
        self.level=self.level+1

    def randomize_name(self):
        name=NameGenerator.generate_name(2, 5)
        self.set_Name(name)
        print(self.name)

    def update_applicable_skills(self):
        self.skills = []
        for skill in skills.ALL:
            continues = True
            for subtype in skill.applicable_subtype:
                if (self.animalsubtype==subtype):
                    continues=False
                    break
            if continues:
                continue
            continues = False

            for required_ability, min_value in skill.required_abilities.items():
                if getattr(self.abilities, required_ability.id).value < min_value:
                    continues = True
                    break
            if continues:
                continue
            self.skills.append(skill)

    def update_skills(self, Liste):
        self.skills=Liste[:]

    def has_skill(self, input_skill):
        for skill in self.skills:
            if skill==input_skill:
                return True
        return False

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