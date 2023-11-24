from ast import List

from seminar1.in_memory_model.i_model_change_observer import IModelChanger, IModelChangeObserver


class ModelStore(IModelChanger):
    def __init__(self, changeObservers: List[IModelChangeObserver]):
        self.changeObservers = changeObservers
        self.models = []
        self.scenes = []
        self.flashes = []
        self.cameras = []

    def get_scene(self, id):
        for scene in self.scenes:
            if scene.id == id:
                return scene
        return None

    def notify_change(self, sender) -> None:
        return super().notify_change(sender)