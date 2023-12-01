from seminar2.products.item_product import ItemInterface


class Gem(ItemInterface):
    def open(self) -> None:
        print('Gem!')