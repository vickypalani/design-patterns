"""
This python file is an introduction to design-patterns, 
and also explains the constraints faced in Inheriatance 
and how to solve it using Composition. 
"""

from abc import ABC, abstractmethod


class FlyBehaviour(ABC):
    """
    Implements the fly behaviour of objects
    """

    @abstractmethod
    def fly(self):
        """
        Responsible for the base fly behaviour
        """


class QuackBehaviour(ABC):
    """
    Implements the quack behaviour of objects
    """

    @abstractmethod
    def quack(self):
        """
        Responsible for the base fly behaviour
        """


class Duck:
    """
    Implements an Duck object in python
    """

    def __init__(self, flyBehaviour: FlyBehaviour, quackBehaviour: QuackBehaviour):
        """
        Initializes a Duck object
        """
        self._flyBehaviour = flyBehaviour
        self._quackBehaviour = quackBehaviour

    def display(self):
        """Implements the display behaviour of Duck"""
        print("This duck is visible, and implemented from the Parent class")

    def swim(self):
        """Implements the swim behaviour of Duck"""
        print("This duck is capable of swimming, and implemented from the Parent class")

    def fly(self):
        """Implements the fly behaviour of Duck"""
        self._flyBehaviour.fly()

    def set_fly(self, value: FlyBehaviour):
        """Modifies the fly behaviour of a duck"""
        self._flyBehaviour = value

    def quack(self):
        """Implements the quack behaviour of Duck"""
        self._quackBehaviour.quack()

    def set_quack(self, value: QuackBehaviour):
        """Modifies the quack behaviour of a duck"""
        self._quackBehaviour = value


# Concrete classes
class FlyWithWings(FlyBehaviour):
    """
    Implements an object that flys with a pair of wings.
    """

    def fly(self):
        """
        Method overriding of the FlyBehaviour's fly method, as needed.
        """
        print("This object has a pair of wings, which is utilized for flying")


class NormalQuack(QuackBehaviour):
    """
    Implements an object with a normal Quack sound.
    """

    def quack(self):
        """
        Method overriding of the QuackBehaviour's quack method, as needed.
        """
        print("This object has a normal quack sound")


class DoesNotFly(FlyBehaviour):
    """
    Implements an object that flys with a pair of wings.
    """

    def fly(self):
        """
        Method overriding of the FlyBehaviour's fly method, as needed.
        """
        print("This object does not fly")


class Squeak(QuackBehaviour):
    """
    Implements an object with a normal Quack sound.
    """

    def quack(self):
        """
        Method overriding of the QuackBehaviour's quack method, as needed.
        """
        print("This object makes a squeak sound, when squezzed")


if __name__ == "__main__":
    NormalDuck = Duck(flyBehaviour=FlyWithWings(), quackBehaviour=NormalQuack())
    RubberDuck = Duck(flyBehaviour=DoesNotFly(), quackBehaviour=Squeak())
    ImaginaryDuck = Duck(flyBehaviour=FlyWithWings(), quackBehaviour=Squeak())

    for _ in (NormalDuck, RubberDuck, ImaginaryDuck):  # Polymorphism example?
        _.display()
        _.swim()
        _.fly()
        _.quack()
        print("*" * 5 + "__end__" + "*" * 5)

    NormalDuck.set_fly(DoesNotFly())  # to check the working of setter
    NormalDuck.fly()

# what have we have done here?
#  We have made an concrete class for the Duck object and,
#  instead of implementing the behaviour of fly and quack in
#  the Parent class like with display and swim, we added interface
#  for those, making it flexible and maintainable


# Improvements:
# 1. We can add a setter for the fly and quack methods.
# that we can modify the duck's fly and quack behaviour as needed.


# Inference:
# Has-A ---> Composition is better than Is-A ---> Inheriatance
