from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.lang import Builder
from kivy.clock import Clock


Builder.load_string('''
<Base>:
    Button:
        text: 'Press for Popup'
        on_press: root.edit_text()
''')


class Base(BoxLayout):
    def __init__(self, **kwargs):
        super(Base, self).__init__(**kwargs)

    def edit_text(self, *args):
        self.clear_widgets()
        content = TextInputX()
        popup = Popup(content=content)
        popup.open()


class TextInputX(TextInput):
    def __init__(self, **kwargs):
        super(TextInputX, self).__init__(**kwargs)
        def set_focus(dt):
            self.focus = True
        Clock.schedule_once(set_focus, 1)


class SampleApp(App):
    def build(self):
        return Base()


if __name__ == '__main__':
    SampleApp().run()
