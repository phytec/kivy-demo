'''
Audio example
=============

This example plays sounds of different formats. You should see a grid of
buttons labelled with filenames. Clicking on the buttons will play, or
restart, each sound. Not all sound formats will play on all platforms.

All the sounds are from the http://woolyss.com/chipmusic-samples.php
"THE FREESOUND PROJECT", Under Creative Commons Sampling Plus 1.0 License.

'''

from os.path import basename
from glob import glob
from kivy.properties import StringProperty, ObjectProperty, NumericProperty
from kivy.core.audio import SoundLoader
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.clock import Clock
from os import path

from kivydemo import path_demo


class AudioButton(Button):

    filename = StringProperty(None)
    sound = ObjectProperty(None, allownone=True)
    volume = NumericProperty(1.0)

    def on_press(self):
        if self.sound is None:
            self.sound = SoundLoader.load(self.filename)
        # stop the sound if it's currently playing
        if self.sound.status != 'stop':
            self.sound.stop()
        self.sound.volume = self.volume
        self.sound.play()

    def release_audio(self):
        if self.sound:
            self.sound.stop()
            self.sound.unload()
            self.sound = None

    def set_volume(self, volume):
        self.volume = volume
        if self.sound:
            self.sound.volume = volume


class AudioBackground(BoxLayout):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        Clock.schedule_once(self.build_stack, -1)

    def build_stack(self, dt):
        for fn in glob(path.join(path_demo, "audio/*.wav")):
            btn = AudioButton(
                text=basename(fn[:-4]).replace('_', ' '), filename=fn,
                size_hint=(None, None), halign='center',
                size=(128, 128), text_size=(118, None))
            self.ids.sl.add_widget(btn)

    def release_audio(self):
        for audiobutton in self.ids.sl.children:
            audiobutton.release_audio()

    def set_volume(self, value):
        for audiobutton in self.ids.sl.children:
            audiobutton.set_volume(value)


class AudioScreen(Screen):
    def __init__(self, *args, **kwargs):
        Builder.load_file(path.join(path_demo, "audio/audio.kv"))
        super().__init__(*args, **kwargs)
        # root = AudioBackground(spacing=5)
