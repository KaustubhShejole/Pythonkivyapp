from cgitb import text
from faulthandler import disable
from itertools import tee
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.properties import ObjectProperty
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.lang import Builder
from kivy.core.window import Window
import random

#First PopUp
class MyPopUp(Popup):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.l1 = Button(
            text="Click here",
            background_color="pink"
        )
        self.l1.bind(on_press = self.button_action)
        self.size_hint = (0.5,0.5)
        self.title = "Toss Phase"
        self.add_widget(self.l1)

    def button_action(self,instance):
        self.dismiss()
#Game Result Popup
class ResultPopUp(Popup):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.l1 = Button(
            text="Result button",background_color="white"
        )
        self.size_hint = (0.5,0.5)
        self.title = "Result Phase"
        self.add_widget(self.l1)

    def button_action(self,instance):
        self.dismiss()
#firstwindow
class FirstWindow(Screen):
    def show(self):
        player1_name = ObjectProperty(None)
        player2_name = ObjectProperty(None)
    def shownow(self):
        self.toss = [self.player1_name,self.player2_name]
        r = random.randint(0,1)
        return self.toss[r]
    def open_popup(self):
        pop = MyPopUp()
        pop.l1.text=str(self.shownow()+' Won the toss')
        tee = str(self.shownow())
        pop.open()
