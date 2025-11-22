"""CP1404/CP5632 Practical - SilverServiceTaxi tests"""
from prac_09.SilverServiceTaxi import SilverServiceTaxi


def main():
    taxi = SilverServiceTaxi("Fancy Cab", fuel=100, fanciness=2)

    # Start fare and drive 18 km
    taxi.start_fare()
    taxi.drive(18)

    # Expected fare: (1.23 * 2) * 18 + 4.50 = 48.78
    expected_fare = 48.78
    actual_fare = taxi.get_fare()

    print(taxi)
    print(f"Fare: ${actual_fare:.2f}")
    assert abs(actual_fare - expected_fare) < 0.01, f"Expected ${expected_fare}, got ${actual_fare:.2f}"


if __name__ == "__main__":
    main()
