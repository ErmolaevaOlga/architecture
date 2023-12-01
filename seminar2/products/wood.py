from seminar2.products.item_product import ItemInterface


class Wood(ItemInterface):
    def open(self) -> None:
        print('Wood!')