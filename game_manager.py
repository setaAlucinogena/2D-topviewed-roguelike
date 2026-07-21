from enum import Enum
from ursina import *

class GameState(Enum):
    PAUSE = 0
    RUN  = 1


class GameManager:
    def __init__(self):
        self.player = None
        

        self.tick_speed = 1
        self.game_status = GameState.PAUSE
        
        self.ground_z = .1
        self.characters_z = 0
        self.displayed_buttons = []
        

    def change_tick_speed(self,new_speed):
        self.tick_speed = abs(new_speed)#x si aca
    

    def end_pause(self):
        self.game_status = GameState.RUN
        for button in self.displayed_buttons:
            destroy(button,delay = 0)
        self.displayed_buttons = []
    def pause(self):
        self.game_status = GameState.PAUSE
        #self.displayed_buttons.append(Button(model='quad', scale=.05, color=color.lime, text='back', text_size=.5, text_color=color.black,parent = camera.ui, position = (-.5,.45,-.3)))
        #self.displayed_buttons[-1].on_click = self.end_pause

        self.displayed_buttons.append(
            Button(model='quad', scale=(.2,.075), color=color.lime, text='resume', text_size=.5, text_color=color.black,parent = camera.ui, position = (0,.05,-.3))
            )
        self.displayed_buttons[-1].on_click = self.end_pause

        self.displayed_buttons.append(
            Button(model='quad', scale=(.2,.075), color=color.lime, text='main menu', text_size=.5, text_color=color.black,parent = camera.ui, position = (0,-.1,-.3))
            )

        self.displayed_buttons[-1].on_click = self.go_to_main_menu #u sure? not saved changes will be lost


        self.displayed_buttons.append(
            Button(model='quad', scale=(.2,.075), color=color.lime, text='quit game', text_size=.5, text_color=color.black,parent = camera.ui, position = (0,-.25,-.3))
            )

        self.displayed_buttons[-1].on_click = self.quit #u sure? not saved changes will be lost


    def save(self):
        #ha de guardar la vida del jugador, l'espasa, la pistola, els items, l'habitacio en la que es troba... 
        pass

    def go_to_main_menu(self):
        pass

    def quit(self):
        exit()
    
