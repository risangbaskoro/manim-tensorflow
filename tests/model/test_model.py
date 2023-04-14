from manim import *

from manim_tensorflow.keras.layers.dense import Dense
from manim_tensorflow.keras.sequential import Sequential


class ModelScene(Scene):
    def construct(self):
        model = Sequential([
            Dense(64),
            Dense(16),
            Dense(8),
            Dense(2),
        ])

        self.play(Write(model))
        self.wait()
        self.play(Write(model.edges))
