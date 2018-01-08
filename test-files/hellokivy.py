import kivy
kivy.require('1.10.0')
from kivy.app import App
from kivy.uix.button import Label
from kivy.uix.boxlayout import BoxLayout

class TestWidget(BoxLayout):
    def __init__(self, **args):
        super(TestWidget, self).__init__(**args)
        label = Label(
            text='Hello, world',
            color=(1, 0, 0, 1))
        self.add_widget(label)


class TestApp(App):
    def build(self):
        return TestWidget()


TestApp().run()
