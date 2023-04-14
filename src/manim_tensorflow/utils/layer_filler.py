from manim import *


class LayerFiller(VGroup):
    def __init__(self, num=3, radius=.03, direction=DOWN, **kwargs):
        VGroup.__init__(self, **kwargs)
        self.direction = direction
        self.add(*[Dot(radius=radius, **kwargs) for _ in range(num)])
        self.arrange(direction, buff=kwargs.get("buff", 0.03))
