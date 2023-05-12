from kivy.app import App
from kivymd.app import MDApp
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.checkbox import CheckBox
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.uix.label import Label
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import OneLineListItem
from plyer import filechooser
from kivy.clock import Clock
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg


# Designate Our .kv design file 
Builder.load_string("""
<visualizationWindow>:
    name:"visualize"
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
            size_hint_x:0.12
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
                    width:60
                    height:60
                
            
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
            # canvas.before:
            #     Color:
            #         rgba:(1,1,1,1)     
            #     RoundedRectangle:
            #         size: self.size
            #         pos: self.pos
            #         radius:[20]

            ScreenManager:
                id: sm
                Screen:
                    name: "upload_window"
                    Label:
                        text:"Please Select a file from the Computer"
                        font_size:"22sp"
                        pos_hint:{"x":0,"top":1.4}
                    Button:
                        id: upload_btn
                        size_hint:(0.15,0.2)
                        background_normal:''
                        background_color:(1,1,1,1)
                        pos_hint:{"x":0.4,"top":0.6}
                        on_press: root.upload_menu()
                        Image:
                            source:"images/Drag.png"
                            center_x: self.parent.center_x
                            center_y: self.parent.center_y


                    Button:
                        font_size:18
                        text: "Back"
                        color: (1,1,1,1)
                        size_hint:(0.15,0.06)
                        pos_hint: {"x":0.1,"top":0.1} 
                        background_color:(0,0,0,0)
                        background_normal:''
                        canvas.before:
                            Color:
                                rgba:(1,0,0,1)
                            RoundedRectangle:
                                size:   self.size
                                pos:    self.pos
                                radius: [20] 
                        on_release:
                            root.manager.transition.direction = 'right'
                            app.root.current = "start"                 

                    Button:
                        font_size:18
                        text: "Next"
                        color: (1,1,1,1)
                        size_hint:(0.15,0.06)
                        pos_hint: {"x":0.83,"top":0.1}
                        background_color:(0,0,0,0)
                        background_normal:''
                        canvas.before:
                            Color:
                                rgba:(0/255, 148/255, 255/255,1)
                            RoundedRectangle:
                                size:   self.size
                                pos:    self.pos
                                radius: [20]
                        on_press:
                            root.manager.transition.direction = 'left'
                            root.switching()

                Screen:
                    name: "visualizer_window"
                    BoxLayout:
                        size_hint_x:0.15

                        canvas.before:
                            Color:
                                rgba: (1,0,0,1)
                            Rectangle:
                                size: self.size
                                pos: self.pos
                            
                        BoxLayout:
                            orientation: "vertical"
                            size_hint:(0.25, 1)
                            canvas.before:
                                Color:
                                    rgba: (0,0,1,1)
                                Rectangle:
                                    size: self.size
                                    pos: self.pos
                            BoxLayout:
                                size_hint: (1,0.5)
                                orientation: "vertical"
                                canvas.before:
                                    Color:
                                        rgba: (1,0,0,1)
                                    Rectangle:
                                        size: self.size
                                        pos: self.pos
                                Label:
                                    markup: True
                                    text: "Files"
                                    size_hint:(1,0.1)
                                    font_size: "22sp"
                                BoxLayout:
                                    size_hint:(1,.85)
                                    canvas.before:
                                        Color:
                                            rgba: (0,1,0,1)
                                        Rectangle:
                                            size: self.size
                                            pos: self.pos
                                    ScrollView:
                                        GridLayout:
                                            id: file_placeholder
                                            size_hint_y:None
                                            height: self.minimum_height
                                            cols:1
                            BoxLayout:
                                size_hint: (1,.5)
                                orientation: "vertical"
                                canvas.before:
                                    Color:
                                        rgba: (0,0,1,1)
                                    Rectangle:
                                        size: self.size
                                        pos: self.pos
                                Label:
                                    markup: True
                                    text: "Attributes"
                                    size_hint:(1,.15)
                                    font_size: "20sp"
                                BoxLayout:
                                    size_hint:(1,.85)
                                    ScrollView:
                                        GridLayout:
                                            id: property_placeholder
                                            size_hint_y:None
                                            height: self.minimum_height
                                            cols:1 

                    FloatLayout:
                        orientation:"vertical"
                        size_hint:(0.85,0.1)
                        Label:
                            markup:True
                            text:"Data Visualization"
                            color:(1,0,0,1)
                            font_size: "32sp"
                            pos_hint:{"x":0.175,"top":10}
                            canvas.before:
                                Color:
                                    rgba: (0,0,1,1)
                                Rectangle:
                                    size: self.size
                                    pos: self.pos
                    FloatLayout:
                        orientation:"vertical"
                        size_hint:(0.85,0.9)
                        pos_hint:{"x":0.15}
                        canvas.before:
                            Color:
                                rgba: (1,0,0,1)
                            Rectangle:
                                size: self.size
                                pos: self.pos
                        FloatLayout:
                            orientation:"vertical"
                            size_hint:(1,0.9)
                            pos_hint:{"x":0.002,"y":0.1}
                            canvas.before:
                                Color:
                                    rgba: (120/255,1,1,1)
                                Rectangle:
                                    size: self.size
                                    pos: self.pos
                            ScrollView:
                                StackLayout:
                                    size_hint_y:None
                                    height: self.minimum_height
                                    id: graph_placeholder
                                    canvas.before:
                                        Color:
                                            rgba: (0,1,0,1)
                                        Rectangle:
                                            size: self.size
                                            pos: self.pos

                        FloatLayout:
                            orientation:"vertical"
                            size_hint:(1,0.1)
                            pos_hint:{"x":0.001}
                            canvas.before:
                                Color:
                                    rgba: (1,1,1,1)
                                Rectangle:
                                    size: self.size
                                    pos: self.pos
                            Button:
                                text:"Show Table/Update"
                                color:(1,1,1,1)
                                size_hint:(0.22,0.7)
                                background_color:(0,0,0,0)
                                pos_hint: {"x":0.3,"y":0.1} 
                                background_normal:''
                                canvas.before:
                                    Color:
                                        rgba:(97/255, 60/255, 117/255,1)     
                                    RoundedRectangle:
                                        size: self.size
                                        pos: self.pos
                                        radius:[20]
                            Button:
                                text:"Back"
                                color:(1,1,1,1)
                                size_hint:(0.22,0.7)
                                background_color:(0,0,0,0)
                                pos_hint: {"x":0.05,"y":0.1} 
                                background_normal:''
                                canvas.before:
                                    Color:
                                        rgba:(1, 0, 0,1)     
                                    RoundedRectangle:
                                        size: self.size
                                        pos: self.pos
                                        radius:[20]

                            

                        


""")

