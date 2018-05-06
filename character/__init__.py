from .name_generator import NameGenerator
from . import abilities
from . import animalsubtypes
from . import skills
from . import animaltypes


class Character:
    abilities=abilities.CharacterAbilities()

    def __init__(self, name=None, animaltype=None, animalsubtype=None, level=0, exp=10, skills=[], status=[], temp_status=[]):
        self.name = name
        self.animaltype = animaltype
        self.animalsubtype = animalsubtype
        self.level = level
        self.exp = exp
        self.skills = skills
        self.update_skills(self.skills)
        self.status = status
        self.temp_status = temp_status

    def get_status_max(self, input_string):
        #Gesundheit
        if input_string=='health':
            return self.status[0]
        #Ausdauer
        elif input_string=='endu':
            return self.status[1]
        #Magie
        elif input_string=="magic":
            return self.status[2]

    def get_status_temp(self, input_string):
        if input_string=='health':
            return self.temp_status[0]
        elif input_string=='endu':
            return self.temp_status[1]
        elif input_string=="magic":
            return self.temp_status[2]

    def change_status_temp(self, input_string, Vorzeichen):
        if input_string=='health':
            if Vorzeichen=='+':
                if self.temp_status<self.status[0]:
                    self.temp_status[0]+=1
            if Vorzeichen=='-':
                if self.temp_status[0] > 0:
                    self.temp_status[0]-=1
        elif input_string=='endu':
            if Vorzeichen=='+':
                if self.temp_status < self.status[1]:
                    self.temp_status[1]+=1
            if Vorzeichen=='-':
                if self.temp_status[1] > 0:
                    self.temp_status[1]-=1
        elif input_string=="magic":
            if Vorzeichen=='+':
                if self.temp_status < self.status[1]:
                    self.temp_status[2]+=1
            if Vorzeichen=='-':
                if self.temp_status[2] > 0:
                    self.temp_status[2]-=1

    def set_status_initial(self, animaltype):
        if (str(animaltype)==str(animaltypes.clsBaer)):
            self.status=[20,100,5]
            if self.has_skill(skills.EnduranceCharacterSkill):
                self.status[1]+=20
        elif (str(animaltype)==str(animaltypes.clsRobbe)):
            self.status=[10,10,15]
            if self.has_skill(skills.EnduranceCharacterSkill):
                self.status[1]+=20
        self.temp_status = self.status[:]

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