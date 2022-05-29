from kivy.app import App
from kivy.uix.pagelayout import PageLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class Page_Layout_demo(PageLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.button1 = Button(
            text="hi"
        )
        self.add_widget(self.button1)
        self.button2 = Button(
            text="h"
        )
        self.add_widget(self.button2)
        self.button3 = Button(
            text="hii"
        )
        self.add_widget(self.button3)
class DemoApp(App):
    def build(self):
        return Page_Layout_demo()
demoapp = DemoApp()
demoapp.run()