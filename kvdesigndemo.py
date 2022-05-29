from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty
class demo(GridLayout):
    name = ObjectProperty(None)
    age = ObjectProperty(None)

    def on_click(self):
        print("My name is {} and i am {} yars old".format(self.name.text,self.age.text))

        self.name.text=""
        self.age.text=""
class myfirstkvapp(App):
    def build(self):
        return demo()
myfirstkvapp().run()