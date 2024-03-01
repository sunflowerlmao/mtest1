from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.core.audio import SoundLoader
from kivy.uix.image import Image

class MainApp(App):
    def build(self):
        main_layout = BoxLayout(orientation="horizontal")
        buttons = ['pik','sirena','streljat','trr','wow','stop']
        img = Image(source='mus.jpeg',
                    size_hint=(1, .5),
                    pos_hint={'center_x': .5, 'center_y': .5})
        for i in buttons:
            h_layout = BoxLayout()
            button = Button(
                text=i,
                pos_hint={"center_x": 0.5, "center_y": 0.5},
            )
            button.bind(on_press=self.on_press_button)
            h_layout.add_widget(button)
            main_layout.add_widget(h_layout)
        main_layout.add_widget(img)


        return main_layout

    def on_press_button(self, instance):
        buttontext = instance.text
        pik = SoundLoader.load('pik.wav')
        sirena = SoundLoader.load('sirena.wav')
        streljat = SoundLoader.load('streljat.mp3')
        trr = SoundLoader.load('trr.wav')
        wow = SoundLoader.load('wowow.wav')
        if buttontext == 'pik':
            pik.play()
        if buttontext == 'sirena':
            sirena.play()
        if buttontext == 'streljat':
            streljat.play()
        if buttontext == 'trr':
            trr.play()
        if buttontext == 'wow':
            wow.play()
        if buttontext == 'stop':
                pik.stop()
                sirena.stop()
                streljat.stop()
                trr.stop()
                wow.stop()


if __name__ == '__main__':
    app = MainApp()
    app.run()