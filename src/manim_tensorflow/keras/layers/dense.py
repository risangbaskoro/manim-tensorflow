from manim import *

from manim_tensorflow.utils.layer_filler import LayerFiller
from manim_tensorflow.utils.neuron import Neuron


class Dense(VGroup):  # TODO: Inherit from Layer and Module
    def __init__(
            self,
            units: int,
            neuron_labels: Tex | str | None = None,
            neurons_config: dict | None = None,
            **kwargs
    ):
        VGroup.__init__(self, **kwargs)

        self.neurons_config = {
            "radius": 0.15,
            "direction": DOWN,
            "stroke_width": 2,
            "neuron_to_neuron_buff": SMALL_BUFF,
            "max_shown_neurons": 15,
        }

        if neurons_config is not None:
            self.neurons_config = merge_dicts_recursively(self.neurons_config, neurons_config)

        self.units = units

        self.neurons = self._create_neurons(
            self.neurons_config,
            color=kwargs.get("color", GRAY_B)
        )

        self.neuron_labels = neuron_labels

        self.add(self.neurons)

        self.surrounding_rectangle = self._create_surrounding_rect()

        # TODO: Add neuron labels (Text, Tex, etc.)

    def _create_neurons(
            self,
            neurons_config,
            **kwargs
    ) -> VGroup:
        radius = neurons_config["radius"]
        direction = neurons_config["direction"]
        stroke_width = neurons_config["stroke_width"]
        buff = neurons_config["neuron_to_neuron_buff"]
        max_neurons = neurons_config["max_shown_neurons"]

        units = self.units
        num_neurons = self.units

        neurons = VGroup()

        filler = None
        if units > max_neurons:
            num_neurons = max_neurons
            filler = VGroup(*[LayerFiller(radius=.03, **kwargs) for _ in range(3)])
            filler.arrange(direction, buff=buff / 3)

        for _ in range(num_neurons):
            if _ == num_neurons // 2 and units > max_neurons and filler is not None:
                neurons.add(filler)
            else:
                neuron = Neuron(
                    radius=radius,
                    stroke_width=stroke_width,
                    **kwargs
                )
                neurons.add(neuron)

        neurons.arrange(
            direction,
            buff=buff,
        )

        return neurons

    def _create_surrounding_rect(self) -> SurroundingRectangle:
        return SurroundingRectangle(
            self.neurons,
            stroke_width=self.neurons_config["stroke_width"],
            buff=0.1,
        )
