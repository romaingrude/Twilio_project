class Customer():

    def __init__(self, name, address, phonenumber):
        self.name = name
        self.address = address
        self.phonenumber = phonenumber

    def get_number(self):
        return self.phonenumber

    def get_address(self):
        return self.address

    def get_name(self):
        return self.name

