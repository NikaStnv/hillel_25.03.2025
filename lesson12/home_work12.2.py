class Item:
    def __init__(self, name, price, description, dimensions, measurement):
        self.price = price
        self.description = description
        self.dimensions = dimensions
        self.name = name
        self.measurement = measurement

    def __str__(self):
        return (f"{self.name}")


class User:
    def __init__(self, name, surname, phone, discount):
        self.name = name
        self.surname = surname
        self.phone = phone
        self.discount = discount

    def __str__(self):
        return (f"{self.name} {self.surname}, знижкa {self.discount}%")


class Purchase:
    def __init__(self, user):
        self.products = {}
        self.user = user
        self.total = 0

    def add_item(self, item, cnt):
        self.products[item] = cnt

    def __str__(self):
        result = [f"Чек клієнта:\n{self.user}"]
        for item, value in self.products.items():
            result.append(f"{item} {self.products[item]} {item.measurement} * {item.price}$ = "
                          f"{self.products[item] * item.price}$")
        return "\n".join(result)

    def get_total(self):
        self.total = 0
        for item, value in self.products.items():
            self.total += item.price * self.products[item]
        if self.user.discount > 0:
            self.total -= round(self.total * self.user.discount / 100, 2)
        return self.total


lemon = Item('lemon', 5, "yellow", "small", 'pcs.')
apple = Item('apple', 2, "red", "middle", 'pcs.')
banana = Item('banana', 3, 'green', 'baby', 'pcs.')
print(lemon)  # lemon, price: 5
print(apple)
print(banana)
#
buyer_1 = User("Ivan", "Ivanov", "02628162", 0)
# buyer_2 = User('Anna', 'Melnik', '02645631', 10)
# buyer_3 = User('Kira', 'Shevchenko', '02668422', 20)
# print(buyer_1)  # Ivan Ivanov
# print(buyer_2)
# print(buyer_3)
#
cart = Purchase(buyer_1)
cart.add_item(lemon, 4)
cart.add_item(apple, 20)
print(cart)
print(cart.get_total())
#
# cart.add_item(apple, 10)
# print(cart)
# print(cart.get_total())
#
# cart_2 = Purchase(buyer_2)
# cart_2.add_item(lemon, 7)
# cart_2.add_item(banana, 15)
# cart_2.add_item(apple, 8)
# print(cart_2)
# print(cart_2.get_total())
#
# cart_3 = Purchase(buyer_3)
# cart_3.add_item(lemon, 1)
# cart_3.add_item(banana, 20)
# cart_3.add_item(apple, 30)
# print(cart_3)
# print(cart_3.get_total())

"""
User: Ivan Ivanov
Items:
lemon: 4 pcs.
apple: 20 pcs.
"""
assert isinstance(cart.user, User) is True, 'Екземпляр класу User'
assert cart.get_total() == 60, "Всього 60"
assert cart.get_total() == 60, 'Повинно залишатися 60!'
cart.add_item(apple, 10)
print(cart)
"""
User: Ivan Ivanov
Items:
lemon: 4 pcs.
apple: 10 pcs.
"""

assert cart.get_total() == 40
