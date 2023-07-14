from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang.builder import Builder
from kivy.animation import Animation
from kivy.clock import Clock
from kivy.uix.button import Button

from .info.infoScreen import InfoScreen
from .monkeyRendering.render import Screen3DRendering
from .touchtracer.main import TouchTracerScreen
from .showcase.main import ShowcaseFullScreen
from .camera.camera_main import CameraScreen

from kivy.properties import ListProperty, NumericProperty

from time import time
from functools import partial

from kivydemo import path_demo
from os import path


class StartScreen(Screen):

    def __init__(self, *args, **kwargs):
        Builder.load_file(path.join(path_demo, "startScreen.kv"))
        super().__init__(*args, **kwargs)

    def startFadeOutAnimation(self):
        animation = Animation(duration=3, opacity=0)
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

    def build(self):
        sm = ScreenManager()
        self.title = "Demo kivy"

        startScreen = StartScreen(name="start")
        homeScreen = HomeScreen(name="home")
        infoScreen = InfoScreen(name="info")
        threeDScreen = Screen3DRendering(name="3D")
        touchtracerScreen = TouchTracerScreen(name="touch")
        showcaseScreen = ShowcaseFullScreen(name="showcase")
        cameraScreen = CameraScreen(name="camera")

        sm.add_widget(startScreen)
        sm.add_widget(homeScreen)
        sm.add_widget(infoScreen)
        sm.add_widget(threeDScreen)
        sm.add_widget(touchtracerScreen)
        sm.add_widget(showcaseScreen)
        sm.add_widget(cameraScreen)

        # Animation of the first page
        startScreen.startFadeOutAnimation()
        Clock.schedule_once(partial(homeScreen.switchToHome, sm), 3.5)
        # This line is for the progress bar (not the most efficient solution)
        Clock.schedule_interval(self._update_clock, 1 / 60.)
        return sm

    def _update_clock(self, dt):
        self.time = time()


def runMainFunction():
    DemoApp().run()


if __name__ == '__main__':
    # DemoApp().run()
    runMainFunction()
