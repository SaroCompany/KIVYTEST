from kivy.app import App
from kivy.utils import QueryDict, rgba
from kivy.core.window import Window
from .view import MainWindow

Window.minimum_width = 500
Window.minimum_height = 650
Window.maximize()

class MyProgramApp(App):
    colors = QueryDict()
    colors.primary = rgba('#2D9CDB')
    colors.secondary = rgba('#16213E')
    colors.succes = rgba('#1FC98E')
    colors.warning = rgba('#F2C94C')
    colors.danger = rgba('#E85757')
    colors.grey_dark = rgba('#C4C4C4')
    colors.grey_light = rgba('#F5F5F5')
    colors.black = rgba('#A1A1A1')
    colors.white = rgba('#FFFFFF')

    def build(self):
        return MainWindow()