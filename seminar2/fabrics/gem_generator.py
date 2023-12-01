from seminar2.fabrics.item_fabric import ItemGeneratorInterface
from seminar2.products.gem import Gem


class GemGenerator(ItemGeneratorInterface):
    """Генератор алмазов"""
    def create_item(self) -> Gem:
        return Gem()