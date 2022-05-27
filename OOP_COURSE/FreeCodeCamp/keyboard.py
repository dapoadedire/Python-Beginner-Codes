from items import Item


class Keyboard(Item):
    discount_rate = 0.7
    def __init__(self, name: str, price: float, quantity=0):
        super().__init__(
            name, price, quantity
        )
