from kivy.app import App
from kivy.uix.label import Label
class DemoApp(App):
    def build(self):
        return Label(
            text = "Hello Program using kivy"
        )
demoapp = DemoApp()
demoapp.run()