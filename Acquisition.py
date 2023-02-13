from kivymd.app import MDApp
from kivy.app import App
from kivy.lang import Builder
import os
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn import preprocessing
from kivy.core.window import Window
from kivymd.uix.screenmanager import ScreenManager
from kivymd.uix.screen import Screen
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
import csv
import random

Builder.load_string("""
<screenwid>:
    name:"z"
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
                background_color:(70/255,81/255,83/255,1)
                background_normal:''
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
                    #     RoundedRectangle:
                    #         size:   self.size
                    #         pos:    self.pos
                    #         radius: [20]
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
                    on_selection: main_win.selected(filechooser.selection)
                
                Button:
                    text:"Get Table"
                    size_hint:(0.4,0.1)
                    pos_hint: {"x":0.15,"top":0.68}
                    background_color:(134/255, 93/255, 201/255,1)
                    background_normal:''
                    canvas.before:
                        Color:
                            rgba:(1, 1, 1,1)
                        Line:
                            width: 2
                            rectangle: self.x, self.y , self.width, self.height
                    on_press:
                        main_win.tablecheck()

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

""")

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

        sc.get_screen("z").ids.content.add_widget(table)

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
            column_data =[(col, dp(30))
                for col in cols
            ] ,
			row_data = values
			)

        table.bind(on_check_press = self.checked)
        table.bind(on_row_press = self.row_checked)

        # self.theme_cls.theme_style= 'Dark'
        # self.theme_cls.primary_palette= 'BlueGray'

        sc.get_screen("z").ids.content.add_widget(table)

    def checked(self,instance_table,current_row):
        print(instance_table,current_row)
    def row_checked(self,instance_table,instance_row):
        print(instance_table,instance_row)

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
        scaler.fit(df)

        # Transform the data
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

        # Open the input CSV file
        with open(file_name[0], 'r') as input_file:
            # Create a CSV reader object
            reader = csv.reader(input_file)

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

        # reader.to_csv(os.path.join(str('training_data') + str('.csv')), index=None, header=True)
        # reader.to_csv(os.path.join(str('testing_data') + str('.csv')), index=None, header = True)
        # Open the training data CSV file
        with open('training_data.csv', 'w', newline='') as training_file:
            # Create a CSV writer object
            writer = csv.writer(training_file)
            # Write the training data to the CSV file
            writer.writerows(training_data)

        # Open the testing data CSV file
        with open('testing_data.csv', 'w', newline='') as testing_file:
            # Create a CSV writer object
            writer = csv.writer(testing_file)
            # Write the testing data to the CSV file
            writer.writerows(testing_data)
        
        print("Successfully Dataset splitted into testing and training")


    def close_window(self,obj):
        App.get_running_app().stop()
        Window.close()

class Acquisition(MDApp):
    def build(self):
        global sc
        sc= ScreenManager()
        sc.add_widget(screenwid())
        return sc
    
    
    

if __name__=='__main__':
    Acquisition().run()