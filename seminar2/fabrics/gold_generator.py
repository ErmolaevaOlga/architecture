from seminar2.fabrics.item_fabric import ItemGeneratorInterface
from seminar2.products.gold import Gold


class GoldGenerator(ItemGeneratorInterface):
    """Геренатор золота"""
    def create_item(self) -> Gold:
        return Gold()