from manim import *

from manim_tensorflow.keras.layers.dense import Dense


class DenseScene(Scene):
    def construct(self):
        layer1 = Dense(10, color=BLUE)
        layer2 = Dense(64).next_to(layer1, RIGHT)
        layer3 = Dense(8).next_to(layer2, RIGHT)
        layer4 = Dense(1).next_to(layer3, RIGHT)

        group = VGroup(layer1, layer2, layer3, layer4).center()

        self.play(Write(group))
        self.wait()
