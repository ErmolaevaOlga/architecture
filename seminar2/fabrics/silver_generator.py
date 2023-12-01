from seminar2.fabrics.item_fabric import ItemGeneratorInterface
from seminar2.products.silver import Silver


class SilverGenerator(ItemGeneratorInterface):
    """Генератор сереба"""
    def create_item(self) -> Silver:
        return Silver()