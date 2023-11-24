from seminar1.model_elements.poligon import Poligon
from seminar1.model_elements.texture import Texture


class PoligonalModel:
    def __init__(self, texture: list[Texture]) -> None:
        self.poligons: list[Poligon] = [Poligon()]
        self.texture: list[Texture] = texture