from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button
class DemoApp(App):
    def build(self):
        layout = AnchorLayout(
            anchor_x = 'left',anchor_y = 'top'
        )
        button = Button(
            text = "Anchor layout",
            size_hint = (.2,.2),
            background_color = (230,250,30),
            color = (0,0,0,1)
        )
        layout.add_widget(button)
        return layout
    
demoapp = DemoApp()
demoapp.run()
