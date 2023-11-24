from abc import ABC, abstractmethod


class IModelChangeObserver(ABC):
    @abstractmethod
    def apply_update_model(self) -> None:
        pass


class IModelChanger(ABC):
    @abstractmethod
    def notify_change(self, sender) -> None:
        pass
