from manim import *

from manim_tensorflow.keras.layers.dense import Dense


class DenseScene(Scene):
    def construct(self):
        layer1 = Dense(10, color=BLUE)
        rect1 = layer1.surrounding_rectangle.move_to(layer1.get_center())
        layer2 = Dense(64).next_to(layer1, RIGHT)
        rect2 = layer2.surrounding_rectangle.move_to(layer2.get_center())
        layer3 = Dense(8).next_to(layer2, RIGHT)
        rect3 = layer3.surrounding_rectangle.move_to(layer3.get_center())
        layer4 = Dense(1).next_to(layer3, RIGHT)
        rect4 = layer4.surrounding_rectangle.move_to(layer4.get_center())

        group = VGroup(layer1, layer2, layer3, layer4)

        self.play(Write(group))

        self.play(Write(rect1))
        self.wait()

        self.play(ReplacementTransform(rect1, rect2))
        self.wait()

        self.play(ReplacementTransform(rect2, rect3))
        self.wait()

        self.play(ReplacementTransform(rect3, rect4))
        self.wait()

