class Pizza:
    def __init__(self, toppings):
        self.toppings = toppings
        
    def add_topping(self, new_topping):
        self.toppings += new_topping
        
class FancyPizza(Pizza):
        
    def get_fancy_first_topping(self):
        return f"Fancy {self.toppings[0]}"

cheese = Pizza(["cheese"])
pepperoni = FancyPizza(["pepperoni"])

pepperoni.add_topping("mushroom")

print(pepperoni.get_fancy_first_topping())
print(pepperoni.toppings)