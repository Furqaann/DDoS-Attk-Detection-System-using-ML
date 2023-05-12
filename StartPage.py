import kivy
from kivy.app import App
from kivymd.app import MDApp
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen
# from ModelBuild import *



# Designate Our .kv design file 
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
		 """)

class SystemLayout(Screen):
	pass

class DDoSApp(MDApp):
	def build(self):
            from MainMenu import Home_PageWindow
            from Featureselection import featurewindow
            from Acquisition import screenwid
            # from ModelBuild import MyLayout
            # from cards import HeroCard
	    
            screenm= ScreenManager()
            screenm.add_widget(SystemLayout())
            screenm.add_widget(Home_PageWindow())
            screenm.add_widget(screenwid())
            screenm.add_widget(featurewindow())
            # screenm.add_widget(MyLayout())
            return screenm

if __name__ == '__main__':
	DDoSApp().run() 
	# ModelBuildApp().run()