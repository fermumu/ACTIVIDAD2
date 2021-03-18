"""
OPEN/CLOSE PINCIPLE
“Debera ser capaz de extender el comportamiento de una clase, sin modificarla”

Ejemplo:

Supongamos que el dueño de una tienda le hace un descuento del 20% a sus clientes favoritos y un descuento del
doble del 20% a clientes VIP.modificamos la clase asi:
"""


class Discount:
    def __init__(self, customer, price):
        self.customer = customer
        self.price = price

    def get_discount(self):
            return self.price * 0.2


class VIPDiscount(Discount):
    def get_discount(self):
        return super().get_discount() * 2

"""
If you decide 80% discount to super VIP customers, it should be like this:
You see, extension without modification.
"""

class SuperVIPDiscount(VIPDiscount):
    def get_discount(self):
        return super().get_discount() * 2