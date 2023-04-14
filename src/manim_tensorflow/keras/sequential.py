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
            "edge_direction": RIGHT,
            "edge_buff": 1,
            "edge_stroke_width": 1,
            "edge_propagation_color": YELLOW,
        }

        if model_config is not None:
            self.model_config = merge_dicts_recursively(self.model_config, model_config)

        self.edge_direction = self.model_config["edge_direction"]
        self.edge_buff = self.model_config["edge_buff"]
        self.edge_stroke_width = self.model_config["edge_stroke_width"]
        self.edge_propagation_color = self.model_config["edge_propagation_color"]

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
                self.edges.add(self.layer_edges)

    def _create_layer_edges(self, prev_layer, layer):
        self.layer_edges = VGroup()
        for neuron in prev_layer.neurons:
            for next_neuron in layer.neurons:
                if isinstance(neuron, LayerFiller):
                    break
                if isinstance(next_neuron, LayerFiller):
                    continue
                edge = Edge(
                    neuron.get_edge_center(self.edge_direction),
                    next_neuron.get_edge_center(LEFT),  # TODO: Change to opposite direction
                    stroke_width=self.edge_stroke_width,
                    color=GRAY_B,
                )
                self.layer_edges.add(edge)

    def _arrange_layers(self):
        direction = self.edge_direction
        buff = self.edge_buff
        self.arrange(direction, buff=buff)
        self.center()

    def forward_pass_animation(
            self,
            index: int,
            run_time_per_edge_group: float = .03,
            time_width: float = 1.0
    ):
        edge_group_copy = self.edges[index].copy()
        edge_group_copy.set_stroke(
            color=self.edge_propagation_color,
            width=1.5 * self.edge_stroke_width
        )
        animation = ShowPassingFlash(
            edge_group_copy,
            run_time=len(edge_group_copy) * run_time_per_edge_group,
            lag_ratio=run_time_per_edge_group,
            time_width=time_width,
        )
        return animation
