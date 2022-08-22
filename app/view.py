from kivy.uix.boxlayout import BoxLayout
from kivy.uix.behaviors import ToggleButtonBehavior
from kivy.properties import StringProperty
from kivy.uix.screenmanager import ScreenManager

class MainWindow(BoxLayout):
    username = StringProperty("Usuario")
    def __init__(self, **kw):
        super().__init__(**kw)
    def on_press_home(self):
        self.ids.scrn_mngr.current = "scrn_home"

class ViewManager(ScreenManager):
    def __init__(self, **kw):
        super().__init__(**kw)

class NavTab(ToggleButtonBehavior, BoxLayout):
    text = StringProperty('')
    icon = StringProperty('')
    def __init__(self, **kw):
        super().__init__(**kw)