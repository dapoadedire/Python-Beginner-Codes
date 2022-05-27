import csv

class Item:
    discount_rate = 0.8 # The pay rate after 20% discount
    all = []

    def __init__(self, name: str, price: float, quantity=0):
        # Run valisations to the received arguments.
        assert price >=0, f"Price {price} is not greater than or equals to zero!"
        assert quantity >=0, f"Price {quantity} is not greater than or equals to zero!"
        #Assign to self object
        self.__name = name
        self.__price = price
        self.quantity = quantity
        
        # Actions to execute
        Item.all.append(self)


    @property
    #Property Decorator = Read-Only Attribute
    def name(self):
        return self.__name

    def apply_discount(self):
        self.__price = self.__price * self.discount_rate
        return self.__price   

    def apply_increment(self, increment_value):
        self.__price = self.__price * increment_value
        return self.__price   

    @property
    def price(self):
        return self.__price
    

    @name.setter
    def name(self, value):
        if len(value) > 10:
            raise Exception("The name of the value is too long")
        else:
            self.__name = value
        

    def calculate_total_price(self):
        return self.__price * self.quantity


    @classmethod
    def instantiate_from_csv(cls):
        with open('PYTHON/OOP_COURSE/items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
  
        for item in items:
            #print(item)
            Item(
                name = item.get('name'),
                price = float(item.get('price')),
                quantity = int(item.get('quantity')),
            )

    @staticmethod
    def is_integer(num):
        #We will count out the floats that are 5.0
        if isinstance(num, float):
            #Count out the float that are 0.0
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False


    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}, {self.__price}, {self.quantity}')"

    # @property
    # def read_only_name(self):
        # return "ABCDE"

    def __connect(self):
        pass

    
    def __prepare_body(self):
        return f"""\n
        We have {self.name} {self.quantity} times at the price of {self.price} per unit.
        You can get 100 units at the price of {self.apply_discount()} per unit. 
        Regards, Tesla.
        What is Lorem Ipsum?

        Lorem Ipsum is simply dummy text of the printing and typesetting industry. 
        Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. 
        It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. 
        It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.


        Where does it come from?

        Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of "de Finibus Bonorum et Malorum" (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, "Lorem ipsum dolor sit amet..", comes from a line in section 1.10.32.

        The standard chunk of Lorem Ipsum used since the 1500s is reproduced below for those interested. Sections 1.10.32 and 1.10.33 from "de Finibus Bonorum et Malorum" by Cicero are also reproduced in their exact original form, accompanied by English versions from the 1914 translation by H. Rackham.


        """
    
    def __send(self):
       pass
    def send_email(self):
        self.__connect()
        self.__prepare_body()
        self.__send()
