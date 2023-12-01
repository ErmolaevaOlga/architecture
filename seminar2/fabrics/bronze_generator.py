from seminar2.fabrics.item_fabric import ItemGeneratorInterface
from seminar2.products.bronze import Bronze


class BronzeGenerator(ItemGeneratorInterface):
    """Генератор бронзы"""
    def create_item(self) -> Bronze:
        return Bronze()