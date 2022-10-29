from kivy.app import App
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

# 日本語を適応させる
import japanize_kivy

# ウィンドウサイズの指定
Window.size = (240, 240)

Builder.load_file('./setting.kv')


class MainWidget(BoxLayout):
    pass

class MancoApp(App):
    
    def build(self):
        return MainWidget()


if __name__ == '__main__':
    MancoApp().run()

