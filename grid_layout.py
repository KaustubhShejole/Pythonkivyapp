from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
class Grid_Layout(GridLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.rows = 2
        self.col = 1
        self.label1 = Label(
            text = "Hello"
        )
        self.add_widget(self.label1)
        self.button = Button(
            text = "button",
            background_color = (255,255,255,1),
            color = (0,0,89)
        )
        self.add_widget(self.button)
class DemoApp(App):
    def build(self):
        return Grid_Layout()
demoapp = DemoApp()
demoapp.run()
