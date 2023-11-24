from seminar1.model_elements.camera import Camera
from seminar1.model_elements.flash import Flash
from seminar1.model_elements.poligonal_model import PoligonalModel


class Scene:
    def __init__(self, models: list[PoligonalModel], flashes: list[Flash]) -> None:
        self.id: int = 0
        self.models: list[PoligonalModel] = models
        self.flashes: list[Flash] = flashes

    def method1(self, object: "Type") -> "Type":
        pass

    def method2(self, object1: "Type", object2: "Type") -> "Type":
        pass
