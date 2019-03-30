'''
Install below pytohn module before you run this code
>>> pip install kivy --upgrade
'''

from kivy.app import App
from kivy.uix.label import Label
		
class SimpleKivy(App):
    def build(self):
        return Label(text="Hello World!")

if __name__ == "__main__":
    SimpleKivy().run()