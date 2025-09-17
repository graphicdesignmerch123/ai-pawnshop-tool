# Item model
class Item:
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price

    def __repr__(self):
        return f"Item(name={self.name}, price={self.price})"