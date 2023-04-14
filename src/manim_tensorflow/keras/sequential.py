from manim import *

from manim_tensorflow.utils.layer import Layer


class Sequential(VGroup):
    def __init__(
            self,
            layers: list[Layer] | None = None,  # TODO Add name and inherits from Module object
            model_config: dict | None = None,
    ):
        VGroup.__init__(self)

        self.model_config = {
            "direction": RIGHT,
            "buff": 2,
        }

        if model_config is not None:
            self.model_config = merge_dicts_recursively(self.model_config, model_config)

        self.layers = layers

        if self.layers is not None:
            self.add(*self.layers)

        self._arrange_layers()

    def _arrange_layers(self):
        direction = self.model_config["direction"]
        buff = self.model_config["buff"]
        self.arrange(direction, buff=buff)
        self.center()
