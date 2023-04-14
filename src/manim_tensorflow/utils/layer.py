from manim import *


class Layer(object):
    def __init__(
            self,
            previous_layer: Mobject | None = None,
    ):
        self.previous_layer = previous_layer

    def __call__(self, inputs, *args, **kwargs):
        return self.__init__(inputs)

    def call(self, inputs, *args, **kwargs):
        self.call(inputs, *args, **kwargs)
