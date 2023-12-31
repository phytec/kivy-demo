from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang.builder import Builder
from kivy.animation import Animation
from kivy.clock import Clock

from .info.info_main import InfoScreen
from .monkeyRendering.render import Screen3DRendering
from .touchtracer.touchtracer_main import TouchTracerScreen
from .showcase.showcase_main import ShowcaseFullScreen
from .camera.camera_main import CameraScreen
from .audio.audio_main import AudioScreen


from kivy.properties import ListProperty, NumericProperty

from time import time
from functools import partial

from kivydemo import path_demo
from os import path
import argparse


class StartScreen(Screen):

    def __init__(self, *args, **kwargs):
        Builder.load_file(path.join(path_demo, "startScreen.kv"))
        super().__init__(*args, **kwargs)

    def startFadeOutAnimation(self):
        animation = Animation(duration=1, opacity=0)
        animation.start(self.ids.welcome)
    pass


class HomeScreen(Screen):

    def __init__(self, *args, **kwargs):
        Builder.load_file(path.join(path_demo, "HomeScreen.kv"))
        super().__init__(*args, **kwargs)

    def switchToHome(self, sm, dt):
        # ok, far from cool way to do that because only the sreen manager know this information !
        sm.current = 'home'
        # change that !

    # TODO: Check import Image !


class DemoApp(App):

    demos = ListProperty([])
    time = NumericProperty(0)
    parser = argparse.ArgumentParser(
        description='Run demo for kivy for PHYTEC products.')
    parser.add_argument('--camera', action='store_true',
                        help="Allow camera in demo")
    parser.add_argument('--audio', action='store_true',
                        help="Allow audio in demo")
    args = parser.parse_args()

    def build(self):
        sm = ScreenManager()
        self.title = "Demo kivy"

        startScreen = StartScreen(name="start")
        homeScreen = HomeScreen(name="home")
        infoScreen = InfoScreen(name="info")
        threeDScreen = Screen3DRendering(name="3D")
        touchtracerScreen = TouchTracerScreen(name="touch")
        showcaseScreen = ShowcaseFullScreen(name="showcase")

        sm.add_widget(startScreen)
        sm.add_widget(homeScreen)
        sm.add_widget(infoScreen)
        sm.add_widget(threeDScreen)
        sm.add_widget(touchtracerScreen)
        sm.add_widget(showcaseScreen)

        if self.args.camera:
            cameraScreen = CameraScreen(name="camera")
            sm.add_widget(cameraScreen)

        if self.args.audio:
            audioScreen = AudioScreen(name="audio")
            sm.add_widget(audioScreen)

        # Animation of the first page
        startScreen.startFadeOutAnimation()
        Clock.schedule_once(partial(homeScreen.switchToHome, sm), 1.5)
        # This line is for the progress bar (not the most efficient solution)
        Clock.schedule_interval(self._update_clock, 1 / 60.)
        return sm

    def _update_clock(self, dt):
        self.time = time()

    def has_no_camera(self):
        return self.args.camera

    def has_no_audio(self):
        return self.args.audio


def runMainFunction():
    DemoApp().run()


if __name__ == '__main__':
    runMainFunction()
