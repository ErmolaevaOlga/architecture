from seminar2.fabrics.item_fabric import ItemGeneratorInterface
from seminar2.products.wood import Wood


class WoodGenerator(ItemGeneratorInterface):
    """Генератор дерева"""
    def create_item(self) -> Wood:
        return Wood()