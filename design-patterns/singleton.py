"""
Implements an Singleton pattern
"""

from typing import Any


class Singleton:
    """
    Iniatializes a single object
    """

    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance


if __name__ == "__main__":
    s1 = Singleton()
    s2 = Singleton()
    s1.dummy_variable = "Mugiwara"
    print(s2.dummy_variable)
    s3 = Singleton()
    print(s3.dummy_variable)
