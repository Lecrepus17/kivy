from kivy.uix.screenmanager import SlideTransition

# Definindo uma classe personalizada que herda de SlideTransition
class CustomSlideTransition(SlideTransition):
    def __init__(self, direction):
        super().__init__()
        self.direction = direction  # Define a direção da transição
