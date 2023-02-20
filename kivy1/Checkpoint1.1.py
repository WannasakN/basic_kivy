import kivy
from kivy.app import App
from kivy.uix.label import Label

class MyApp(App):
    def build(self):
        return Label(text='Wannasak Nooplod', font_size ='90')
if __name__ == '__main__':
    MyApp().run()