class tab2(GridLayout):
    def __init__(self, **kwargs):
        self.opt=['0','X']
        super().__init__(**kwargs)
        self.count = 0
        self.padding = (20,20)
        self.current_value=2
        self.cols=3
        self.rows=4
        self.done = False
        self.label = Button(text="Choose either X or 0",font_size = 18)
        self.add_widget(self.label)
        self.input_opt = TextInput(font_size = 100)
        self.add_widget(self.input_opt)
        self.button = Button(text="Enter")
        self.button.bind(on_press=self.button_action)
        self.add_widget(self.button)
        
        self.spacing = (5,5)
        self.b1 = Button(text="",font_size=150,background_color=(1,1,1,1))
        self.b1.bind(on_press = self.bact1)
        self.add_widget(self.b1)
        self.b2 = Button(text="",font_size=150)
        self.b2.bind(on_press = self.bact2)
        self.add_widget(self.b2)
        self.b3 = Button(text="",font_size=150,background_color=(1,1,1,1))
        self.b3.bind(on_press = self.bact3)
        self.add_widget(self.b3)
        self.b4 = Button(text="",font_size=150,background_color=(1,1,1,1))
        self.b4.bind(on_press = self.bact4)
        self.add_widget(self.b4)
        self.b5 = Button(text="",font_size=150,background_color=(1,1,1,1))
        self.b5.bind(on_press = self.bact5)
        self.add_widget(self.b5)
        self.b6 = Button(text="",font_size=150,background_color=(1,1,1,1))
        self.b6.bind(on_press = self.bact6)
        self.add_widget(self.b6)
        self.b7 = Button(text="",font_size=150,background_color=(1,1,1,1))
        self.b7.bind(on_press = self.bact7)
        self.add_widget(self.b7)
        self.b8 = Button(text="",font_size=150,background_color=(1,1,1,1))
        self.b8.bind(on_press = self.bact8)
        self.add_widget(self.b8)
        self.b9 = Button(text="",font_size=150,background_color=(1,1,1,1))
        self.b9.bind(on_press = self.bact9)
        self.add_widget(self.b9)
        self.all(True)
    
    def button_action(self,instance):
        self.all(True)
        a = self.input_opt.text
        a = str(a)
        a = a.lower()

        if a=='x' or a=='0':
            self.done = True
            self.all(False)
            if a=='x':
                self.current_value=1
            else:
                self.current_value=0
        else:
            print("Invalid entry")
            self.all(True)
            self.input_opt.text = ""
    def bact1(self,instance):
        self.result()
        self.count +=1
        self.b1.text = self.opt[self.current_value]
        if self.current_value == 1:
            self.current_value = 0
        elif self.current_value==0:
            self.current_value = 1
        self.b1.disabled = True
        self.result()

    def bact2(self,instance):
        self.result()
        self.count +=1
        self.b2.text = self.opt[self.current_value]
        if self.current_value == 1:
            self.current_value = 0
        elif self.current_value==0:
            self.current_value = 1
        self.b2.disabled = True
        self.result()
    def bact3(self,instance):
        self.result()
        self.count +=1
        self.b3.text = self.opt[self.current_value]
        if self.current_value == 1:
            self.current_value = 0
        elif self.current_value==0:
            self.current_value = 1
        self.b3.disabled = True
        self.result()
    def bact4(self,instance):
        self.result()
        self.count +=1
        self.b4.text = self.opt[self.current_value]
        if self.current_value == 1:
            self.current_value = 0
        elif self.current_value==0:
            self.current_value = 1
        self.b4.disabled = True
        self.result()
    def bact5(self,instance):
        self.result()
        self.count +=1
        self.b5.text = self.opt[self.current_value]
        if self.current_value == 1:
            self.current_value = 0
        elif self.current_value==0:
            self.current_value = 1
        self.b5.disabled = True
        self.result()
    def bact6(self,instance):
        self.result()
        self.count +=1
        self.b6.text = self.opt[self.current_value]
        if self.current_value == 1:
            self.current_value = 0
        elif self.current_value==0:
            self.current_value = 1
        self.b6.disabled = True
        self.result()
    def bact7(self,instance):
        self.result()
        self.count +=1
        self.b7.text = self.opt[self.current_value]
        if self.current_value == 1:
            self.current_value = 0
        elif self.current_value==0:
            self.current_value = 1
        self.b7.disabled = True
        self.result()
    def bact8(self,instance):
        self.result()
        self.count +=1
        self.b8.text = self.opt[self.current_value]
        if self.current_value == 1:
            self.current_value = 0
        elif self.current_value==0:
            self.current_value = 1
        self.b8.disabled = True
        self.result()
    def bact9(self,instance):
        self.result()
        self.count +=1
        self.b9.text = self.opt[self.current_value]
        if self.current_value == 1:
            self.current_value = 0
        elif self.current_value==0:
            self.current_value = 1
        self.b9.disabled = True
        self.result()
    def all(self,value):
        self.b1.disabled = value
        self.b2.disabled = value
        self.b3.disabled = value
        self.b4.disabled = value
        self.b5.disabled = value
        self.b6.disabled = value
        self.b7.disabled = value
        self.b8.disabled = value
        self.b9.disabled = value
    def result(self):
        if self.b1.text.lower() == "x" and self.b2.text.lower() == "x" and self.b3.text.lower() == "x":
            self.all(True)
            self.ans = 'X is the Winner'
            self.back()
        elif self.b4.text.lower() == "x" and self.b5.text.lower() == "x" and self.b6.text.lower() == "x":
            self.all(True)
            self.ans = 'X is the Winner'
            self.back()
        elif self.b7.text.lower() == "x" and self.b8.text.lower() == "x" and self.b9.text.lower() == "x":
            self.all(True)
            self.ans = 'X is the Winner'
            self.back()
        elif self.b1.text.lower() == "x" and self.b4.text.lower() == "x" and self.b7.text.lower() == "x":
            self.all(True)
            self.ans = 'X is the Winner'
            self.back()
        elif self.b2.text.lower() == "x" and self.b5.text.lower() == "x" and self.b8.text.lower() == "x":
            self.all(True)
            self.ans = 'X is the Winner'
            self.back()
        elif self.b3.text.lower() == "x" and self.b6.text.lower() == "x" and self.b9.text.lower() == "x":
            self.all(True)
            self.ans = 'X is the Winner'
            self.back()
        elif self.b1.text.lower() == "x" and self.b5.text.lower() == "x" and self.b9.text.lower() == "x":
            self.all(True)
            self.ans = 'X is the Winner'
            self.back()
        elif self.b3.text.lower() == "x" and self.b5.text.lower() == "x" and self.b7.text.lower() == "x":
            self.all(True)
            self.ans = 'X is the Winner'
            self.back()
        if self.b1.text.lower() == "0" and self.b2.text.lower() == "0" and self.b3.text.lower() == "0":
            self.all(True)
            self.ans = '0 is the Winner'
            self.back()
        elif self.b4.text.lower() == "0" and self.b5.text.lower() == "0" and self.b6.text.lower() == "0":
            self.all(True)
            self.ans = '0 is the Winner'
            self.back()
        elif self.b7.text.lower() == "0" and self.b8.text.lower() == "0" and self.b9.text.lower() == "0":
            self.all(True)
            self.ans = '0 is the Winner'
            self.back()
        elif self.b1.text.lower() == "0" and self.b4.text.lower() == "0" and self.b7.text.lower() == "0":
            self.all(True)
            self.ans = '0 is the Winner'
            self.back()
        elif self.b2.text.lower() == "0" and self.b5.text.lower() == "0" and self.b8.text.lower() == "0":
            self.all(True)
            self.ans = '0 is the Winner'
            self.back()
        elif self.b3.text.lower() == "0" and self.b6.text.lower() == "0" and self.b9.text.lower() == "0":
            self.all(True)
            self.ans = '0 is the Winner'
            self.back()
        elif self.b1.text.lower() == "0" and self.b5.text.lower() == "0" and self.b9.text.lower() == "0":
            self.all(True)
            self.ans = '0 is the Winner'
            self.back()
        elif self.b3.text.lower() == "0" and self.b5.text.lower() == "0" and self.b7.text.lower() == "0":
            self.all(True)
            self.ans = '0 is the Winner'
            self.back()
        if self.count==9:
            self.ans = "Match Tied"
            self.back()
    def back(self):
        pop = ResultPopUp()
        pop.l1.text = self.ans
        pop.open()
class SecondWindow(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.add_widget(tab2())

class Manager(ScreenManager):
    pass
kv = Builder.load_file('MyRoot.kv')

class MyRootApp(App):
    def build(self):
        self.title = "tic tac toe"
        return kv
if __name__ =='__main__':
    MyRootApp().run()