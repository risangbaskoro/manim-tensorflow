from manim import *


class Edge(Line):
    def __init__(self, start, end, buff=0, path_arc=None, **kwargs):
        super().__init__(start, end, buff, path_arc, **kwargs)
