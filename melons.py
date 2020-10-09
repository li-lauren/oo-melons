from random import randint
from datetime import date, time, datetime

# _____________________________________________

class AbstractMelonOrder():
    """An abstract base class that other Melon Orders inherit from."""
    def __init__(self, species, qty, country_code = "USA"):
        self.species = species
        self.qty = qty
        self.country_code = country_code
        self.shipped = False  

    def get_base_price(self):
        """calculate base proce accoutring to random num 5-9"""
        weekday = date.today().weekday()
        hour = datetime.now().hour
        
        base_price = randint(5,9)
        print(base_price)
        if weekday < 5 and (hour in range(8, 11)):
            return base_price + 4

        return base_price

    def get_total(self):
        """Calculate price, including tax."""
        org_base_price = self.get_base_price()
        base_price = org_base_price * 1.5 if self.species == "christmas" else org_base_price
        total = (1 + self.tax) * self.qty * base_price

        return total
    
    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True

class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""
    tax = 0.08
    order_type = "domestic"

class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""
    tax = 0.17
    order_type = "international"

    def get_total(self):
        if self.qty < 10:
            total = super().get_total() + 3
        else:
            total = super().get_total()
        return total

class GovernmentMelonOrder(AbstractMelonOrder):
    """For government melon orders."""
    tax = 0
    passed_inspection = False

    def mark_inspection(self, passed):
        self.passed_inspection = passed






