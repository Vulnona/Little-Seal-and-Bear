from character import Character
import character.abilities
import character.animalsubtypes
import character.skills
import character.animaltypes
import settings
import logging
import Helper
import pygame
import sys
import gui


class Editor:
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.window = pygame.display.set_mode(
            settings.WINDOW_SIZE, pygame.DOUBLEBUF | pygame.HWSURFACE)
        self.window_rect = self.window.get_rect()
        self._load_fonts()
        self._load_images()
        self.character = Character()
        # self.character.randomize_all()
        self._load_gui()

        MODE = "CREATE"
        self.MODE = MODE

    def get_Mode(self):
        return self.MODE

    def _load_fonts(self):
        logging.info('Loading fonts')
        self.fonts = {
            'normal': Helper.load_font('celtic_gaelige.ttf', 21)
        }

    def _load_images(self):
        logging.info('Loading images')

        self.images = {
            'window': Helper.load_image('window.png'),
            'validatewindow': Helper.load_image('validatewindow.png'),
            'bearavatar': Helper.load_image('bearavatar.jpg'),
            'sealavatar': Helper.load_image('sealavatar.jpg'),
            'unknown': Helper.load_image('unknown.png'),
            'bearicon': Helper.load_image('bearicon.png'),
            'sealicon': Helper.load_image('sealicon.png'),
            'abilities': {ability.id: Helper.load_image('abilities/' + ability.id + '.png') for ability in character.abilities.ALL},
            'skills': {skill.id: Helper.load_image('skills/' + skill.id + '.png') for skill in character.skills.ALL},
            'animaltypes': {
                'normal': {animaltype.id: Helper.load_image('animaltypes/' + animaltype.id + '.png') for animaltype in character.animaltypes.ALL},
                'active': {animaltype.id: Helper.load_image('animaltypes/' + animaltype.id + '_active.png') for animaltype in character.animaltypes.ALL}
            },
            'animalsubtypes': {
                'normal': {animalsubtype_.id: Helper.load_image('animalsubtypes/' + animalsubtype_.id + '.png') for animalsubtype_ in character.animalsubtypes.ALL},
                'active': {animalsubtype_.id: Helper.load_image('animalsubtypes/' + animalsubtype_.id + '_active.png') for animalsubtype_ in character.animalsubtypes.ALL}
            },
            'buttons': {
                'yes': Helper.load_image('buttons/yes.png'),
                'refresh': Helper.load_image('buttons/refresh.png'),
                'exit': Helper.load_image('buttons/exit.png'),
                'randomize': Helper.load_image('buttons/randomize.png'),
                'save': Helper.load_image('buttons/save.png'),
                'less': Helper.load_image('buttons/links.png'),
                'more': Helper.load_image('buttons/rechts.png')
            }
        }

    def _load_gui(self):
        # AnimalType Buttons
        spacing = 272
        for animaltype in character.animaltypes.ALL:
            animaltype_image_rect = self.images['animaltypes']['normal'][animaltype.id].get_rect(
            )
            animaltype_image_rect.right = spacing
            animaltype_image_rect.top = 110
            gui.add(gui.RadioButton(
                {
                    'normal': self.images['animaltypes']['normal'][animaltype.id],
                    'selected': self.images['animaltypes']['active'][animaltype.id]
                },
                animaltype_image_rect,
                'animaltype',
                animaltype,
                on_click=self._click_animaltype_button,
                selected=isinstance(self.character.animaltype, animaltype)
            ))
            spacing += 50

        # Animalsubtype Buttons
        for animalsubtype in character.animalsubtypes.ALL:
            animalsubtype_image_rect = self.images['animalsubtypes']['normal'][animalsubtype.id].get_rect(
            )
            animalsubtype_image_rect.right = spacing-115
            animalsubtype_image_rect.top = 155
            gui.add(gui.RadioButton(
                {
                    'normal': self.images['animalsubtypes']['normal'][animalsubtype.id],
                    'selected': self.images['animalsubtypes']['active'][animalsubtype.id]
                },
                animalsubtype_image_rect,
                'animalsubtype',
                animalsubtype,
                on_click=self._click_animalsubtype_button,
                selected=isinstance(
                    self.character.animalsubtype, animalsubtype)
            ))
            spacing += 50

        spacing = 250
        posless = 352
        posmore = 308
        lesser_attribute_strength_button_rect = self.images['buttons']['less'].get_rect(
        )
        lesser_attribute_strength_button_rect.top = spacing
        lesser_attribute_strength_button_rect.right = self.window_rect.w-posless
        gui.add(gui.Button(
            self.images['buttons']['less'],
            lesser_attribute_strength_button_rect,
            self._click_lesser_attribute_strength_button
        ))

        more_attribute_strength_button_rect = self.images['buttons']['more'].get_rect(
        )
        more_attribute_strength_button_rect.top = spacing
        more_attribute_strength_button_rect.right = self.window_rect.w-posmore
        gui.add(gui.Button(
            self.images['buttons']['more'],
            more_attribute_strength_button_rect,
            self._click_more_attribute_strength_button
        ))
        spacing += 30
        lesser_attribute_resistance_button_rect = self.images['buttons']['less'].get_rect(
        )
        lesser_attribute_resistance_button_rect.top = spacing
        lesser_attribute_resistance_button_rect.right = self.window_rect.w-posless
        gui.add(gui.Button(
            self.images['buttons']['less'],
            lesser_attribute_resistance_button_rect,
            self._click_lesser_attribute_resistance_button
        ))

        more_attribute_resistance_button_rect = self.images['buttons']['more'].get_rect(
        )
        more_attribute_resistance_button_rect.top = spacing
        more_attribute_resistance_button_rect.right = self.window_rect.w-posmore
        gui.add(gui.Button(
            self.images['buttons']['more'],
            more_attribute_resistance_button_rect,
            self._click_more_attribute_resistance_button
        ))
        spacing += 30
        lesser_attribute_dexterity_button_rect = self.images['buttons']['less'].get_rect(
        )
        lesser_attribute_dexterity_button_rect.top = spacing
        lesser_attribute_dexterity_button_rect.right = self.window_rect.w-posless
        gui.add(gui.Button(
            self.images['buttons']['less'],
            lesser_attribute_dexterity_button_rect,
            self._click_lesser_attribute_dexterity_button
        ))

        more_attribute_dexterity_button_rect = self.images['buttons']['more'].get_rect(
        )
        more_attribute_dexterity_button_rect.top = spacing
        more_attribute_dexterity_button_rect.right = self.window_rect.w-posmore
        gui.add(gui.Button(
            self.images['buttons']['more'],
            more_attribute_dexterity_button_rect,
            self._click_more_attribute_dexterity_button
        ))
        spacing += 30
        lesser_attribute_intelligence_button_rect = self.images['buttons']['less'].get_rect(
        )
        lesser_attribute_intelligence_button_rect.top = spacing
        lesser_attribute_intelligence_button_rect.right = self.window_rect.w-posless
        gui.add(gui.Button(
            self.images['buttons']['less'],
            lesser_attribute_intelligence_button_rect,
            self._click_lesser_attribute_intelligence_button
        ))

        more_attribute_intelligence_button_rect = self.images['buttons']['more'].get_rect(
        )
        more_attribute_intelligence_button_rect.top = spacing
        more_attribute_intelligence_button_rect.right = self.window_rect.w-posmore
        gui.add(gui.Button(
            self.images['buttons']['more'],
            more_attribute_intelligence_button_rect,
            self._click_more_attribute_intelligence_button
        ))
        # Randomize character name button
        randomize_name_button_rect = self.images['buttons']['randomize'].get_rect(
        )
        randomize_name_button_rect.top = 70
        randomize_name_button_rect.right = self.window_rect.w - 20
        gui.add(gui.Button(
            self.images['buttons']['randomize'],
            randomize_name_button_rect,
            self._click_randomize_name_button
        ))

        # Randomize all character attributes button
        # randomize_all_button_rect = self.images['buttons']['randomize'].get_rect()
        # randomize_all_button_rect.bottom = self.window_rect.h - 10
        # randomize_all_button_rect.right = self.window_rect.w - 110
        # gui.add(gui.Button(
        #    self.images['buttons']['randomize'],
        #    randomize_all_button_rect,
        #    self._click_randomize_all_button
        # ))

        # Save Charakterbogen
        save_button_rect = self.images['buttons']['save'].get_rect()
        save_button_rect.bottom = self.window_rect.h - 10
        save_button_rect.right = self.window_rect.w - 60
        gui.add(gui.Button(
            self.images['buttons']['save'],
            save_button_rect,
            self._click_save_button
        ))

        # Exit button
        exit_button_rect = self.images['buttons']['exit'].get_rect()
        exit_button_rect.bottom = self.window_rect.h - 10
        exit_button_rect.right = self.window_rect.w - 10
        gui.add(gui.Button(
            self.images['buttons']['exit'],
            exit_button_rect,
            self._click_exit_button
        ))

    def play_with_this_character(self):
        print("Mit diesem Charakter das Abenteuer bestreiten?")
        back_button_rect = self.images['buttons']['refresh'].get_rect()
        back_button_rect.bottom = self.window_rect.h - 10
        back_button_rect.right = self.window_rect.w - 10

        gui.add(gui.Button(
            self.images['buttons']['refresh'],
            back_button_rect,
            self._click_back_button
        ))

        yes_button_rect = self.images['buttons']['yes'].get_rect()
        yes_button_rect.bottom = self.window_rect.h - 10
        yes_button_rect.right = self.window_rect.w - 10
        gui.add(gui.Button(
            self.images['buttons']['yes'],
            yes_button_rect,
            self._click_yes_button
        ))

        self.MODE = "PLAY"

    def _click_yes_button(self):
        pass

    def _click_back_button(self):
        pass

    def save_character_sheet(self):
        if self.character.get_Name() is not None:
            if self.character.get_Type() is not None:
                if self.character.get_Subtype() is not None:
                    logging.info('Saving character')
                    with open(settings.CHARACTER_SHEET_FILE_NAME, 'w', encoding='utf-8') as f:
                        f.write(str(self.character))
                    self.play_with_this_character()
                else:
                    logging.info('Subtype missing')
            else:
                logging.info('Type missing')
        else:
            logging.info('Name missing')

    def update(self):
        # Events handling
        for event in pygame.event.get():
            event_handlers = [
                self._event_quit,
                gui.event_handler
            ]
            for handler in event_handlers:
                if handler(event):
                    break

        # Drawings
        self.window.blit(self.images['window'],
                         self.images['window'].get_rect())
        self.draw_avatar()
        self._draw_name_input()
        self._draw_abilities()
        self._draw_skills()
        gui.draw(self.window)
        pygame.display.update()
        self.clock.tick(settings.FPS)

    # --------------------------------------------------------------------------
    # Events handlers
    def _event_quit(self, event):
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            pygame.quit()
            sys.exit()
        return False

    def _click_exit_button(self, element):
        pygame.quit()
        sys.exit()

    def _click_lesser_attribute_strength_button(self, element):
        valuetocheck = self.character.Build_Point_Value("strength")
        if int(valuetocheck) > 0:
            self.character.lose_Build_Points("strength")
            self.character.gain_Build_Points(1)
            self.character.set_status_initial()

    def _click_more_attribute_strength_button(self, element):
        if int(self.character.get_Build_Points()) > 0:
            self.character.lower_Build_Points(1)
            self.character.spend_Build_Points("strength")
            self.character.set_status_initial()

    def _click_lesser_attribute_resistance_button(self, element):
        valuetocheck = self.character.Build_Point_Value("resistance")
        if int(valuetocheck) > 0:
            self.character.lose_Build_Points("resistance")
            self.character.gain_Build_Points(1)
            self.character.set_status_initial()

    def _click_more_attribute_resistance_button(self, element):
        if int(self.character.get_Build_Points()) > 0:
            self.character.lower_Build_Points(1)
            self.character.spend_Build_Points("resistance")
            self.character.set_status_initial()

    def _click_lesser_attribute_dexterity_button(self, element):
        valuetocheck = self.character.Build_Point_Value("dexterity")
        if int(valuetocheck) > 0:
            self.character.lose_Build_Points("dexterity")
            self.character.gain_Build_Points(1)
            self.character.set_status_initial()

    def _click_more_attribute_dexterity_button(self, element):
        if int(self.character.get_Build_Points()) > 0:
            self.character.lower_Build_Points(1)
            self.character.spend_Build_Points("dexterity")
            self.character.set_status_initial()

    def _click_lesser_attribute_intelligence_button(self, element):
        valuetocheck = self.character.Build_Point_Value("intelligence")
        if int(valuetocheck) > 0:
            self.character.lose_Build_Points("intelligence")
            self.character.gain_Build_Points(1)
            self.character.set_status_initial()

    def _click_more_attribute_intelligence_button(self, element):
        if int(self.character.get_Build_Points()) > 0:
            self.character.lower_Build_Points(1)
            self.character.spend_Build_Points("intelligence")
            self.character.set_status_initial()

    def _click_randomize_name_button(self, element):
        self.character.randomize_Name()

    # def _click_randomize_all_button(self, element):
    #    self.character.randomize_all()

    def _click_save_button(self, element):
        self.save_character_sheet()

    def _click_animaltype_button(self, element):
        self.character.set_Type(element.value)
        self.character.set_status_initial()

    def _click_animalsubtype_button(self, element):
        self.character.set_Subtype(element.value)

    # --------------------------------------------------------------------------
    # Drawing handlers
    def draw_avatar(self):
        if (isinstance(self.character.get_Type(), character.animaltypes.clsRobbe)):
            seal = pygame.image.load(
                './resources/images/sealavatar.jpg').convert()
            # seal=self.images('sealavatar')
            seal = pygame.transform.scale(seal, (155, 150))
            self.window.blit(seal, (50, 42))
        elif (isinstance(self.character.get_Type(), character.animaltypes.clsBaer)):
            bear = pygame.image.load(
                './resources/images/bearavatar.jpg').convert()
            bear = pygame.transform.scale(bear, (155, 150))
            self.window.blit(bear, (50, 42))

    def _draw_name_input(self):
        name_text = self.fonts['normal'].render(
            self.character.get_Name(), True, settings.TEXT_COLOR)
        name_text_rect = name_text.get_rect()
        name_text_rect.left = 320
        name_text_rect.top = 80
        # print(self.character.get_Name())
        self.window.blit(name_text, name_text_rect)

    def _draw_abilities(self):
        spacing = 250
        for ability in character.abilities.ALL:
            ability_image = self.images['abilities'][ability.id]
            ability_image_rect = ability_image.get_rect()
            ability_image_rect.left = 28
            ability_image_rect.top = spacing

            self.window.blit(ability_image, ability_image_rect)

            ability_text = self.fonts['normal'].render(
                ability.name, True, settings.TEXT_COLOR)
            ability_text_rect = ability_text.get_rect()
            ability_text_rect.left = 55
            ability_text_rect.top = spacing

            self.window.blit(ability_text, ability_text_rect)

            ability_value = self.fonts['normal'].render(str(
                getattr(self.character.abilities, ability.id).value), True, settings.TEXT_COLOR)
            ability_value_rect = ability_value.get_rect()
            ability_value_rect.left = 252
            ability_value_rect.top = spacing
            self.window.blit(ability_value, ability_value_rect)
            spacing += 30

    def _draw_skills(self):
        spacing = 250
        for skill in self.character.skills:
            # for skill in character.skills.ALL:
            skill_image = self.images['skills'][skill.id]
            skill_image_rect = skill_image.get_rect()
            skill_image_rect.left = 320
            skill_image_rect.top = spacing

            self.window.blit(skill_image, skill_image_rect)

            skill_text = self.fonts['normal'].render(
                skill.name, True, settings.TEXT_COLOR)
            skill_text_rect = skill_text.get_rect()
            skill_text_rect.left = 345
            skill_text_rect.top = spacing
            self.window.blit(skill_text, skill_text_rect)
            spacing += 30
