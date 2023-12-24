"""
Implements Simple Factory.
"""

from abc import ABC, abstractmethod


class ElectronicFactory(ABC):
    """
    Implements a Abstract Factory class.
    """

    @abstractmethod
    def handle_chip(self):
        """
        Logic to select an chip.
        """

    @abstractmethod
    def handle_processor(self):
        """
        Logic to select an processor.
        """

    @abstractmethod
    def handle_display(self):
        """
        Logic to select an display.
        """


class IndianElectronicFactory(ElectronicFactory):
    """
    Implements an IndianElectronicFactory.
    """

    def handle_display(self):
        """
        Returns an Indian display.
        """
        print("Display made in India.")

    def handle_chip(self):
        """
        Returns an Indian chip.
        """
        print("Chip made in India.")

    def handle_processor(self):
        """
        Returns an Indian processor.
        """
        print("Processor made in India.")


class USElectronicFactory(ElectronicFactory):
    """
    Implements an USElectronicFactory.
    """

    def handle_display(self):
        """
        Returns an US display.
        """
        print("Display made in US.")

    def handle_chip(self):
        """
        Returns an US chip.
        """
        print("Chip made in US.")

    def handle_processor(self):
        """
        Returns an US processor.
        """
        print("Processor made in US.")


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


class IndianElectronicStore(ElectornicStore):
    """
    Implements Indian electronics.
    """

    def handle(self, value):
        """
        Logic to select an electronic device.
        """
        if value == "Laptop":
            electronic_device = Laptop(factory=IndianElectronicFactory())
        elif value == "MacBook":
            electronic_device = MacBook(factory=IndianElectronicFactory())
        elif value == "SmartPhone":
            electronic_device = SmartPhone(factory=IndianElectronicFactory())

        return electronic_device


class USElectronicStore(ElectornicStore):
    """
    Implements US electronics.
    """

    def handle(self, value):
        """
        Logic to select an electronic device.
        """
        if value == "Laptop":
            electronic_device = Laptop(factory=USElectronicFactory())
        elif value == "MacBook":
            electronic_device = MacBook(factory=USElectronicFactory())
        elif value == "SmartPhone":
            electronic_device = SmartPhone(factory=USElectronicFactory())

        return electronic_device


class Electronic(ABC):
    """
    Implements a bad instantiation.
    """

    def __init__(self, factory: ElectronicFactory):
        """
        Initializes an IndianElectricStore.
        """
        self._factory = factory

    @abstractmethod
    def display(self):
        """
        Initializes a display method.
        """

    @abstractmethod
    def chip(self):
        """
        Initializes a chip method.
        """

    @abstractmethod
    def processor(self):
        """
        Initializes a processor method.
        """


class Laptop(Electronic):
    """
    Implement a Laptop object.
    """

    def display(self):
        """
        Initializes a display method.
        """
        self._factory.handle_display()

    def chip(self):
        """
        Initializes a chip method.
        """
        self._factory.handle_chip()

    def processor(self):
        """
        Initializes a processor method.
        """
        self._factory.handle_processor()


class MacBook(Electronic):
    """
    Implement a MacBook object.
    """

    def display(self):
        """
        Initializes a display method.
        """
        self._factory.handle_display()

    def chip(self):
        """
        Initializes a chip method.
        """
        self._factory.handle_chip()

    def processor(self):
        """
        Initializes a processor method.
        """
        self._factory.handle_processor()


class SmartPhone(Electronic):
    """
    Implement a SmartPhone object.
    """

    def display(self):
        """
        Initializes a display method.
        """
        self._factory.handle_display()

    def chip(self):
        """
        Initializes a chip method.
        """
        self._factory.handle_chip()

    def processor(self):
        """
        Initializes a processor method.
        """
        self._factory.handle_processor()


if __name__ == "__main__":
    # Assume we're giving a input
    inp = "Laptop"
    store = IndianElectronicStore()
    store.select(inp)
