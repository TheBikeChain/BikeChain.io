import kivy
import random
 
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.button import Label
from kivy.uix.boxlayout import BoxLayout
 

class VBoxLayoutExample(App):
    """
    Vertical oriented BoxLayout example class
    """
 
    #----------------------------------------------------------------------
    def setOrientation(self, orient):
        """"""
        self.orient = orient
 
    #----------------------------------------------------------------------
    def build(self):
        """"""
        layout = BoxLayout(padding=10, orientation=self.orient)
        l = Label(text='BikeChain')
        layout.add_widget(l)
        ia = Button(text="Import ETH Address")
        layout.add_widget(ia)
        rgb = Button(text="Register Bike")
        layout.add_widget(rgb)
        rpb = Button(text="Report Bike")
        layout.add_widget(rpb)
        rcb = Button(text="Recover Bike")
        layout.add_widget(rcb)
        sdb = Button(text="Search BikeChain")
        layout.add_widget(sdb)

        return layout
 
#----------------------------------------------------------------------
if __name__ == "__main__":
    #app = HBoxLayoutExample()
    app = VBoxLayoutExample()
    app.setOrientation(orient="vertical")
    app.run()
