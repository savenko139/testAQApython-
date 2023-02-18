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
    """

    Product class: This class will represent a product that can be added to the shopping cart.
    It will have fields for the name, price, and quantity.

    """

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


class CartItem:
    """

    CartItem class: This class will represent an item in the shopping cart.
    It will have fields for the product being purchased, the quantity of the product, and the total price of the item.

    """
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity
        self.total_price = self.product.price * self.quantity


class ShoppingCart:
    """

    ShoppingCart class: This class will represent the shopping cart itself.
    It will have fields for the items in the cart, and methods to add and remove items,
    as well as calculate the total price of the cart.

    """
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def get_total_price(self):
        return sum([item.total_price for item in self.items])


class Checkout(ABC):
    """

    Checkout class: This class will represent the checkout process.
    It will have a method to process the payment for the items in the cart and complete the transaction.

    """
    @abstractmethod
    def process_payment(self, total_price):
        pass


class CreditCardCheckout(Checkout):
    def __init__(self, credit_card_number, expiration_date):
        self.credit_card_number = credit_card_number
        self.expiration_date = expiration_date

    def process_payment(self, total_price):
        print(f"Processing credit card payment of {total_price} with credit card number {self.credit_card_number} and expiration date {self.expiration_date}")



apple = Product("Apple", 0.5, 10)
banana = Product("Banana", 0.3, 15)
orange = Product("Orange", 0.4, 12)

print()
cart = ShoppingCart()
cart.add_item(CartItem(apple, 2))
cart.add_item(CartItem(banana, 3))
cart.add_item(CartItem(orange, 1))
print()

print(f"Total price: {cart.get_total_price()}")

print()
checkout = CreditCardCheckout("1234-5678-9012-3456", "12/22")
checkout.process_payment(cart.get_total_price())
