"""
This python file represents the observer patterns
"""

# Basic concept of Observer pattern
# Consist of a subject which has ever changing state and,
# a list of observers which are supposed to get data from the subject.

from abc import ABC, abstractmethod


class Observer(ABC):
    """
    Base class for the observer in the Observer pattern.
    """

    @abstractmethod
    def update(self):
        """
        Responsible for updating the states.
        """


class Subject(ABC):
    """
    Base class for the subject in the Observer pattern.
    """

    @abstractmethod
    def registerObserver(self, observer: Observer):
        """
        Adds an observer to the list of the observers.
        """

    @abstractmethod
    def removeObserver(self, observer: Observer):
        """
        Removes an observer to the list of the observers.
        """

    @abstractmethod
    def notifyObservers(self):
        """
        Notifies the list of observers.
        """


# Lets try to implement a newsletter magazine, which is delivered to multiple users.


class Newsletter(Subject):
    """
    Sends update on any new discoveries of something.
    """

    def __init__(self, observer: list[Observer] = None):
        """
        Initializes the Newsletter with a default observers.
        """
        self._observers = observer if observer else []

    def registerObserver(self, observer: Observer):
        """
        Add a member to the newsletter.
        """
        self._observers.append(observer)
        print(f"{observer} has been added to the Newsletter.")

    def removeObserver(self, observer: Observer):
        """
        Remove a member to the newsletter.
        """
        self._observers.remove(observer)
        print(f"{observer} has been removed from the Newsletter.")

    def notifyObservers(self):
        """
        Notify all the observers about the update.
        """
        for observer in self._observers:
            observer.update()


class Subscriber(Observer):
    """
    Implements a Sbscriber to the Newsletter.
    """

    def update(self):
        """
        Implements the buisness logic to do on the update.
        """
        print("Newsletter has been updated, please check it.")


if __name__ == "__main__":
    Python = Newsletter()
    Subscriber1 = Subscriber()
    Subscriber2 = Subscriber()
    Subscriber3 = Subscriber()

    for subscriber in [Subscriber1, Subscriber2, Subscriber3]:
        Python.registerObserver(observer=subscriber)

    Python.notifyObservers()

    Python.removeObserver(Subscriber1)

    Python.notifyObservers()


# Follows one-to-many relationship
# Example for this weather reports that is displayed across various platforms
# Web-Socket concept?
# Loose coupling
# Accepts any type of Observer that implements the Observer Interface
# Ability to change this at runtime
