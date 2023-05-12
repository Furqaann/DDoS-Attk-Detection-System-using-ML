from kivymd.uix.behaviors import FakeRectangularElevationBehavior
from kivymd.uix.card import MDCard
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.properties import StringProperty
from kivymd.uix.screen import Screen

Builder.load_string("""
<HeroCard>
    orientation:"vertical"
    size_hint:1, None
    height:"420dp"
    elevation:4
    radius:24
    padding:12

    MDHeroFrom:
        id: hero_from
        size_hint:1,None
        height:root.height/1.6

        FitImage:
            source:root.source
            size_hint:None,None
            size:hero_from.size
            radius:24

    MDLabel:
        text:root.label_text
        bold:True
        adaptive_height:True
        padding:12,12
        font_style:"H5"

    MDLabel:
        text:root.description
        padding:12,12
""")

class ElevationCard(FakeRectangularElevationBehavior, MDCard):
    pass

class HeroCard(ElevationCard):
    label_text = StringProperty()
    source= StringProperty()
    description=StringProperty()

class cardsApp(MDApp):
	def build(self):
		return HeroCard()

if __name__ == '__main__':
	cardsApp().run()