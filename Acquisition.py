from kivymd.app import MDApp
from kivy.app import App
from kivy.lang import Builder
import os
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn import preprocessing
from kivy.core.window import Window
from kivymd.uix.screenmanager import ScreenManager

from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
import csv
import random
from kivy.uix.behaviors import ButtonBehavior
from cards import *
from kivymd.uix.screenmanager import ScreenManager
from kivymd.uix.screen import Screen
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from pgmpy.models import BayesianModel
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.decomposition import PCA
from sklearn.feature_selection import RFE
from sklearn.linear_model import LinearRegression
from sklearn.feature_selection import SelectKBest, f_classif
from cards import HeroCard
import csv
from plyer import filechooser
from sklearn.metrics import accuracy_score
from sklearn.model_selection import GridSearchCV
from keras.models import Sequential
from keras.layers import Dense
from sklearn.cluster import KMeans
from kivy.properties import ObjectProperty
from sklearn.metrics import confusion_matrix
from sklearn.metrics import precision_score, recall_score
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
import pyttsx3

Builder.load_string("""
<SystemLayout>:
    name:"start"
    canvas.before:
        Color:
            rgba: (0,0,0,1)
        Rectangle:
            size: self.size
            pos: self.pos
    
	BoxLayout:
		orientation: "vertical"
		size: root.width, root.height

		Image:
			source: 'images/back.png'
			allow_stretch: True
			keep_ratio: True
			
    FloatLayout:
        orientation: "horizontal"
		size: root.width, root.height

		Image:
			source: 'images/Logo.png'
			allow_stretch: True
			keep_ratio: True
			size_hint:(0.2,0.2)
			pos_hint: {"x":0.41,"top":0.82}

        Label:
            text:"Welcome To "
            font_size: 34
            font_name: "Tahoma"
            size_hint:(0.2,0.2)
			pos_hint: {"x":0.41,"top":0.6}

        Label:
            text:"DDoS Attack "
            font_size: 28
            font_name: "Tahoma"
            color: (1,0,0,1)
            size_hint:(0.2,0.2)
			pos_hint: {"x":0.41,"top":0.53}

        Label:
            text:"Detection System "
            font_size: 30
            font_name: "Tahoma"
            size_hint:(0.2,0.2)
			pos_hint: {"x":0.41,"top":0.46}

        Button:
            font_size:18
            text: "Get Started"
            color: (1,1,1,1)
            background_normal:''
            background_color:(0,0,0,1)
            size_hint:(0.2,0.06)
			pos_hint: {"x":0.41,"top":0.2}
            canvas.before:
                Color:
                    rgba: 1, 1, 1, 1
                Line:
                    width: 2
                    rectangle: self.x, self.y , self.width, self.height
            on_release:
                root.manager.transition.direction = 'left'
                app.root.current = "home"

<screenwid>:
    name:"z"
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
                background_color:(30/255,35/255,36/255,1)
                background_normal:''
                on_press:
                    root.manager.transition.direction = 'right'
                    app.root.current = "home"
                Image:
                    source:"images/home.png"
                    center_x: self.parent.center_x
                    center_y: self.parent.center_y
            
            Button:
                id:btn_acquisition
                size_hint_x:0.99
                background_color:(55/255,61/255,62/255,1)
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
                orientation: "vertical"
                size: root.width, root.height

                Label:
                    text:"Please Select File Extension of selected File "
                    font_size: 20
                    font_name: "Tahoma"
                    size_hint:(0.2,0.2)
                    pos_hint: {"x":0.23,"top":1.02}

                Spinner:
                    id:spinner_acquisition
                    text: "File extension"
                    values:[".Xlsx",".Csv"]
                    size_hint:(0.4,0.1)
                    pos_hint: {"x":0.15,"top":0.85}
                    background_color:(0/255, 148/255, 255/255,1)
                    background_normal:''
                    canvas.before:
                        Color:
                            rgba:(1,1,1,1)
                        Line:
                            width: 2
                            rectangle: self.x, self.y, self.width, self.height
                    on_text: root.spinner_clicked(spinner_acquisition.text)

                FileChooserIconView:
                    id: filechooser
                    size_hint:(0.35,0.58)
                    pos_hint: {"x":0.65,"top":1}
                    canvas.before:
                        Color:
                            rgb: 1,1,1
                        Rectangle:
                            pos: self.pos
                            size: self.size
                    on_selection: root.selected(filechooser.selection)
                
                Button:
                    text:"Get Table"
                    size_hint:(0.4,0.1)
                    pos_hint: {"x":0.15,"top":0.68}
                    background_color:(0/255, 148/255, 255/255,1)
                    background_normal:''
                    canvas.before:
                        Color:
                            rgba:(1, 1, 1,1)
                        Line:
                            width: 2
                            rectangle: self.x, self.y , self.width, self.height
                    on_press:
                        main_win.tablecheck()
                        app.root.current = "tablewid"
                        root.manager.transition.direction = 'left'

                Label:
                    text:"Data Preprocessing"
                    font_size: 25
                    font_name: "Tahoma"
                    size_hint:(0.2,0.2)
			        pos_hint: {"x":0.09,"top":0.55}

                Button:
                    text:"Convert"
                    color:(0,0,0,1)
                    size_hint:(0.2,0.06)
                    pos_hint: {"x":0.04,"top":0.35}
                    background_color:(0,0,0,0)
                    background_normal:''
                    canvas.before:
                        Color:
                            rgba:(1,1,1,1)
                        RoundedRectangle:
                            size:   self.size
                            pos:    self.pos
                            radius: [15]
                    on_release:
                        root.Conversion()

                Button:
                    text:"Label Encode"
                    color:(0,0,0,1)
                    size_hint:(0.2,0.06)
                    pos_hint: {"x":0.27,"top":0.35}
                    background_color:(0,0,0,0)
                    background_normal:''
                    canvas.before:
                        Color:
                            rgba:(1,1,1,1)
                        RoundedRectangle:
                            size:   self.size
                            pos:    self.pos
                            radius: [15]
                    on_release:
                        root.Label_encode()
                        

                Button:
                    text:"Normalize Dataset"
                    color:(0,0,0,1)
                    size_hint:(0.2,0.06)
                    pos_hint: {"x":0.5,"top":0.35}
                    background_color:(0,0,0,0)
                    background_normal:''
                    canvas.before:
                        Color:
                            rgba:(1,1,1,1)
                        RoundedRectangle:
                            size:   self.size
                            pos:    self.pos
                            radius: [15]
                    on_release:
                        root.normalize()
                        

                Button:
                    text:"Remove Missing Attribute"
                    color:(0,0,0,1)
                    size_hint:(0.25,0.06)
                    pos_hint: {"x":0.73,"top":0.35}
                    background_color:(0,0,0,0)
                    background_normal:''
                    canvas.before:
                        Color:
                            rgba:(1,1,1,1)
                        RoundedRectangle:
                            size:   self.size
                            pos:    self.pos
                            radius: [15]
                    on_release:
                        root.Remove_missing()
                        

                Button:
                    text:"Split Dataset"
                    color:(0,0,0,1)
                    size_hint:(0.2,0.06)
                    pos_hint: {"x":0.04,"top":0.2}
                    background_color:(0,0,0,0)
                    background_normal:''
                    canvas.before:
                        Color:
                            rgba:(1,1,1,1)
                        RoundedRectangle:
                            size:   self.size
                            pos:    self.pos
                            radius: [15]
                    on_release:
                        root.Split_Dataset()

                Button:
                    text:"Cancel"
                    color:(1,1,1,1)
                    size_hint:(0.2,0.06)
                    pos_hint: {"x":0.54,"top":0.1}
                    background_color:(0,0,0,0)
                    background_normal:''
                    canvas.before:
                        Color:
                            rgba:(1,0,0,1)
                        RoundedRectangle:
                            size:   self.size
                            pos:    self.pos
                            radius: [15]
                    on_release:
                        root.close_window()

                Button:
                    text:"NEXT"
                    color:(1,1,1,1)
                    size_hint:(0.2,0.06)
                    pos_hint: {"x":0.78,"top":0.1}
                    background_color:(0,0,0,0)
                    background_normal:''
                    canvas.before:
                        Color:
                            rgba:(0/255, 148/255, 255/255,1)
                        RoundedRectangle:
                            size:   self.size
                            pos:    self.pos
                            radius: [15]
                    on_press:
                        root.manager.transition.direction = 'left'
                        root.manager.current = "featureselection"

<Table_wid>:
    name:"tablewid"
    id: table_win
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
                background_color:(30/255,35/255,36/255,1)
                background_normal:''
                on_press:
                    root.manager.transition.direction = 'right'
                    app.root.current = "home"
                Image:
                    source:"images/home.png"
                    center_x: self.parent.center_x
                    center_y: self.parent.center_y
            
            Button:
                id:btn_acquisition
                size_hint_x:0.99
                background_color:(55/255,61/255,62/255,1)
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

<featurewindow>:
    name:"featureselection"
    id: main_win
    orientation: 'vertical'
    canvas.before:
        Color:
            rgba: (30/255,35/255,36/255,1)
            # rgba:(1,1,1,1)
        Rectangle:
            size: self.size
            

    BoxLayout:
        id: content_nav
        
        BoxLayout:
            id: nav_tabs
            size_hint_x:0.1
            orientation: 'vertical'
            spacing: 1
            
            canvas.before:
                # horizontal
                Color:
                    rgba: (1,1,1,1)
                Rectangle:
                    size: self.size
                    pos: self.pos
                # Vertical                                                                                      
                Color:
                    rgba: (1,1,1,1)
                Rectangle:
                    size: self.width-1, self.height
                    pos: self.x, self.y

            Button:
                id:btn_home
                size_hint_x:0.99
                background_color:(30/255,35/255,36/255,1)
                background_normal:''
                on_press:
                    root.manager.transition.direction = 'right'
                    root.manager.current = "home"
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
                    root.manager.current = "z"
                    root.manager.transition.direction = 'right'
                Image:
                    source:"images/acquisition.png"
                    center_x: self.parent.center_x
                    center_y: self.parent.center_y
                    width:50
                    height:50
                
            Button:
                id:btn_feature
                size_hint_x:0.99
                background_color:(55/255,61/255,62/255,1)
                background_normal:''
                on_release:
                    root.manager.current = "featureselection"
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
                    root.manager.current = "mainwin"
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
                orientation: "vertical"
                size: root.width, root.height

                Image:
                    source: 'images/learning.png'
                    size_hint:(0.1,0.1)
                    pos_hint: {"x":0.2,"y":0.88}
                    size: self.texture_size

                Label:
                    text:" Dimensionality Reduction "
                    font_size: 30
                    font_name: 'Font/Poppins-Medium.ttf'
                    pos_hint: {"x":0.1,"y":0.43}

                Button:
                    id:btn_SelectFile
                    size_hint:(0.86,0.25)
                    pos_hint: {"x":0.07,"y":0.6}
                    background_color:(55/255,61/255,62/255,1)
                    background_normal:''
                    on_press:
                        root.file_chooser()
                    Image:
                        source:"images/select.png"
                        center_x: self.parent.center_x
                        center_y: self.parent.center_y

                Label:
                    text:"Feature Extraction and Selection Techniques"
                    font_size: 20
                    font_name: 'Font/Poppins-Medium.ttf'
                    size_hint:(0.5,0.08)
                    pos_hint: {"x":0.07,"y":0.45}
                
                Spinner:
                    id:spinner_acquisition
                    text: "Please Select One Technique"
                    values:["Principal Component Analysis","Univariate Feature Selection","Recursive Feature Elimination"]
                    size_hint:(0.5,0.08)
                    pos_hint:{"x":0.07,"y":0.35}
                    background_color:(0/255, 148/255, 255/255,1)
                    background_normal:''
                    canvas.before:
                        Color:
                            rgba:(1,1,1,1)
                        Line:
                            width: 1.5
                            rectangle: self.x, self.y,self.width, self.height
                    on_text: root.spinner_clicked(spinner_acquisition.text)
    
                Button:
                    text:"Cancel"
                    color:(1,1,1,1)
                    size_hint:(0.25,0.06)
                    pos_hint: {"x":0.15,"top":0.1}
                    background_color:(0,0,0,0)
                    background_normal:''
                    canvas.before:
                        Color:
                            rgba:(1,0,0,1)
                        RoundedRectangle:
                            size:   self.size
                            pos:    self.pos
                            radius: [15]
                    on_release:
                        root.close_window()

                Button:
                    text:"NEXT"
                    color:(1,1,1,1)
                    size_hint:(0.25,0.06)
                    pos_hint: {"x":0.68,"top":0.1}
                    background_color:(0,0,0,0)
                    background_normal:''
                    canvas.before:
                        Color:
                            rgba:(0/255, 148/255, 255/255,1)
                        RoundedRectangle:
                            size:   self.size
                            pos:    self.pos
                            radius: [15]
                    on_press:
                        root.manager.transition.direction = 'left'
                        root.manager.current = "mainwin"

<MyLayout>
	name:"mainwin"
    id: main_win
	orientation: 'vertical'
    canvas.before:
        Color:
            rgba: (30/255,35/255,36/255,1)
            # rgba:(1,1,1,1)
        Rectangle:
            size: self.size
            pos: self.pos

	FloatLayout:
		orientation: "vertical"
		size: root.width, root.height

		Image:
			source: 'images/machine-learning.png'
			size_hint:(0.1,0.1)
			pos_hint: {"x":0.24,"y":0.89}
			size: self.texture_size

		Label:
			text:" Machine Learning Algorithm "
			font_size: 30
			font_name: 'Font/Poppins-Medium.ttf'
			pos_hint: {"x":0.1,"y":0.43}
		

	MDBoxLayout:
        id: content_nav
        
        BoxLayout:
            id: nav_tabs
            size_hint_x:0.15
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
                background_color:(30/255,35/255,36/255,1)
                background_normal:''
                on_press:
                    root.manager.transition.direction = 'right'
                    root.manager.current = "home"
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
                    root.manager.current = "z"
                    root.manager.transition.direction = 'right'
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
                    root.manager.current = "featureselection"
                    root.manager.transition.direction = 'right'
                Image:
                    source:"images/feature.png"
                    center_x: self.parent.center_x
                    center_y: self.parent.center_y
                    width:50
                    height:50
            
            Button:
                id:btn_machinelearning
                size_hint_x:0.99
                background_color:(55/255,61/255,62/255,1)
                background_normal:''
                on_release:
                    root.manager.current = "mainwin"
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
		
	
		MDBoxLayout:
			orientation: "vertical"
			size: root.width, root.height
			padding: "100dp", "65dp","100dp","0dp"
			spacing:"12dp"

			ScrollView:

				MDList:
					id: hero_list
					padding:"24dp"
					spacing:"24dp"

                    
<traintestwindow>:
    name:"traintest"
    id: traintest_win
    orientation: 'vertical'
    canvas.before:
        Color:
            rgba: (30/255,35/255,36/255,1)
        Rectangle:
            size: self.size
            

    BoxLayout:
        id: content_nav
        
        BoxLayout:
            id: nav_tabs
            size_hint_x:0.1
            orientation: 'vertical'
            spacing: 1
            
            canvas.before:
                # horizontal
                Color:
                    rgba: (1,1,1,1)
                Rectangle:
                    size: self.size
                    pos: self.pos
                # Vertical                                                                                      
                Color:
                    rgba: (1,1,1,1)
                Rectangle:
                    size: self.width-1, self.height
                    pos: self.x, self.y

            Button:
                id:btn_home
                size_hint_x:0.99
                background_color:(30/255,35/255,36/255,1)
                background_normal:''
                on_press:
                    root.manager.transition.direction = 'right'
                    root.manager.current = "home"
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
                    root.manager.current = "z"
                    root.manager.transition.direction = 'right'
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
                    root.manager.current = "featureselection"
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
                    root.manager.current = "mainwin"
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
                background_color:(55/255,61/255,62/255,1)
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
                orientation: "vertical"
                size: root.width, root.height

                Image:
                    source: 'images/testmodel.png'
                    size_hint:(0.1,0.1)
                    pos_hint: {"x":0.2,"y":0.88}
                    size: self.texture_size

                Label:
                    text:" Training & Testing "
                    font_size: 30
                    font_name: 'Font/Poppins-Medium.ttf'
                    pos_hint: {"x":0.1,"y":0.43}

                Button:
                    id:btn_Train
                    size_hint:(0.4,0.20)
                    pos_hint: {"x":0.07,"y":0.67}
                    background_color:(55/255,61/255,62/255,1)
                    background_normal:''
                    on_press:
                        root.file_chooser("train")
                    Image:
                        source:"images/Train1.png"
                        center_x: self.parent.center_x
                        center_y: self.parent.center_y
                Label:
                    text:"Select Training Dataset "
                    font_size: 15
                    font_name: 'Font/Poppins-Medium.ttf'
                    size_hint:(0.2,0.1)
                    pos_hint: {"x":0.15,"y":0.6}

                Button:
                    id:btn_Test
                    size_hint:(0.4,0.20)
                    pos_hint: {"x":0.5,"y":0.67}
                    background_color:(55/255,61/255,62/255,1)
                    background_normal:''
                    on_press:
                        root.file_chooser("test")
                    Image:
                        source:"images/Test1.png"
                        center_x: self.parent.center_x
                        center_y: self.parent.center_y
                Label:
                    text:"Select Testing Dataset "
                    font_size: 15
                    font_name: 'Font/Poppins-Medium.ttf'
                    size_hint:(0.2,0.1)
                    pos_hint: {"x":0.6,"y":0.6}
                
                Button:
                    text:"Predict"
                    color:(1,1,1,1)
                    size_hint:(0.45,0.06)
                    pos_hint: {"x":0.3,"y":0.4}
                    background_color:(0,0,0,0)
                    background_normal:''
                    canvas.before:
                        Color:
                            rgba:(69/255, 172/255, 173/255,1)
                        RoundedRectangle:
                            size:   self.size
                            pos:    self.pos
                            radius: [15]
                    on_release:
                        root.predict()
    
                Label:
                    id: accuracy_label
                    text:" "
                    font_size: 20
                    font_name: 'Font/Poppins-Medium.ttf'
                    size_hint:(0.3,0.08)
                    pos_hint: {"x":0.35,"y":0.2}

                Button:
                    text:"Cancel"
                    color:(1,1,1,1)
                    size_hint:(0.25,0.06)
                    pos_hint: {"x":0.15,"top":0.1}
                    background_color:(0,0,0,0)
                    background_normal:''
                    canvas.before:
                        Color:
                            rgba:(1,0,0,1)
                        RoundedRectangle:
                            size:   self.size
                            pos:    self.pos
                            radius: [15]
                    on_release:
                        root.close_window()

                Button:
                    text:"NEXT"
                    color:(1,1,1,1)
                    size_hint:(0.25,0.06)
                    pos_hint: {"x":0.68,"top":0.1}
                    background_color:(0,0,0,0)
                    background_normal:''
                    canvas.before:
                        Color:
                            rgba:(0/255, 148/255, 255/255,1)
                        RoundedRectangle:
                            size:   self.size
                            pos:    self.pos
                            radius: [15]
                    on_press:
                        root.manager.transition.direction = 'left'
                        root.manager.current = "mainwin"

""")
class SystemLayout(Screen):
	pass

