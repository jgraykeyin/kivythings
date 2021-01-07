from kivy.app import App
from kivy.uix.videoplayer import VideoPlayer


class MyVideoApp(App):
    def build(self):
        self.player = VideoPlayer(
            source='office_theme.mp4',
            state='play',
            options={'allow_stretch': True}
        )
        return (self.player)


if __name__ == '__main__':
    MyVideoApp().run()