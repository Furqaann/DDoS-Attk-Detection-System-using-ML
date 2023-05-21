from kivymd.app import MDApp
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from kivymd.uix.screen import Screen
from kivymd.uix.screenmanager import ScreenManager
from plyer import filechooser
import csv
from kivy.uix.spinner import SpinnerOption
from kivy.properties import ListProperty
import numpy as np
import plotly.graph_objects as go


Builder.load_string("""

<visualizationwindow>:
    name:"visualization"
    id: main_win
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
                background_color:(55/255,61/255,62/255,1)
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
                    source: 'images/visualize.png'
                    size_hint:(0.1,0.1)
                    pos_hint: {"x":0.2,"y":0.88}
                    size: self.texture_size

                Label:
                    text:" Data Visualization "
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
                        root.file_choose()
                    Image:
                        source:"images/select.png"
                        center_x: self.parent.center_x
                        center_y: self.parent.center_y

                Label:
                    text:" Note: For Histogram  select only X "
                    font_size: 10
                    font_name: 'Font/Poppins-Medium.ttf'
                    pos_hint: {"x":0.22,"y":-0.08}

                
                Spinner:
                    id:spinner1
                    text: "Please Select X"
                    values:root.spinner1_options
                    size_hint:(0.4,0.08)
                    pos_hint:{"x":0.07,"y":0.45}
                    background_color:(0/255, 148/255, 255/255,1)
                    background_normal:''
                    canvas.before:
                        Color:
                            rgba:(1,1,1,1)
                        Line:
                            width: 1.5
                            rectangle: self.x, self.y,self.width, self.height
                    on_text: root.spinner_clickedX(spinner1.text)

                Spinner:
                    id:spinner2
                    text: "Please Select Y"
                    values:root.spinner2_options
                    size_hint:(0.4,0.08)
                    pos_hint:{"x":0.54,"y":0.45}
                    background_color:(0/255, 148/255, 255/255,1)
                    background_normal:''
                    canvas.before:
                        Color:
                            rgba:(1,1,1,1)
                        Line:
                            width: 1.5
                            rectangle: self.x, self.y,self.width, self.height
                    on_text: root.spinner_clickedY(spinner2.text)

                    
                Label:
                    text:" Graphs "
                    font_size: 20
                    font_name: 'Font/Poppins-Medium.ttf'
                    pos_hint: {"x":0,"y":-0.15}

                Button:
                    text:"Scatter plot"
                    color:(1,1,1,1)
                    size_hint:(0.2,0.06)
                    pos_hint: {"x":0.05,"top":0.28}
                    background_color:(0,0,0,0)
                    background_normal:''
                    canvas.before:
                        Color:
                            rgba:(60/255, 166/255, 166/255,1)
                        RoundedRectangle:
                            size:   self.size
                            pos:    self.pos
                            radius: [20]
                    on_press:
                        root.generate_scatter_plot()

                Button:
                    text:"BarGraph"
                    color:(1,1,1,1)
                    size_hint:(0.2,0.06)
                    pos_hint: {"x":0.3,"top":0.28}
                    background_color:(0,0,0,0)
                    background_normal:''
                    canvas.before:
                        Color:
                            rgba:(64/255, 166/255, 166/255,1)
                        RoundedRectangle:
                            size:   self.size
                            pos:    self.pos
                            radius: [20]
                    on_press:
                        root.generate_bar_graph()
                        

                Button:
                    text:"Histogram"
                    color:(1,1,1,1)
                    size_hint:(0.2,0.06)
                    pos_hint: {"x":0.55,"top":0.28}
                    background_color:(0,0,0,0)
                    background_normal:''
                    canvas.before:
                        Color:
                            rgba:(64/255, 166/255, 166/255,1)
                        RoundedRectangle:
                            size:   self.size
                            pos:    self.pos
                            radius: [20]
                    on_press:
                        root.generate_histogram_chart()

                Button:
                    text:"HeatMap"
                    color:(1,1,1,1)
                    size_hint:(0.17,0.06)
                    pos_hint: {"x":0.8,"top":0.28}
                    background_color:(0,0,0,0)
                    background_normal:''
                    canvas.before:
                        Color:
                            rgba:(64/255, 166/255, 166/255,1)
                        RoundedRectangle:
                            size:   self.size
                            pos:    self.pos
                            radius: [20]
                    # on_press:
                    #     root.manager.transition.direction = 'left'
                    #     root.manager.current = "mainwin"

                Button:
                    text:"Compare ML Models Accuracy"
                    color:(1,1,1,1)
                    size_hint:(0.8,0.06)
                    pos_hint: {"x":0.1,"top":0.12}
                    background_color:(55/255,61/255,62/255,1)
                    background_normal:''
                    canvas.before:
                        Color:
                            rgba:1, 1, 1, 1
                        # RoundedRectangle:
                        #     size:   self.size
                        #     pos:    self.pos
                        #     radius: [20]
                        Line:
                            width: 2
                            rectangle: self.x, self.y , self.width, self.height
                    # on_press:
                    #     root.manager.transition.direction = 'left'
                    #     root.manager.current = "mainwin"
    
""")
class visualizationwindow(Screen):

    spinner1_options = ListProperty([])  # Spinner 1 options
    spinner2_options = ListProperty([])  # Spinner 2 options

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.attributeX = None
        self.attributeY = None
        self.visfile_name = None

    
    def file_choose(self):
        filechooser.open_file(on_selection=self.visualizationfile)

    def visualizationfile(self,selection):
        self.visfile_name=selection
        
        # Open the CSV file
        with open(self.visfile_name[0], newline='') as csvfile:
            # Create a reader object
            reader = csv.reader(csvfile)
            # Read the header row
            header = next(reader)
            # Print the header row
            print(header)    

            # Update spinner options
            self.spinner1_options = header
            self.spinner2_options = header

    def spinner_clickedX(self,attribute): 
        self.attributeX = attribute

    def spinner_clickedY(self,attribute): 
        self.attributeY = attribute

    def generate_scatter_plot(self, *args):
        # Check if both attributes are selected
        if self.attributeX is None or self.attributeY is None:
            print("Please select both attributes.")
            return

        # Open the CSV file
        with open(self.visfile_name[0], newline='') as csvfile:
            # Create a reader object
            reader = csv.reader(csvfile)
            # Read the data rows
            data = list(reader)

        # Find the indices of selected attributes in the header row
        header = data[0]
        x_index = header.index(self.attributeX)
        y_index = header.index(self.attributeY)

        # Extract the selected attributes from the data
        x_values = [float(row[x_index]) for row in data[1:]]
        y_values = [float(row[y_index]) for row in data[1:]]

        # Create a scatter plot
        plt.scatter(x_values, y_values)
        plt.xlabel(self.attributeX)
        plt.ylabel(self.attributeY)
        plt.title("Scatter Plot")

        # Display the scatter plot
        plt.show()

    def generate_bar_graph(self, *args):
        # Check if both attributes are selected
        if self.attributeX is None or self.attributeY is None:
            print("Please select both attributes.")
            return

        # Open the CSV file
        with open(self.visfile_name[0], newline='') as csvfile:
            # Create a reader object
            reader = csv.reader(csvfile)
            # Read the data rows
            data = list(reader)

        # Find the indices of selected attributes in the header row
        header = data[0]
        x_index = header.index(self.attributeX)
        y_index = header.index(self.attributeY)

        # Extract the selected attributes from the data
        x_values = [row[x_index] for row in data[1:]]
        y_values = [float(row[y_index]) for row in data[1:]]

        plt.plot(x_values,y_values)
        plt.show()
        # Calculate the x-axis positions for the bars
        # x_pos = np.arange(len(x_values))

        # # Create a bar graph
        # fig, ax = plt.subplots()
        # ax.bar(x_pos, y_values, align='center')

        # # Set the x-axis tick labels
        # ax.set_xticks(x_pos)
        # ax.set_xticklabels(x_values, rotation=90)

        # ax.set_xlabel(self.attributeX)
        # ax.set_ylabel(self.attributeY)
        # ax.set_title("Bar Graph")

        # Display the bar graph
        # plt.show()

    def generate_histogram_chart(self, *args):
        # Check if both attributes are selected
        if self.attributeX is None or self.attributeY is None:
            print("Please select both attributes.")
            return

        # Open the CSV file
        with open(self.visfile_name[0], newline='') as csvfile:
            # Create a reader object
            reader = csv.reader(csvfile)
            # Read the data rows
            data = list(reader)
        
        # Find the indices of selected attributes in the header row
        header = data[0]
        x_index = header.index(self.attributeX)
        y_index = header.index(self.attributeY)

        # Extract the selected attributes from the data
        labels = [row[x_index] for row in data[1:]]
        sizes = [float(row[y_index]) for row in data[1:]]

        # Specify the attribute you want to create a histogram for
        attribute = x_index
        values = labels

        # Create a histogram
        plt.hist(values, bins=10)

        # Add labels and title
        plt.xlabel(attribute)
        plt.ylabel('Frequency')
        plt.title('Histogram')

        # Display the histogram
        plt.show()


        # # Create a pie chart
        # fig, ax = plt.subplots()
        # ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)

        # ax.set_title("Pie Chart")

        # # Equal aspect ratio ensures that pie is drawn as a circle
        # ax.axis('equal')

        # # Display the pie chart
        # plt.show()

	

class visualizationApp(MDApp):
    
    def build(self):
        global ScreenManager
        ScreenManager= ScreenManager()
        ScreenManager.add_widget(visualizationwindow())
        return ScreenManager

if __name__=='__main__':
     visualizationApp().run()
