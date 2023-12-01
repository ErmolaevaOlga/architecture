from abc import ABC, abstractmethod
from seminar2.products.item_product import ItemInterface


class ItemGeneratorInterface(ABC):
    @abstractmethod
    def create_item(self) -> ItemInterface:
        raise NotImplementedError("Method create_item was not implemented")