class settingWindow(MDBoxLayout):
    pass

class visualizationWindow(Screen):
    def binder(self,checkbox,value):
        if value:
            print(self.obj_dict[checkbox]," added")
        else:
            print(self.obj_dict[checkbox], " removed")
    def uploader(self, dt):
        self.obj_dict=dict()
        self.column_dict=dict()
        self.files_address=dict()
        self.files = filechooser.open_file(title="Choose excel files", filters=[("*.xlsx")], multiple=True)
        for file in self.files:
            file_name=file.split("\\")[-1]
            self.files_address[file_name]=file
            box=BoxLayout(size_hint_y=None,height=50,padding=[30,0,0,0])
            checkbox=CheckBox(size_hint_x=.25,background_checkbox_normal="images/checkbox_nor.png",background_checkbox_down="images/checkbox_tic.png")
            checkbox.bind(active=self.binder)
            label=Label(text=f"[color=#3f51b5]{file_name}[/color]",markup=True)
            box.add_widget(checkbox)
            box.add_widget(label)
            self.ids.file_placeholder.add_widget(box)
            self.obj_dict[checkbox]=file_name

        columns=pd.read_excel(self.files[0]).columns.values.tolist()
        for column in columns:
            box = BoxLayout(size_hint_y=None, height=50, padding=[30, 0, 0, 0])
            checkbox = CheckBox(size_hint_x=.25, background_checkbox_normal="images/checkbox_nor.png",
                                background_checkbox_down="images/checkbox_tic.png")
            label = Label(text=f"[color=#3f51b5]{column}[/color]", markup=True)
            box.add_widget(checkbox)
            box.add_widget(label)
            self.ids.property_placeholder.add_widget(box)
            self.column_dict[checkbox]=column

        self.ids.upload_btn.source = "images/Drag.png"
    
    def upload_menu(self):
        self.ids.upload_btn.source="images/Drag.png"
        Clock.schedule_once(self.uploader)
    
    def switching(self):
        self.ids.sm.current="visualizer_window"

class visualization_App(MDApp):
    def build(self):
            sm = ScreenManager()
            sm.add_widget(visualizationWindow())
            return sm

if __name__=='__main__':
    visualization_App().run()