import numpy as np
from manim import *

from manim_tensorflow.keras.layers.dense import Dense
from manim_tensorflow.utils.edge import Edge
from manim_tensorflow.utils.layer_filler import LayerFiller


class Sequential(VGroup):
    def __init__(
            self,
            layers: list[Dense],  # TODO Add name and inherits from Module object
            model_config: dict | None = None,
    ):
        VGroup.__init__(self)

        self.model_config = {
            "direction": RIGHT,
            "buff": 1,
        }

        if model_config is not None:
            self.model_config = merge_dicts_recursively(self.model_config, model_config)

        self.layers = layers

        if self.layers is not None:
            self.add(*self.layers)

        self._arrange_layers()
        self._create_edges()

    def _create_edges(self):
        self.edges = VGroup()
        for i, layer in enumerate(self.layers):
            if i == 0:
                continue
            else:
                prev_layer = self.layers[i - 1]
                self._create_layer_edges(prev_layer, layer)
                self.edges.add(self.layer_edges).z_index = -1

    def _create_layer_edges(self, prev_layer, layer):
        self.layer_edges = VGroup()
        for neuron in prev_layer.neurons:
            for next_neuron in layer.neurons:
                if isinstance(neuron, LayerFiller):
                    break
                if isinstance(next_neuron, LayerFiller):
                    continue
                edge = Edge(
                    neuron.get_edge_center(self.model_config["direction"]),
                    next_neuron.get_edge_center(LEFT),  # TODO: Change to opposite direction
                    stroke_width=1,
                    color=GRAY_B,
                )
                self.layer_edges.add(edge)

    def _arrange_layers(self):
        direction = self.model_config["direction"]
        buff = self.model_config["buff"]
        self.arrange(direction, buff=buff)
        self.center()
