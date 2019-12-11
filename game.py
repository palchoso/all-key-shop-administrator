class Game:
    def __init__(self,name1,price1,price2):
        self.name = name1
        self.price = price1
        self.price2 = price2

    def imp(self):
        print(f"{self.name} {self.price} {self.price2}")
        return (f"{self.name} {self.price} {self.price2}")

