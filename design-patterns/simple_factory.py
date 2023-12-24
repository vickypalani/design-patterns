"""
Implements Simple Factory.
"""

from abc import ABC, abstractmethod


class ElectronicFactory:
    """
    Implements a simple factory method.
    """

    def handle(self, value):
        """
        Logic to select an electronic device.
        """
        if value == "Laptop":
            electronic_device = Laptop()
        elif value == "MacBook":
            electronic_device = MacBook()
        elif value == "SmartPhone":
            electronic_device = SmartPhone()

        return electronic_device


class ElectornicStore:
    """
    Implements a store.
    """

    def __init__(self, factory: ElectronicFactory):
        self._factory = factory

    def select(self, value):
        """
        Create an Electronic device (assumption).
        """
        electronic_device = self._factory.handle(value)

        electronic_device.display()


class Electronic(ABC):
    """
    Implements a bad instantiation.
    """

    @abstractmethod
    def display(self):
        """
        Abstract method for the display behaviour.
        """


class Laptop(Electronic):
    """
    Implement a Laptop object.
    """

    def display(self):
        """
        Implements the display behaviour.
        """
        print("Display behaviour of a Laptop.")


class MacBook(Electronic):
    """
    Implement a MacBook object.
    """

    def display(self):
        """
        Implements the display behaviour.
        """
        print("Display behaviour of a MacBook.")


class SmartPhone(Electronic):
    """
    Implement a SmartPhone object.
    """

    def display(self):
        """
        Implements the display behaviour.
        """
        print("Display behaviour of a SmartPhone.")


if __name__ == "__main__":
    # Assume we're giving a input
    inp = "Laptop"
    # inp = "MacBook"
    # inp = "SmartPhone"
    store = ElectornicStore(factory=ElectronicFactory())
    store.select(inp)


# Now even if we want to modify or add or remove the electronics,
# the factory is the only place it is modified and also,
# now select is now unaware of the electronic device choosen, does this is loosely coupled.

# The object creation is encapsulated
