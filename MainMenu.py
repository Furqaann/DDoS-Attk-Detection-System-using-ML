from kivy.app import App
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
            rgba: (70/255,81/255,83/255,1)
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
                background_color:(70/255,81/255,83/255,1)
                background_normal:''
                on_release:
                    app.root.current = "home"
                Image:
                    source:"images/home.png"
                    center_x: self.parent.center_x
                    center_y: self.parent.center_y
                
            
            Button:
                id:btn_acquisition
                size_hint_x:0.99
                background_color:(70/255,81/255,83/255,1)
                background_normal:''
                on_release:
                    app.root.current = "z"
                Image:
                    source:"images/acquisition.png"
                    center_x: self.parent.center_x
                    center_y: self.parent.center_y
                    width:50
                    height:50     
                
                
            Button:
                id:btn_feature
                size_hint_x:0.99
                background_color:(70/255,81/255,83/255,1)
                background_normal:''
                Image:
                    source:"images/feature.png"
                    center_x: self.parent.center_x
                    center_y: self.parent.center_y
                    width:50
                    height:50
            
            Button:
                id:btn_machinelearning
                size_hint_x:0.99
                background_color:(70/255,81/255,83/255,1)
                background_normal:''
                Image:
                    source:"images/machine_learning.png"
                    center_x: self.parent.center_x
                    center_y: self.parent.center_y
                    width:50
                    height:50
            Button:
                id:btn_model
                size_hint_x:0.99
                background_color:(70/255,81/255,83/255,1)
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
                background_color:(70/255,81/255,83/255,1)
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

                Label:
                    text:"About Project:  "
                    font_size: 24
                    font_name: "Tahoma"
                    size_hint:(0.2,0.2)
                    pos_hint: {"x":0.05,"top":1}
                
                FloatLayout:
                    orientation: "horizontal"
		            size: root.width, root.height
                
                    Label:
                        text:"Machine Learning Based DDoS attack detection system which detects any malicios data packets"
                        font_size: 16
                        font_name: "Tahoma"
                        size_hint:(0.2,0.2)
                        pos_hint: {"x":0.5,"top":0.91}

                    Label:
                        text:"entering into network which could crash the server and make it unavailable for the end user."
                        font_size: 16
                        font_name: "Tahoma"
                        size_hint:(0.2,0.2)
                        pos_hint: {"x":0.495,"top":0.86}

                Label:
                    text:"Vision: "
                    font_size: 24
                    font_name: "Tahoma"
                    size_hint:(0.2,0.2)
                    pos_hint: {"x":0.02,"top":0.73}
              
                Label:
                    text:"To make a system which would detect DDoS attack threats by analyzing the data packets"
                    font_size: 16
                    font_name: "Tahoma"
                    size_hint:(0.2,0.2)
                    pos_hint: {"x":0.36,"top":0.68}

                Label:
                    text:" by analyzing the data packets Effectivly and Efficiently. "
                    font_size: 16
                    font_name: "Tahoma"
                    size_hint:(0.2,0.2)
                    pos_hint: {"x":0.275,"top":0.62}

                Label:
                    text:"Models Used: "
                    font_size: 24
                    font_name: "Tahoma"
                    size_hint:(0.2,0.2)
                    pos_hint: {"x":0.05,"top":0.52}

                Label:
                    text:"A total of 3 Feature Selection techniques are used to select best features from dataset to build"
                    font_size: 16
                    font_name: "Tahoma"
                    size_hint:(0.2,0.2)
                    pos_hint: {"x":0.38,"top":0.42}

                Label:
                    text:"a classifier. 11 Different Supervised, Unsupervised and Semi-Supervised Machine learning"
                    font_size: 16
                    font_name: "Tahoma"
                    size_hint:(0.2,0.2)
                    pos_hint: {"x":0.371,"top":0.37}
                Label:
                    text:"techniques are used to build a classifier which would classify both benign and malicious data packets."
                    font_size: 16
                    font_name: "Tahoma"
                    size_hint:(0.2,0.2)
                    pos_hint: {"x":0.4,"top":0.32}


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

class Home_PageApp(App):
    def build(self):
            sm = ScreenManager()
            sm.add_widget(Home_PageWindow())
            return sm

if __name__=='__main__':
    Home_PageApp().run()