class Home_PageWindow(Screen, ButtonBehavior):
    pass

class Table_wid(Screen):
    pass

class screenwid(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
    
    def spinner_clicked(self,value):
        global file_extension 
        file_extension= value

    def selected(self,filename):
        try:
            global file_name
            file_name=filename
            # self.convertion_Excel_to_Csv(filename) This is just for giving the name to the table
            pass
        except:
            pass

    def tablecheck(self):
        if(file_extension==".Xlsx"):
            self.read_excel()
        else:
            self.read_csv()
                
    def read_excel(self):
        read_file=pd.read_excel(file_name[0])
        cols=read_file.columns.values
        values=read_file.values

        # print (read_file.columns)
        table= MDDataTable(
            pos_hint= {'center_x': 0.5, 'center_y': 0.5},
            size_hint= (0.9,0.6),
            use_pagination=True,
            rows_num=20,
            check = True,
            column_data =[(col, dp(30))
                for col in cols
            ] ,
			row_data = values
			)

        table.bind(on_check_press = self.checked)
        table.bind(on_row_press = self.row_checked)

        # self.theme_cls.theme_style= 'Dark'
        # self.theme_cls.primary_palette= 'BlueGray'

        ScreenManager.get_screen("tablewid").ids.content.add_widget(table)

    def checked(self,instance_table,current_row):
        print(instance_table,current_row)
    def row_checked(self,instance_table,instance_row):
        print(instance_table,instance_row)   

    # Method for displaying table if file is in csv format 
    
    def read_csv(self):
        read_file=pd.read_csv(file_name[0])
        cols=read_file.columns.values
        values=read_file.values

        # print (read_file.columns)
        table= MDDataTable(
            pos_hint= {'center_x': 0.5, 'center_y': 0.5},
            size_hint= (0.9,0.6),
            use_pagination=True,
            rows_num=20,
            check = True,
            background_color_header="#03cffc",
            column_data =[(col, dp(30))
                for col in cols
            ] ,
			row_data = values
			)

        table.bind(on_check_press = self.checked)
        table.bind(on_row_press = self.row_checked)

        # self.theme_cls.theme_style= 'Dark'
        # self.theme_cls.primary_palette= 'BlueGray'

        ScreenManager.get_screen("tablewid").ids.content.add_widget(table)

    def checked(self,instance_table,current_row):
        print(instance_table,current_row)
    def row_checked(self,instance_table,instance_row):
        print(instance_table,instance_row)


# *********************************************************** DATA PREPROCESSING************************************************


    def Conversion(self):
        if(file_extension==".Xlsx"):
            self.convertion_Excel_to_Csv(file_name)
        else:
            print("Error!! File Already in CSV format")

    def convertion_Excel_to_Csv(self,getfilename):
        read_file=pd.read_excel(getfilename[0])
        read_file.to_csv(os.path.join(str('New_Dataset') + str('.csv')), index=None, header=True)
        print("Converted Successfully")
        


    def Label_encode(self):
        # Read in the CSV file
        data = []
        with open(file_name[0], 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                data.append(row)

        # Get the indices of the non-numerical columns
        non_num_cols = []
        for i, col in enumerate(data[0]):
            try:
                float(col)
            except ValueError:
                non_num_cols.append(i)

        # Convert the non-numerical data using label encoder
        le = LabelEncoder()
        for i in non_num_cols:
            col = [row[i] for row in data[1:]]
            le.fit(col)
            for j, val in enumerate(col):
                data[j+1][i] = le.transform([val])[0]

        # Write the converted data back to the CSV file
        with open(file_name[0], 'w', newline='') as f:
            writer = csv.writer(f)
            for row in data:
                writer.writerow(row)

        print("Congrats User! Dataset Label Encoded Successfully ")

    
    def normalize(self):
        
        # Load the CSV file
        df = pd.read_csv(file_name[0])

        # Create the scaler
        scaler = preprocessing.MinMaxScaler()

        # Fit the scaler to the data
        # Mean and Standard deviation is calculated
        scaler.fit(df)

        # Transform the data
        # Values are transformed into 0 to 1
        df_scaled = scaler.transform(df)

        # Convert the data back to a DataFrame
        df_scaled = pd.DataFrame(df_scaled, columns=df.columns)

        # Save the transformed data
        df_scaled.to_csv(file_name[0], index=False)

        print("Normalized Successfully!!")
    
    def Remove_missing(self):

        # Open the input CSV file
        with open(file_name[0], 'r') as input_file:
            # Create a CSV reader object
            reader = csv.reader(input_file)

            # Initialize a list to store the rows with no missing values
            clean_rows = []

            # Iterate through the rows in the CSV
            for row in reader:
                # Check if any of the values in the row are missing
                if any(value == '' for value in row):
                    # Skip the row if any values are missing
                    continue
                # Otherwise, append the row to the list of clean rows
                clean_rows.append(row)

        # Open the output CSV file
        with open(file_name[0], 'w', newline='') as output_file:
            # Create a CSV writer object
            writer = csv.writer(output_file)

            # Write the clean rows to the output CSV file
            writer.writerows(clean_rows)

        print("Missing Values successfully removed from the dataset")


    def Split_Dataset(self):
        # Open the input CSV file and create a CSV reader object
        with open(file_name[0], 'r') as input_file:
            reader = csv.DictReader(input_file)
            
            # Extract the column names from the input file and store them in a list
            column_names = reader.fieldnames

            # Initialize lists to store the training and testing data
            training_data = []
            testing_data = []

            # Iterate through the rows in the CSV
            for row in reader:
                # Generate a random number between 0 and 1
                rand = random.random()
                # If the random number is less than 0.8, add the row to the training data
                if rand < 0.8:
                    training_data.append(row)
                # Otherwise, add the row to the testing data
                else:
                    testing_data.append(row)

        # Open the training data CSV file and create a CSV writer object with column names
        with open('training_data.csv', 'w', newline='') as training_file:
            writer = csv.DictWriter(training_file, fieldnames=column_names)
            # Write the column names to the CSV file
            writer.writeheader()
            # Write the training data to the CSV file
            writer.writerows(training_data)

        # Open the testing data CSV file and create a CSV writer object with column names
        with open('testing_data.csv', 'w', newline='') as testing_file:
            writer = csv.DictWriter(testing_file, fieldnames=column_names)
            # Write the column names to the CSV file
            writer.writeheader()
            # Write the testing data to the CSV file
            writer.writerows(testing_data)

        print("Successfully Dataset splitted into testing and training")

    def close_window(self,obj):
        App.get_running_app().stop()
        Window.close()

class featurewindow(Screen):
    global selected_features

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def file_chooser(self):
        filechooser.open_file(on_selection=self.file)

    def file(self,selection):
        global file_name
        file_name=selection
        
        # Open the CSV file
        with open(file_name[0], newline='') as csvfile:
            # Create a reader object
            reader = csv.reader(csvfile)
            # Read the header row
            header = next(reader)
            # Print the header row
            print(header)

    def spinner_clicked(self,attribute): 
        if(attribute=="Principal Component Analysis"):
            selected_features = self.pca()
        elif(attribute=="Univariate Feature Selection"):
            selected_features = self.UFS()
        elif(attribute=="Recursive Feature Elimination"):
            selected_features = self.RFE()
        print (selected_features)

############################################################# Principle Component Analysis ################################################

    def pca(self):
        # Load the dataset
        data = pd.read_csv(file_name[0])
        
        # Separate the features and the target variable
        X = data.drop(columns=['class'])
        y = data['class']

        # Initialize PCA with the number of components you want to keep
        pca = PCA(n_components=15)
        # Apply PCA on your dataset
        pca.fit(X)
        # Transform the data into the reduced feature space
        X_reduced = pca.transform(X)

        # Identify the most important original features
        components = pd.DataFrame(pca.components_.T, columns=['PC'+str(i) for i in range(1, X_reduced.shape[1]+1)], index=X.columns)
        top_features = components.abs().sum(axis=1).sort_values(ascending=False)[:15].index.tolist()
        print("Most important original features:\n", top_features)

        # Create a list of column names for the reduced features
        columns = top_features.copy()

        # Create a DataFrame with the reduced features as columns
        X_reduced_df = pd.DataFrame(X_reduced, columns=columns)

        # Concatenate the target variable with the reduced feature space
        X_reduced_df = pd.concat([X_reduced_df, data['class']], axis=1)

                # Split the selected data into training and testing sets
        train_data, test_data = train_test_split(X_reduced_df, test_size=0.2, random_state=42)

        # Save the training data to a CSV file
        with open('training.csv', 'w') as f:
            # Write the header row
            header = ','.join(train_data.columns)
            f.write(header + '\n')
            
            # Write the data rows
            for index, row in train_data.iterrows():
                values = ','.join([str(val) for val in row.values])
                f.write(values + '\n')

        # Save the testing data to a CSV file
        with open('testing.csv', 'w') as f:
            # Write the header row
            header = ','.join(test_data.columns)
            f.write(header + '\n')
            
            # Write the data rows
            for index, row in test_data.iterrows():
                values = ','.join([str(val) for val in row.values])
                f.write(values + '\n')

        # Print the explained variance ratios
        print("Explained variance ratios:", pca.explained_variance_ratio_)
        # Print the new shape of the data
        print("New shape of X:", X_reduced_df.shape)
        return X_reduced_df




        
############################################################# univariate Feature Selection ################################################
    def UFS(self):
        # Load the dataset
        data = pd.read_csv(file_name[0])

        # Separate the features and the target variable
        X = data.drop(columns=['class'])
        y = data['class']

        # Apply univariate feature selection
        selector = SelectKBest(score_func=f_classif, k=15)
        selector.fit(X, y)

        # Get the selected features
        selected_features = X.columns[selector.get_support()]

        # Concatenate the selected features and the target variable column
        selected_df = pd.concat([X[selected_features], y], axis=1)

        # Split the selected data into training and testing sets
        train_data, test_data = train_test_split(selected_df, test_size=0.2, random_state=42)

        # Save the training data to a CSV file
        with open('training.csv', 'w') as f:
            # Write the header row
            header = ','.join(train_data.columns)
            f.write(header + '\n')
            
            # Write the data rows
            for index, row in train_data.iterrows():
                values = ','.join([str(val) for val in row.values])
                f.write(values + '\n')

        # Save the testing data to a CSV file
        with open('testing.csv', 'w') as f:
            # Write the header row
            header = ','.join(test_data.columns)
            f.write(header + '\n')
            
            # Write the data rows
            for index, row in test_data.iterrows():
                values = ','.join([str(val) for val in row.values])
                f.write(values + '\n')

        print("Selected features are:")
        print(selected_features)
        return selected_df

    
################################################################## Recursive Feature Elimination  #########################################
    def RFE(self): 
        # Load the dataset from a CSV file using Pandas
        data = pd.read_csv(file_name[0])

        # Separate the target variable from the features
        X = data.drop('class', axis=1)
        y = data['class']

        # Create a logistic regression estimator
        lr_estimator = LinearRegression()

        # Define The number of features you want to select
        rfe = RFE(lr_estimator, n_features_to_select=15)

        # Fit the RFE object to the data
        rfe.fit(X, y)

        # Print the selected features
        selected_features = X.columns[rfe.support_]
        selected_df = pd.concat([X[selected_features], y], axis=1)
		# Split the selected data into training and testing sets
        train_data, test_data = train_test_split(selected_df, test_size=0.2, random_state=42)
        # Save the training data to a CSV file
        with open('training.csv', 'w') as f:
            # Write the header row
            header = ','.join(train_data.columns)
            f.write(header + '\n')
            
            # Write the data rows
            for index, row in train_data.iterrows():
                values = ','.join([str(val) for val in row.values])
                f.write(values + '\n')

        # Save the testing data to a CSV file
        with open('testing.csv', 'w') as f:
            # Write the header row
            header = ','.join(test_data.columns)
            f.write(header + '\n')
            
            # Write the data rows
            for index, row in test_data.iterrows():
                values = ','.join([str(val) for val in row.values])
                f.write(values + '\n')

        # print("Selected Features:",selected_features)
        return selected_df
    

class MyLayout(Screen):
	pass

class AcquisitionApp(MDApp):
    selected_card = None

    image_list=[
		"images/DecisiontreeAlgo.jpeg",
		"images/pic2.jpeg",
		"images/pic3.jpeg",
		"images/pic5.jpeg",
		"images/pic6.jpeg",
		"images/pic7.jpeg",
		"images/pic8.jpeg",
		"images/randomforest.jpeg"
	]

    label_list=[
		"Decision Tree",
		"Logistic Regression(LR)",
		"Naive Bayes(NB)",
		"K Nearest Neighbour",
		"Support Vector Machines",
		"Neural Networks (NNs)",
		"Gradient Boosting Classifier",
		"Random Forest"
	]

    description_list=[
		"Can solve a non-linear problems Can Work on high-dimensional data with excellent accuracy Easy to visualize and explain",
		"It is much easier to set up and train than other machine learning and AI applications. It is one of the most efficient algorithms when the different outcomes or distinctions represented by the data are linearly separable.",
		"Naive Bayes methods are a set of supervised learning algorithms based on applying Bayes' theorem with the “naive” assumption of conditional independence between every pair of features given the value of the class variable",
		"The k-nearest neighbors algorithm, also known as KNN or k-NN, is a non-parametric, supervised learning classifier, which uses proximity to make classifications or predictions about the grouping of an individual data point.",
		"SVM are a set of supervised learning methods used for classification, regression and outliers detection.It is Effective in high dimensional spaces.Still effective in cases where number of dimensions is greater than the number of samples. It is also memory efficient.",
		"A neural network is a method in artificial intelligence that teaches computers to process data in a way that is inspired by the human brain. It is a type of machine learning process, called deep learning, that uses interconnected nodes or neurons in a layered structure that resembles the human brain.",
		" It is an ensemble learning algorithm that combines multiple weak classifiers to create a strong classifier",
		"Random forest is a commonly-used machine learning algorithm trademarked by Leo Breiman and Adele Cutler, which combines the output of multiple decision trees to reach a single result. Its ease of use and flexibility have fueled its adoption"
	]
    
    def build(self):
        global ScreenManager
        ScreenManager= ScreenManager()
        ScreenManager.add_widget(SystemLayout())
        ScreenManager.add_widget(Home_PageWindow())
        ScreenManager.add_widget(screenwid())
        ScreenManager.add_widget(Table_wid())
        ScreenManager.add_widget(featurewindow())
        ScreenManager.add_widget(MyLayout())
        ScreenManager.add_widget(traintestwindow())
        self.on_enter()
        return ScreenManager
    
    def on_enter(self,*args):
        if not ScreenManager.get_screen("mainwin").ids.hero_list.children:
            for i, (source, label_text,description) in enumerate(zip(self.image_list, self.label_list,self.description_list)):
                ScreenManager.get_screen("mainwin").ids.hero_list.add_widget(
                HeroCard(source=source,label_text=label_text,description=description, on_press=lambda x,i=i:self.checkclicked(i))
            )

    def checkclicked(self,i):
        if (i==0):
            AcquisitionApp.selected_card = "Decision Tree"
            ScreenManager.current='traintest'
            print("Clicked Decision Tree classifier")
        elif(i==1):
            AcquisitionApp.selected_card = "Logistic Regression"
            ScreenManager.current='traintest'
            print("Clicked Logistic Regression classifier")
        elif(i==2):
            AcquisitionApp.selected_card = "Naive Bayes"
            ScreenManager.current='traintest'
            print("Clicked Naive Bayes classifier")
        elif(i==3):
            AcquisitionApp.selected_card = "K Nearest Neighbour"
            ScreenManager.current='traintest'
            print("Clicked K Nearest Neighbour classifier")
        elif(i==4):
            AcquisitionApp.selected_card = "Support Vector"
            ScreenManager.current='traintest'
            print("Clicked Support Vector classifier")
        elif(i==5):
            AcquisitionApp.selected_card = "Neural Network"
            ScreenManager.current='traintest'
            print("Clicked  Neural Networks")
        elif(i==6):
            AcquisitionApp.selected_card = "Gradient Boosting"
            ScreenManager.current='traintest'
            print("Clicked Baysein Network classifier")
        elif(i==7):
            AcquisitionApp.selected_card = "Random Forest"
            ScreenManager.current='traintest'
            print("Clicked Random Forest classifier")

class traintestwindow(Screen, AcquisitionApp):
    accuracy_label = ObjectProperty(None)
    def __init__(self, **kwargs):
        super().__init__(**kwargs)  
        self.X_train = None
        self.y_train = None
        self.X_test = None
        self.y_test = None
        self.model = None

        
    def file_chooser(self, data_type):
        filechooser.open_file(on_selection=lambda selection: self.file(data_type, selection))
        
    def file(self, data_type, selection):
        if data_type == 'train':
            train_df = pd.read_csv(selection[0])
            self.X_train = train_df.drop(columns=train_df.columns[-1])
            self.y_train = train_df[train_df.columns[-1]]
            print("Training data loaded")
        elif data_type == 'test':
            test_df = pd.read_csv(selection[0])
            self.X_test = test_df.drop(columns=test_df.columns[-1])
            self.y_test = test_df[test_df.columns[-1]]            
            print("Testing data loaded")

    def predict(self):
        if (AcquisitionApp.selected_card == "Decision Tree"):
            accuracy,precision,recall = self.DecisionTree_classifier()
        elif(AcquisitionApp.selected_card == "Logistic Regression"):
            accuracy,precision,recall = self.LogisticRegression_classifier()
        elif(AcquisitionApp.selected_card == "Naive Bayes"):
            accuracy,precision,recall = self.NaiveBayes_classifier()
        elif(AcquisitionApp.selected_card == "K Nearest Neighbour"):
            accuracy,precision,recall = self.K_NearestNeighbour_classifier()
        elif(AcquisitionApp.selected_card == "Support Vector"):
            accuracy,precision,recall = self.SupportVectorMachine_classifier()
        elif(AcquisitionApp.selected_card == "Neural Network"):
            accuracy,precision,recall = self.NeuralNetwork_classifier()
        elif(AcquisitionApp.selected_card == "Gradient Boosting"):
            accuracy,precision,recall = self.GradientBoosting_classifier()
        elif(AcquisitionApp.selected_card == "Random Forest"):
            accuracy,precision,recall = self.RandomForest_classifier()
        else:
            print("OOPS Something Happened !!!")
        
        print("Precision: {:.2f}%".format(precision*100))
        print("Recall: {:.2f}%".format(recall*100))
        self.ids.accuracy_label.text = "Accuracy: {:.2f}%".format(accuracy*100)

        instance1= Alert()
        if(precision and recall > 65):
            instance1.show_AffirmativeDialog()
        else:
            instance1.show_NegativeDialog()


    def DecisionTree_classifier(self):
        self.model = DecisionTreeClassifier(random_state=42)
        self.model.fit(self.X_train, self.y_train)
        # Evaluate the classifier on the testing set
        y_pred = self.model.predict(self.X_test)
        # print(self.model.predict_proba(self.X_test)[0:10])
        accuracy = accuracy_score(self.y_test, y_pred)
        precision = precision_score(self.y_test, y_pred)
        recall = recall_score(self.y_test, y_pred)
        print("Accuracy: {:.2f}%".format(accuracy*100))
        cm = confusion_matrix(self.y_test, y_pred)
        print("Confusion matrix:")
        print(cm)
        return accuracy,precision,recall
    
    def LogisticRegression_classifier(self):
        self.model = LogisticRegression(random_state=42)
        self.model.fit(self.X_train, self.y_train)
        # Evaluate the classifier on the testing set
        y_pred = self.model.predict(self.X_test)
        accuracy = accuracy_score(self.y_test, y_pred)
        precision = precision_score(self.y_test, y_pred)
        recall = recall_score(self.y_test, y_pred)
        print("Accuracy: {:.2f}%".format(accuracy*100))
        cm = confusion_matrix(self.y_test, y_pred)
        print("Confusion matrix:")
        print(cm)
        return accuracy,precision,recall
            
    def NaiveBayes_classifier(self):
        self.model = GaussianNB()
        self.model.fit(self.X_train, self.y_train)
        # Evaluate the classifier on the testing set
        y_pred = self.model.predict(self.X_test)
        accuracy = accuracy_score(self.y_test, y_pred)
        precision = precision_score(self.y_test, y_pred)
        recall = recall_score(self.y_test, y_pred)
        print("Accuracy: {:.2f}%".format(accuracy*100))
        cm = confusion_matrix(self.y_test, y_pred)
        print("Confusion matrix:")
        print(cm)
        return accuracy,precision,recall
    
    def K_NearestNeighbour_classifier(self):
        self.model = KNeighborsClassifier()
        self.model.fit(self.X_train, self.y_train)
        # Evaluate the classifier on the testing set
        y_pred = self.model.predict(self.X_test)
        accuracy = accuracy_score(self.y_test, y_pred)
        precision = precision_score(self.y_test, y_pred)
        recall = recall_score(self.y_test, y_pred)
        print("Accuracy: {:.2f}%".format(accuracy*100))
        cm = confusion_matrix(self.y_test, y_pred)
        print("Confusion matrix:")
        print(cm)
        return accuracy,precision,recall

    def SupportVectorMachine_classifier(self):
        self.model = SVC()
        self.model.fit(self.X_train, self.y_train)
        y_pred = self.model.predict(self.X_test)
        accuracy = accuracy_score(self.y_test, y_pred)
        precision = precision_score(self.y_test, y_pred)
        recall = recall_score(self.y_test, y_pred)
        print("Accuracy: {:.2f}%".format(accuracy*100))
        cm = confusion_matrix(self.y_test, y_pred)
        print("Confusion matrix:")
        print(cm)
        return accuracy,precision,recall
        
    def NeuralNetwork_classifier(self):
        self.model = Sequential()
        # add layers to the model
        self.model.add(Dense(64, input_dim=self.X_train.shape[1], activation='relu'))
        self.model.add(Dense(32, activation='relu'))
        self.model.add(Dense(1, activation='sigmoid'))
        # compile the model
        self.model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

        # fit the model on the training data
        self.model.fit(self.X_train, self.y_train, epochs=10, batch_size=32, validation_data=(self.X_test, self.y_test))

        # predict labels on the test data
        y_pred_prob = self.model.predict(self.X_test)
        y_pred = (y_pred_prob > 0.5).astype(int)

        # evaluate the model on the test data
        accuracy = self.model.evaluate(self.X_test, self.y_test)[1]
        precision = precision_score(self.y_test, y_pred)
        recall = recall_score(self.y_test, y_pred)
        print("Accuracy: {:.2f}%".format(accuracy*100))
        cm = confusion_matrix(self.y_test, y_pred)
        print("Confusion matrix:")
        print(cm)
        return accuracy,precision,recall

    def GradientBoosting_classifier(self):
        self.model = GradientBoostingClassifier()
        self.model.fit(self.X_train, self.y_train)
        y_pred = self.model.predict(self.X_test)
        accuracy = accuracy_score(self.y_test, y_pred)
        precision = precision_score(self.y_test, y_pred)
        recall = recall_score(self.y_test, y_pred)
        print("Accuracy: {:.2f}%".format(accuracy*100))
        cm = confusion_matrix(self.y_test, y_pred)
        print("Confusion matrix:")
        print(cm)
        return accuracy,precision,recall

    def RandomForest_classifier(self):
        param_grid = {
            'n_estimators': [10, 50, 100],
            'max_depth': [None, 5, 10],
            'random_state': [42]
        }
        rf = RandomForestClassifier()
        self.model = GridSearchCV(rf, param_grid, cv=5)
        self.model.fit(self.X_train, self.y_train)
        y_pred = self.model.predict(self.X_test)
        accuracy = accuracy_score(self.y_test, y_pred)
        precision = precision_score(self.y_test, y_pred)
        recall = recall_score(self.y_test, y_pred)
        print("Accuracy: {:.2f}%".format(accuracy*100))
        cm = confusion_matrix(self.y_test, y_pred)
        print("Confusion matrix:")
        print(cm)
        return accuracy,precision,recall
    
class Alert(traintestwindow):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)  
        
    def show_AffirmativeDialog(self):
        self.my_dialog = MDDialog(title="Alert",text="\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n                Congratulations No Attack Identified",
            size_hint=(0.5, 0.35),
            buttons=[
                MDFlatButton(
                    text="CANCEL", on_release=lambda *args: self.my_dialog.dismiss()
                ),
                MDFlatButton(
                    text="OK", on_release=lambda *args: self.handle_ok_button()
                ),
            ])
        # Create a BoxLayout for the content of the dialog
        content = BoxLayout(orientation='vertical')

        # Create an Image widget and add it to the dialog
        image = Image(source="images/checked.png")
        content.add_widget(image)
        self.my_dialog.add_widget(content)
        self.my_dialog.open()
        
        # create a TTS engine
        engine = pyttsx3.init()
        # set the voice rate (default is 200)
        engine.setProperty('rate', 150)
        # set the voice volume (default is 1.0)
        engine.setProperty('volume', 0.5)
        # say a message
        engine.say('Alert! Congratulations No Attack Occured ')
        # run the TTS engine
        engine.runAndWait()
    
    def show_NegativeDialog(self):
        self.my_dialog = MDDialog(title="Alert",text="\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n                      Possible Attack Detected",
            size_hint=(0.5, 0.35),
            buttons=[
                MDFlatButton(
                    text="CANCEL", on_release=lambda *args: self.my_dialog.dismiss()
                ),
                MDFlatButton(
                    text="OK", on_release=lambda *args: self.handle_ok_button()
                ),
            ])
        # Create a BoxLayout for the content of the dialog
        content = BoxLayout(orientation='vertical')

        # Create an Image widget and add it to the dialog
        image = Image(source="images/cancel.png")
        content.add_widget(image)
        self.my_dialog.add_widget(content)
        self.my_dialog.open()
        # create a TTS engine
        engine = pyttsx3.init()
        # set the voice rate (default is 200)
        engine.setProperty('rate', 150)
        # set the voice volume (default is 1.0)
        engine.setProperty('volume', 0.5)
        # say a message
        engine.say('Alert!Alert!Alert! Possible Attack Detected')
        # run the TTS engine
        engine.runAndWait()

    def handle_ok_button(self):
        # Handle OK button press here
        print("OK button pressed")
        self.my_dialog.dismiss()
        
	

if __name__=='__main__':
    AcquisitionApp().run()