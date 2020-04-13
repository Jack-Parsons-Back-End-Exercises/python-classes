class Pizza:
    def __init__(self):
        self.size = ""
        self.style = ""
        self.toppings = []

    def add_topping(self, topping):
        self.toppings.append(topping)

    def print_order(self):
        print(f'I would like a {self.size}-inch, {self.style} pizza with {self.toppings[0]} & {self.toppings[1]}.')