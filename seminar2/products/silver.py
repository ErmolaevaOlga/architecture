from seminar2.products.item_product import ItemInterface


class Silver(ItemInterface):
    def open(self) -> None:
        print('Silver!')