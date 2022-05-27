class User:
    def log(self):
        print(self)

class Teacher(User):
    def log(self):
        print("I am a teacher")

class Customer(User):
    def __init__(self, name, membership_type):
        self.name = name
        self.membership_type = membership_type

    @property
    def name(self):
        # print("getting name")
        return self._name

    @name.setter
    def name(self, name):
        # print("setting name")
        self._name = name


    def update_membership(self, new_membership):
        print("Updating membership")
        self.membership_type = new_membership


    def __str__(self):
        return self.name + " " + self.membership_type

    def print_all_customers(customers):
        for customer in customers:
            print(customer)

    def __eq__(self, other):
        if self.name == other.name and self.membership_type == other.membership_type:
           return True

        return False
    __hash__ = None
    
    __repr__ = __str__
customers = [Customer("Farouq", "Diamond"),
           #  Customer("Adedapo", "Gold"),
            # Customer("Adedapo", "Gold"),
             Customer("Adedire", "Silver"),
             Customer("Tesla", "Bronze"),
             Teacher()]


#Customer.print_all_customers(customers)

#wrong #compare = customers[1].__eq__(customers[2])
#print(compare)
# print(customers[1] == customers[2])
#print(customers)

print(customers[1].name)


customers[3].log()
#Encapsulation
#Getter and setter methods

"""
        #invoke an API
        #update a database
        #charge the customers
        #calculate the costs
        #conquer the world
        #pretty much anything else
    def reading_customers():
        print("Reading customers from the database")




# customers[1].verified = False

customers[1].update_membership("Bronze")
customers[1].membership_type = "Steel"
print(customers[1].name, customers[1].membership_type)
Customer.reading_customers()

"""