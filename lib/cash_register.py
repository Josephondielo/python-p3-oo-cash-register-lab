#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.total = 0
        self.discount = discount
        self.items = []
        self.last_transaction = 0
        self._last_item_count = 0

    def add_item(self, title, price, quantity=1):
        qty = int(quantity)
        amount = price * qty
        self.total += amount
        self.last_transaction = amount
        self._last_item_count = qty

        for _ in range(qty):
            self.items.append(title)

    def apply_discount(self):
        if self.discount:
           
            self.total = int(self.total * (100 - self.discount) / 100)
            print(f"After the discount, the total comes to ${self.total}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        self.total -= self.last_transaction
        for _ in range(self._last_item_count):
            if self.items:
                self.items.pop()
        self.last_transaction = 0
        self._last_item_count = 0
