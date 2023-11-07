from kivy.uix.screenmanager import SlideTransition

class CustomSlideTransition(SlideTransition):
    def __init__(self, direction):
        super().__init__()
        self.direction = direction
