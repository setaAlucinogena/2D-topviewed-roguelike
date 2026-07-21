


from game_manager import *
from ursina import *
from ursina.prefabs.conversation import Conversation

class DialogueScene:
    game_manager = None
    def __init__(self,background = None,conversation_text=None,animation_texture_name=None,convo_variables = None):
        #self.conversation_text = conversation_text
        self.conversation_text = dedent('''
You look pale and you smell like beer
What's wrong with you?
    * That's very rude.
        Yeah that's right I'm sorry (ended += True)
        
            
    * Me cago en tu puta madre y toda tu familia (ended += True)
''')
        
        #x si aca

        self.animation = SpriteSheetAnimation(animation_texture_name, parent = camera.ui,autoplay=False,eternal = True,scale = .5,loop = False,model = "quad",tileset_size=(1,1), fps=8, position = (0,0,-.1) ,animations = {'idle':((0,0),(0,0))})

        self.animation.enabled = False
        #self.animation.visible = False
        
        self.background = background
        self.conversation = None
        #
        self.back_button = None
        self.convo_variables = convo_variables
    

    def initiate(self):
        self.back_button = Button(model='quad', scale=.05, color=color.lime, text='back', text_size=.5, text_color=color.black,parent = camera.ui, position = (-.5,.45,-.3))#sera una fletxa
        self.back_button.on_click = self.end


        self.animation.enabled = True
        #self.animation.start()
        self.animation.play_animation('idle')
        self.game_manager.game_status = GameState.PAUSE
        if self.background == None:
            self.curtains = Entity(model = "quad",color = color.black, scale = 5,position = (0,0,0),parent = camera.ui,texture = self.background)
        else:
            self.curtains = Entity(model = "quad", scale = 2,position = (0,0,0),parent = camera.ui,texture = self.background)
        
        
        self.conversation = Conversation(variables_object=self.convo_variables)
        self.conversation.parse_conversation(self.conversation_text)
        self.conversation.start_conversation(self.conversation_text)
        self.conversation.z = -.2

    def end(self):
        self.animation.disable()
        destroy(self.animation,delay = 0)
        self.animation.visible = False
        destroy(self.curtains,delay = 0)
        destroy(self.back_button,delay = 0)

        self.conversation.enabled = False
        destroy(self.conversation,delay=1)

        self.game_manager.game_status = GameState.RUN

