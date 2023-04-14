from manim import *


class Model(VGroup):
    def __init__(
            self,
            *args,
            **kwargs
    ):
        VGroup.__init__(self)
        self.add(*args)
        self.arrange(RIGHT, buff=1)
        self.center()
