from kivymd.app import MDApp
from kivy.lang import Builder
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
from plyer import filechooser
# from StartPage import SystemLayout
# from MainMenu import Home_PageWindow
# from Featureselection import featurewindow
# from Acquisition import screenwid
from cards import HeroCard
import csv
from plyer import filechooser
	    
# Designate Our .kv design file 
Builder.load_file('ModelBuild.kv')
# train_df = [selected_features]
# test_df = [selected_features]
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
        # Load your dataset skipping the first row
        X = np.genfromtxt(file_name[0], delimiter=',', skip_header=1)
        # Initialize PCA with the number of components you want to keep(how many dimentions you want to reduce data)
        pca = PCA(n_components=10)
        # Apply PCA on your dataset
        global X_pca 
        X_pca = pca.fit_transform(X)
        # print(X_pca)
        return X_pca
        
############################################################# univariate Feature Selection ################################################
    def UFS(self):
        # Load the dataset
        data = pd.read_csv(file_name[0])

        # Separate the features and the target variable
        X = data.drop(columns=['class'])
        y = data['class']

        # Apply univariate feature selection
        selector = SelectKBest(score_func=f_classif, k=20)
        selector.fit(X, y)

        # Get the selected features
        selected_features = X.columns[selector.get_support()]

        # Concatenate the selected features and the target variable column
        selected_df = pd.concat([X[selected_features], y], axis=1)

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
    
    
class MyLayout(Screen):
	pass
	    
class ModelBuildApp(MDApp):	
	global model	

	image_list=[
		"images/DecisiontreeAlgo.jpeg",
		"images/pic2.jpeg",
		"images/pic3.jpeg",
		"images/pic5.jpeg",
		"images/pic6.jpeg",
		"images/pic7.jpeg",
		"images/pic8.jpeg",
		"images/pic9.jpeg",
		"images/randomforest.jpeg",
	]
	label_list=[
		"Decision Tree",
		"Logistic Regression(LR)",
		"Naive Bayes(NB)",
		"K Nearest Neighbour",
		"Support Vector Machines",
		"Convolutional Neural Networks (CNNs)",
		"Baysein Network",
		"Gradient Boosting Classifier",
		"Random Forest",
	]
	description_list=[
		"Can solve a non-linear problems Can Work on high-dimensional data with excellent accuracy Easy to visualize and explain",
		"It is much easier to set up and train than other machine learning and AI applications. It is one of the most efficient algorithms when the different outcomes or distinctions represented by the data are linearly separable.",
		"Naive Bayes methods are a set of supervised learning algorithms based on applying Bayes' theorem with the “naive” assumption of conditional independence between every pair of features given the value of the class variable",
		"The k-nearest neighbors algorithm, also known as KNN or k-NN, is a non-parametric, supervised learning classifier, which uses proximity to make classifications or predictions about the grouping of an individual data point.",
		"SVM are a set of supervised learning methods used for classification, regression and outliers detection.It is Effective in high dimensional spaces.Still effective in cases where number of dimensions is greater than the number of samples. It is also memory efficient.",
		"A deep learning algorithm that can automatically learn features from raw data, such as packet headers and payloads, and can be used to classify incoming packets.",
		"A Bayesian network (BN) is a probabilistic graphical model for representing knowledge about an uncertain domain where each node corresponds to a random variable and each edge represents the conditional probability for the corresponding random variables",
		" It is an ensemble learning algorithm that combines multiple weak classifiers to create a strong classifier",
		"Random forest is a commonly-used machine learning algorithm trademarked by Leo Breiman and Adele Cutler, which combines the output of multiple decision trees to reach a single result. Its ease of use and flexibility have fueled its adoption"
	]
	def build(self,*args):

		global screenmang
		screenmang = ScreenManager()
		screenmang.add_widget(featurewindow())
		screenmang.add_widget(MyLayout())
		# screenmang.add_widget(SystemLayout())
		# screenmang.add_widget(Home_PageWindow())
		# screenmang.add_widget(screenwid())
		# screenmang.add_widget(featurewindow())
		# screenmang.add_widget(MyLayout())
		screenmang.add_widget(traintestwindow())
		self.on_enter()
		return screenmang
	
	def on_enter(self,*args):
		if not screenmang.get_screen("mainwin").ids.hero_list.children:
			for i, (source, label_text,description) in enumerate(zip(self.image_list, self.label_list,self.description_list)):
				screenmang.get_screen("mainwin").ids.hero_list.add_widget(
					HeroCard(source=source,label_text=label_text,description=description, on_press=lambda x,i=i:self.checkclicked(i))
				)
	def checkclicked(self,i):
		if (i==0):
			self.DecisionTree_classifier()
			screenmang.current='traintest'
			print("Clicked Decision Tree classifier")
		elif(i==1):
			self.LogisticRegression_classifier()
			screenmang.current='traintest'
			print("Clicked Logistic Regression classifier")
		elif(i==2):
			self.NaiveBayes_classifier()
			screenmang.current='traintest'
			print("Clicked Naive Bayes classifier")
		elif(i==3):
			self.K_NearestNeighbour_classifier()
			screenmang.current='traintest'
			print("Clicked K Nearest Neighbour classifier")
		elif(i==4):
			self.SupportVectorMachine_classifier()
			screenmang.current='traintest'
			print("Clicked Support Vector classifier")
		elif(i==5):
			screenmang.current='traintest'
			print("Clicked Convolutional Neural Networks")
		elif(i==6):
			screenmang.current='traintest'
			print("Clicked Baysein Network classifier")
		elif(i==7):
			screenmang.current='traintest'
			print("Clicked Gradient Boosting classifier")
		elif(i==8):
			screenmang.current='traintest'
			print("Clicked Random Forest classifier")
		

	def DecisionTree_classifier(self):
		model = DecisionTreeClassifier(random_state=42)

	def LogisticRegression_classifier(self):
		# model = LogisticRegression()
		# model.fit(X_train, y_train)
		pass
	def NaiveBayes_classifier(self):
		# model = GaussianNB()
		# model.fit(X_train, y_train)
		pass
	def K_NearestNeighbour_classifier(self):
		# model = KNeighborsClassifier()
		# model.fit(X_train, y_train)
		pass
	def SupportVectorMachine_classifier(self):
		# model = SVC()
		# model.fit(X_train, y_train)
		pass
	def BayesianNetwork_classifier(self):
		# model = BayesianModel()
		# model.fit(X_train, y_train)
		pass
	def GradientBoosting_classifier(self):
		# model = GradientBoostingClassifier()
		# model.fit(X_train, y_train)
		pass
	def RandomForest_classifier(self):
		# model = RandomForestClassifier()
		# model.fit(X_train, y_train)
		pass



class traintestwindow(Screen):    
    global train_df
    train_df= pd.read_csv('training_data.csv')
    global test_df
    test_df= pd.read_csv('testing_data.csv')
    global X_train
    X_train = train_df.drop(columns=['class'])
    global y_train
    y_train = train_df['class']
    global X_test
    X_test = test_df.drop(columns=['class'])
    global y_test
    y_test = test_df['class']
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)  
        
    def traintestfile_chooser(self):
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
	
if __name__ == '__main__':
	ModelBuildApp().run()