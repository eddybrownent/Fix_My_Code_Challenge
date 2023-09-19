#!/usr/bin/python3
"""
This script has a model Square
"""


class Square():
    """
    class defining a Square
    """

    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """
        the constructor
        """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.height

    def permiter_of_my_square(self):
        """ Perimeter of the square """
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """
        returns a string rep of the square
        """
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":

    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.permiter_of_my_square())
