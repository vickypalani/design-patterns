"""
Implements Simple Factory.
"""

from abc import ABC, abstractmethod


# Now assume that there are multiple Electronic stores,
# and each has its own display behaviour (variations)
# For example assume IndianElectronicStore and USElectronicStore,
# now we've variations of Laptops like IndianLaptop and USLaptop,
# thus it is better to use Factory pattern over Simple factory


class ElectornicStore:
    """
    Implements a store.
    """

    @abstractmethod
    def handle(self, value):
        """
        Handles the electronic device to be selected.
        """

    def select(self, value):
        """
        Create an Electronic device (assumption).
        """
        electronic_device = self.handle(value)

        electronic_device.display()


class IndianElectricStore(ElectornicStore):
    """
    Implements Indian electronics.
    """

    def handle(self, value):
        """
        Logic to select an electronic device.
        """
        if value == "Laptop":
            electronic_device = IndianLaptop()
        elif value == "MacBook":
            electronic_device = IndianMacBook()
        elif value == "SmartPhone":
            electronic_device = IndianSmartPhone()

        return electronic_device


class USElectricStore(ElectornicStore):
    """
    Implements US electronics.
    """

    def handle(self, value):
        """
        Logic to select an electronic device.
        """
        if value == "Laptop":
            electronic_device = USLaptop()
        elif value == "MacBook":
            electronic_device = USMacBook()
        elif value == "SmartPhone":
            electronic_device = USSmartPhone()

        return electronic_device


class Electronic(ABC):
    """
    Implements a bad instantiation.
    """

    @abstractmethod
    def display(self):
        """
        Abstract method for the display behaviour.
        """


class IndianLaptop(Electronic):
    """
    Implement a IndianLaptop object.
    """

    def display(self):
        """
        Implements the display behaviour.
        """
        print("Display behaviour of a IndianLaptop.")


class IndianMacBook(Electronic):
    """
    Implement a IndianMacBook object.
    """

    def display(self):
        """
        Implements the display behaviour.
        """
        print("Display behaviour of a IndianMacBook.")


class IndianSmartPhone(Electronic):
    """
    Implement a IndianSmartPhone object.
    """

    def display(self):
        """
        Implements the display behaviour.
        """
        print("Display behaviour of a IndianSmartPhone.")


class USLaptop(Electronic):
    """
    Implement a USLaptop object.
    """

    def display(self):
        """
        Implements the display behaviour.
        """
        print("Display behaviour of a USLaptop.")


class USMacBook(Electronic):
    """
    Implement a USMacBook object.
    """

    def display(self):
        """
        Implements the display behaviour.
        """
        print("Display behaviour of a USMacBook.")


class USSmartPhone(Electronic):
    """
    Implement a USSmartPhone object.
    """

    def display(self):
        """
        Implements the display behaviour.
        """
        print("Display behaviour of a USSmartPhone.")


if __name__ == "__main__":
    # Assume we're giving a input
    inp = "Laptop"
    # inp = "MacBook"
    # inp = "SmartPhone"
    store = IndianElectricStore()
    store.select(inp)

    another_store = USElectricStore()
    another_store.select(inp)
