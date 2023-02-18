"""

Выбрать систему, которая может быть описана несколькими классами.

Описать исползуя классы и применить принципы ООП:

- Наследование

- Абстрактные классы и/или интерфейсы

- Сокрытие

- Инкапсуляция

У классов должно быть состояние (поля) и реализация поведения через методы.

Требований к типам полей (экземпляра/класса) и методов (экземпляра/класса/статические) нет, по необходимости как вы видите.

Написать код который создает необходимые экземпляры и демонстрирует работу систему.

Ограничений на количество классов нет, но конечно их тут будет не пара.

"""


from abc import ABC, abstractmethod


class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


class CartItem:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity
        self.total_price = self.product.price * self.quantity


class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def get_total_price(self):
        return sum([item.total_price for item in self.items])


class Checkout(ABC):
    @abstractmethod
    def process_payment(self, total_price):
        pass


class CreditCardCheckout(Checkout):
    def __init__(self, credit_card_number, expiration_date):
        self.credit_card_number = credit_card_number
        self.expiration_date = expiration_date

    def process_payment(self, total_price):
        print(f"Processing credit card payment of {total_price} with credit card number {self.credit_card_number} and expiration date {self.expiration_date}")


# Create some products
apple = Product("Apple", 0.5, 10)
banana = Product("Banana", 0.3, 15)
orange = Product("Orange", 0.4, 12)

# Create a shopping cart and add some items
cart = ShoppingCart()
cart.add_item(CartItem(apple, 2))
cart.add_item(CartItem(banana, 3))
cart.add_item(CartItem(orange, 1))

# Print the total price of the cart
print(f"Total price: {cart.get_total_price()}")

# Create a credit card checkout and process the payment
checkout = CreditCardCheckout("1234-5678-9012-3456", "12/22")
checkout.process_payment(cart.get_total_price())
