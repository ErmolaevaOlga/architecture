from seminar2.products.item_product import ItemInterface


class Gold(ItemInterface):
    def open(self) -> None:
        print('Gold!')