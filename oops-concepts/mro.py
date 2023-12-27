"""
Example of an Method Resolution Order.
"""


class A:
    """
    Just a dummy class
    """

    def print_something(self):
        """
        Just a dummy method.
        """
        print("Inherited from the Class A.")


class B:
    """
    Just a dummy class
    """

    def print_something(self):
        """
        Just a dummy method.
        """
        print("Inherited from the Class B.")


# class C(A, B):
class C(B, A):
    """
    Just a dummy class
    """


class D(C):
    """
    Just a dummy class
    """

    def print_something(self):
        """
        Check about the super()
        """
        return super().print_something()


if __name__ == "__main__":
    classC = C()
    classC.print_something()
    print(C.mro())

    classD = D()
    classD.print_something()
