"""
This python file implements a decorator pattern.
"""

from abc import ABC, abstractmethod


class Cake(ABC):
    """
    Base class for the Cake object.
    """

    def __init__(self, description):
        """
        Initializes the description of a cake.
        """
        self._description = description if description else "Unknown Cake"

    def get_description(self):
        """
        Prints the description of the cake.
        """
        return f"The cake's description is as follows {self._description}"

    @abstractmethod
    def cost(self):
        """
        Determines the cost of the Cake.
        """


class EggLessCake(Cake):
    """
    Implements a Eggless cake (Vegetarian? probably vegan?).
    """

    def cost(self):
        return 200


class CakeWithEgg(Cake):
    """
    Implements a Cake with egg.
    """

    def cost(self):
        return 150


class Cream(Cake):
    """
    Base class for cream to be used.
    """

    def __init__(self, cake: Cake):
        """
        Initializes the Cake type to be used.
        """
        self._cake = cake

    @abstractmethod
    def get_description(self):
        """
        Updates the description of the cake.
        """

    @abstractmethod
    def cost(self):
        """
        Returns the cost of the cake.
        """


class Vanilla(Cream):
    """
    Base class for cream to be used.
    """

    def get_description(self):
        """
        Updates the description of the cake.
        """
        return f"{self._cake.get_description()}, wrapped by vanilla cream."

    def cost(self):
        """
        Returns the cost of the cake.
        """
        return self._cake.cost() + 50


class Chocolate(Cream):
    """
    Base class for cream to be used.
    """

    def get_description(self):
        """
        Updates the description of the cake.
        """
        return f"{self._cake.get_description()}, wrapped by chocolate cream."

    def cost(self):
        """
        Returns the cost of the cake.
        """
        return self._cake.cost() + 75


if __name__ == "__main__":
    Eggless = EggLessCake(description="Cake without Egg")
    print(Eggless.get_description())
    NormalCake = EggLessCake(description="Cake with Egg")
    print(NormalCake.get_description())

    VanillaCream = Vanilla(cake=Eggless)
    print(VanillaCream.get_description())
    print(VanillaCream.cost())

    ChocolateCream = Chocolate(cake=NormalCake)
    print(ChocolateCream.get_description())
    print(ChocolateCream.cost())

    ChocoVanilla = Chocolate(cake=VanillaCream)
    print(ChocoVanilla.get_description())
    print(ChocoVanilla.cost())
