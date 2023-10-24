class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, product, quantity):
        self.items.append({'product': product, 'quantity': quantity})

    def remove_item(self, product_name):
        for item in self.items:
            if item['product'].name == product_name:
                self.items.remove(item)
                return
        print(f"{product_name} not found in the cart.")

    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item['product'].price * item['quantity']
        return total

    def display_cart(self):
        print("Shopping Cart Contents:")
        for item in self.items:
            print(f"{item['product'].name} - ${item['product'].price:.2f} x {item['quantity']}")

if __name__ == "__main":
    apple = Product("Apple", 0.5)
    banana = Product("Banana", 0.25)
    laptop = Product("Laptop", 1000.0)

    cart = ShoppingCart()

    cart.add_item(apple, 10)
    cart.add_item(banana, 5)
    cart.add_item(laptop, 2)

    cart.display_cart()
    total_cost = cart.calculate_total()
    print(f"Total cost of the items in the cart: ${total_cost:.2f}")

    cart.remove_item("Apple")
    cart.display_cart()
