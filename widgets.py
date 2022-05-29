from typing import Text
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
class kivy_ui(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 1
        self.rows = 4
        self.img = Image(
            source = "dino.png"
        )
        self.add_widget(self.img)
        self.label = Label(
            text = "Name"
        )
        self.add_widget(self.label)

        self.text = TextInput(
            text='',font_size = 40
        )
        self.add_widget(self.text)
        self.button = Button(
            text = "Submit"
        )
        self.button.bind(on_press = self.call_back)
        self.add_widget(self.button)

        self.popup = Popup(
            title = "Popup",
            size_hint = (0.3,0.3),
            content = Label(
                text=''
            )
        )
    def call_back(self,element):
        self.popup.content.text = self.text.text
        self.popup.open()
class DemoApp(App):
    def build(self):
        return kivy_ui()
demoapp = DemoApp()
demoapp.run()