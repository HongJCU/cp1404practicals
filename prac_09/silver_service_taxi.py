"""CP1404/CP5632 Practical - silver_service_taxi class"""
from prac_09.taxi import Taxi

class SilverServiceTaxi(Taxi):
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        """Initialise a silver_service_taxi with scaled price per km."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = Taxi.price_per_km * fanciness  # scale base price

    def get_fare(self):
        """Calculate fare including flagfall."""
        return super().get_fare() + self.flagfall

    def __str__(self):
        """Return string representation including flagfall."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"
