from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.screenmanager import ScreenManager
from kivymd.uix.screen import Screen
import csv
from kivymd.app import MDApp
import numpy as np
from sklearn.decomposition import PCA
import pandas as pd
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression
from sklearn.feature_selection import SelectKBest, f_classif
from Acquisition import *
from plyer import filechooser
from kivy.properties import ObjectProperty



Builder.load_string("""
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
                    app.root.current = "home"
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

""")
class featurewindow(Screen):
    # features_label = ObjectProperty()
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
        global selected_features 
        if(attribute=="Principal Component Analysis"):
            selected_features = self.pca()
        elif(attribute=="Univariate Feature Selection"):
            selected_features = self.UFS()
        elif(attribute=="Recursive Feature Elimination"):
            selected_features = self.RFE()
        print (selected_features)

    # Principle Component Analysis
    def pca(self):
        # Load your dataset skipping the first row
        X = np.genfromtxt(file_name[0], delimiter=',', skip_header=1)
        # Initialize PCA with the number of components you want to keep(how many dimentions you want to reduce data)
        pca = PCA(n_components=10)
        # Apply PCA on your dataset
        global X_pca 
        X_pca = pca.fit_transform(X)
        # print(X_pca)
        return X_pca
        
    # univariate Feature Selection
    def UFS(self):
        # Load the dataset
        data = pd.read_csv(file_name[0])

        # Separate the features and the target variable
        X = data.drop(columns=['class'])
        y = data['class']

        # Apply univariate feature selection
        selector = SelectKBest(score_func=f_classif, k=10)
        selector.fit(X, y)

        # Get the selected features
        selected_features = X.columns[selector.get_support()]
        # Print the selected features
        print("Selected Features:")
        selected_df = data[selected_features]
        # print(selected_features)
        return selected_df
        
    # Recursive Feature Elimination
    def RFE(self): 
        # Load the dataset from a CSV file using Pandas
        data = pd.read_csv(file_name[0])

        # Separate the target variable from the features
        X = data.drop('class', axis=1)
        y = data['class']

        # Create a logistic regression estimator
        lr_estimator = LogisticRegression()

        # Create an RFE object with a step size of 1
        rfe = RFE(estimator=lr_estimator, n_features_to_select=10, step=1)

        # Fit the RFE object to the data
        rfe.fit(X, y)

        # Print the selected features
        selected_features = X.columns[rfe.support_]
        selected_df = data[selected_features]
        # print("Selected Features:")
        # print(X.columns[rfe.support_])
        return selected_df

class feature(MDApp):

    def build(self):
        global sf
        sf= ScreenManager()
        sf.add_widget(featurewindow())        
        return sf
    
if __name__=='__main__':
    feature().run()