"""
Implements bad implementations of factory patterns.
"""

# Bad Program
from abc import ABC, abstractmethod


class ElectornicStore:
    """
    Implements a store.
    """

    def select(self, value):
        """
        Create an Electronic device (assumption).
        """
        if value == "Laptop":
            electronic_device = Laptop()
        elif value == "MacBook":
            electronic_device = MacBook()
        elif value == "SmartPhone":
            electronic_device = SmartPhone()
        
        electronic_device.display()


class BadElectronic(ABC):
    """
    Implements a bad instantiation.
    """

    @abstractmethod
    def display(self):
        """
        Abstract method for the display behaviour.
        """


class Laptop(BadElectronic):
    """
    Implement a Laptop object.
    """

    def display(self):
        """
        Implements the display behaviour.
        """
        print("Display behaviour of a Laptop.")


class MacBook(BadElectronic):
    """
    Implement a MacBook object.
    """

    def display(self):
        """
        Implements the display behaviour.
        """
        print("Display behaviour of a MacBook.")


class SmartPhone(BadElectronic):
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
    store = ElectornicStore().select(inp)


# if we're sopposed to add or remove electronics, then we're forces
# to modify the select() method in the Electronic store, which violates the
# Open or Closed Principle.
