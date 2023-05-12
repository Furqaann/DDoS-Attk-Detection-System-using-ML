from kivymd.app import MDApp
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.behaviors import ButtonBehavior

# Designate Our .kv design file 
Builder.load_string("""

<Home_PageWindow>:
    name:"home"
    id: main_win
    orientation: 'vertical'
    canvas.before:
        Color:
            rgba: (30/255,35/255,36/255,1)
        Rectangle:
            size: self.size
            pos: self.pos

    BoxLayout:
        id: content_nav
        
        BoxLayout:
            id: nav_tabs
            size_hint_x:0.1
            pos_hint:{"x":0.1}
            orientation: 'vertical'
            spacing: 1
            
            canvas.before:
                Color:
                    rgba: (1,1,1,1)
                Rectangle:
                    size: self.size
                    pos: self.pos
                Color:
                    rgba: (1,1,1,1)
                Rectangle:
                    size: self.width-1, self.height
                    pos: self.x, self.y

            Button:
                id:btn_home
                size_hint_x:0.99
                background_color:(55/255,61/255,62/255,1)
                background_normal:''
                on_release:
                    app.root.current = "home"
                    root.manager.transition.direction = 'left'
                Image:
                    source:"images/home.png"
                    center_x: self.parent.center_x
                    center_y: self.parent.center_y
                
            
            Button:
                id:btn_acquisition
                size_hint_x:0.99
                background_color:(30/255,35/255,36/255,1)
                background_normal:''
                on_release:
                    app.root.current = "z"
                    root.manager.transition.direction = 'left'
                Image:
                    source:"images/acquisition.png"
                    center_x: self.parent.center_x
                    center_y: self.parent.center_y
                    width:50
                    height:50     
                
                
            Button:
                id:btn_feature
                size_hint_x:0.99
                background_color:(30/255,35/255,36/255,1)
                background_normal:''
                on_release:
                    app.root.current = "featureselection"
                    root.manager.transition.direction = 'left'
                Image:
                    source:"images/feature.png"
                    center_x: self.parent.center_x
                    center_y: self.parent.center_y
                    width:50
                    height:50
            
            Button:
                id:btn_machinelearning
                size_hint_x:0.99
                background_color:(30/255,35/255,36/255,1)
                background_normal:''
                on_release:
                    app.root.current = "mainwin"
                    root.manager.transition.direction = 'left'
                Image:
                    source:"images/machine_learning.png"
                    center_x: self.parent.center_x
                    center_y: self.parent.center_y
                    width:50
                    height:50
            Button:
                id:btn_model
                size_hint_x:0.99
                background_color:(30/255,35/255,36/255,1)
                background_normal:''
                Image:
                    source:"images/testmodel.png"
                    center_x: self.parent.center_x
                    center_y: self.parent.center_y
                    width:50
                    height:50
            
            Button:
                id:btn_visualize
                size_hint_x:0.99
                background_color:(30/255,35/255,36/255,1)
                background_normal:''
                Image:
                    source:"images/visualize.png"
                    center_x: self.parent.center_x
                    center_y: self.parent.center_y
                    width:50
                    height:50
       
        BoxLayout:
            id: content
            size_hint_x: 0.8
            FloatLayout:
                orientation: "horizontal"
		        size: root.width, root.height
                  
                Image:
                    source: 'images/home.png'
                    size_hint:(0.1,0.1)
                    pos_hint: {"x":0.3,"y":0.88}
                    size: self.texture_size

                Label:
                    text:" Home Screen "
                    font_size: 30
                    font_name: 'Font/Poppins-Medium.ttf'
                    pos_hint: {"x":0.1,"y":0.43}

                Label:
                    text:"About Project:  "
                    font_size: 24
                    font_name: 'Font/Poppins-Medium.ttf'
                    size_hint:(0.1,0.2)
                    pos_hint: {"x":0.1,"y":0.7}
                
                FloatLayout:
                    orientation: "horizontal"
		            size: root.width, root.height
                
                    Label:
                        text:"Machine Learning Based DDoS attack detection system which detects any malicios data packets"
                        font_size: 15
                        font_name: "Tahoma"
                        size_hint:(0.2,0.2)
                        pos_hint: {"x":0.57,"y":0.63}

                    Label:
                        text:"entering into network which could crash the server and make it unavailable for the end user."
                        font_size: 15
                        font_name: "Tahoma"
                        size_hint:(0.2,0.2)
                        pos_hint: {"x":0.559,"y":0.58}

                Label:
                    text:"Vision: "
                    font_size: 24
                    font_name: 'Font/Poppins-Medium.ttf'
                    size_hint:(0.2,0.2)
                    pos_hint: {"x":0.02,"y":0.49}
              
                Label:
                    text:"To make a system which would detect DDoS attack threats by analyzing the data packets"
                    font_size: 15
                    font_name: "Tahoma"
                    size_hint:(0.2,0.2)
                    pos_hint: {"x":0.43,"y":0.42}

                Label:
                    text:"by analyzing the data packets Effectivly and Efficiently.                                             "
                    font_size: 15
                    font_name: "Tahoma"
                    size_hint:(0.2,0.2)
                    pos_hint: {"x":0.43,"y":0.37}

                Label:
                    text:"Models Used: "
                    font_size: 24
                    font_name: 'Font/Poppins-Medium.ttf'
                    size_hint:(0.2,0.2)
                    pos_hint: {"x":0.05,"y":0.29}

                Label:
                    text:"A total of 3 Feature engineering techniques are used to select best features from dataset"
                    font_size: 15
                    font_name: "Tahoma"
                    size_hint:(0.2,0.2)
                    pos_hint: {"x":0.43,"y":0.22}

                Label:
                    text:"to build a classifier. 10 Different Supervised Machine learning techniques are used to      "
                    font_size: 15
                    font_name: "Tahoma"
                    size_hint:(0.2,0.2)
                    pos_hint: {"x":0.43,"y":0.17}


                Label:
                    text:"build a classifier which would classify both benign and malicious data packets.               "
                    font_size: 15
                    font_name: "Tahoma"
                    size_hint:(0.2,0.2)
                    pos_hint: {"x":0.43,"y":0.12}

                RoundedButton:
                    font_size:18
                    text: "Back"
                    color: (1,1,1,1)
                    size_hint:(0.15,0.06)
                    pos_hint: {"x":0.08,"top":0.1} 
                    canvas.before:
                        Color:
                            rgba:(1, 0, 0,1)
                        RoundedRectangle:
                            size:   self.size
                            pos:    self.pos
                            radius: [20] 
                    on_release:
                        root.manager.transition.direction = 'right'
                        app.root.current = "start"                 

                RoundedButton:
                    font_size:18
                    text: "Next"
                    color: (1,1,1,1)
                    size_hint:(0.15,0.06)
                    pos_hint: {"x":0.8,"top":0.1}
                    on_press:
                        root.manager.transition.direction = 'left'
                        root.manager.current = "z"       
                    
                
<RoundedButton@Button>
    background_color:(0,0,0,0)
    background_normal:''
    canvas.before:
        Color:
            rgba:(0/255, 148/255, 255/255,1)
        RoundedRectangle:
            size:   self.size
            pos:    self.pos
            radius: [20]
""")


class Home_PageWindow(Screen, ButtonBehavior):
    pass

class Home_PageApp(MDApp):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(Home_PageWindow())
        return sm

if __name__=='__main__':
    Home_PageApp().run()