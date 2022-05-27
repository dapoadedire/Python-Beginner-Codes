from items import Item


class Phone(Item):
    def __init__(self, name: str, price: float, quantity=0, broken=0):
        #Call to super function to have access to all attributes/function.\
        super().__init__(
            name, price, quantity
        )
        # Run validations to the received arguments.
        assert broken >= 0, f"Broken phones {broken} is not greater than or equal to zero"
        #Assign to self object
        self.broken = broken

