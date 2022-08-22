from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.factory import Factory
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.app import App

Builder.load_file('views/home/home.kv')

class Home(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def open_popup(self):
        Factory.SomePopup().open()

class SomePopup(Popup):
    def __init__(self, **kw):
        super().__init__(**kw)
    
    def modify_home_box(self):
        my_box = App.current_app().ids.scrn_mngr("scrn_home").ids.home_box
        custom_button = Button(
            text = "something"
        )
        my_box.add_widget(custom_button)