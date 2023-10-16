from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.uix.button import Button


class Pistol:
    damage = 10
    bullet_speed = 100


deagle = Pistol()
m1911 = Pistol()

deagle.damage = Pistol.damage * 6
deagle.bullet_speed = Pistol.bullet_speed * 5

m1911.damage = Pistol.damage * 3.4
m1911.bullet_speed = Pistol.bullet_speed * 3


KV = """
MyBL:
    orientation: "vertical"
    size_hint: (0.95, 0.95)
    pos_hint: {"center_x":0.5, "center_y":0.5}
    
    Label:
        font_size: "30sp"
        text: root.data_label
    
    TextInput:
        id: Inp
        multiline: False
        padding_y:(5,5)
        size_hint:(1,0.3)
        
    Button:
        text: "Поиск по названию"
        bold: True
        background_color:'#32E317'
        size_hint: (1, 0.6)
        on_press: root.callback()
        
    Button:
        text: "Deagle"
        bold: True
        background_color:'#32E317'
        size_hint: (1, 0.5)
        on_press: root.callback1()
        
    Button:
        text: "M1911"
        bold: True
        background_color:'#32E317'
        size_hint: (1, 0.5)
        on_press: root.callback2()
        
"""

class MyBL(BoxLayout):

    data_label = StringProperty("PICK YOUR GUN")

    def callback(self):
        print("Введите название в консоль")

    def callback1(self):
        print(f'{"Deagle:"} {deagle.__dict__}')

    def callback2(self):
        print(f'{"M1911"} {m1911.__dict__}')


class MyApp(App):

    running = True

    def build(self):

        return Builder.load_string(KV)

    def on_stop(self):
        self.running = False

MyApp().run()
