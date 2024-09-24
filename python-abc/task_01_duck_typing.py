#!/usr/bin/env python3
from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    pi = 3.14159265358979323846264338327950288419716939937510582
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.pi * (self.radius * self.radius)

    def perimeter(self):
        return (2 * self.radius) * self.pi

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return (self.width + self.height) * 2

def shape_info(Shape):
    print("Area : {}".format(Shape.area()))
    print("Perimeter : {}".format(Shape.perimeter()))
