from manim import *

from manim_tensorflow.keras.layers.dense import Dense
from manim_tensorflow.keras.sequential import Sequential


class ModelScene(Scene):
    def construct(self):
        model = Sequential([
            Dense(10),
            Dense(5),
            Dense(2),
        ])

        self.play(Write(model))
        self.wait()
