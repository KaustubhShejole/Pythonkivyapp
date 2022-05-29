from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class Float_Layout_demo(FloatLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.button1 = Button(
            text = "hi",
            size_hint = (0.4,0.4),
            pos_hint = {"x":0.3,"y":0.5}
        )
        self.add_widget(self.button1)
        self.button2 = Button(
            text = "hii",
            size_hint = (0.1,0.1),
            pos_hint = {"x":0.9,"y":0.9}
        )
        self.add_widget(self.button2)
class DemoApp(App):
    def build(self):
        return Float_Layout_demo()
demoapp = DemoApp()
demoapp.run()