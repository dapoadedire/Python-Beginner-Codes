class User:
    def __init__(self, name, user_type):
        self.name = name
        self.user_type = user_type

    def update_user_type(self, new_type):
        print("Updating membership")
        self.user_type = new_type


