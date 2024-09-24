#!/usr/bin/env python3
from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    def sound(self):
        super().sound()  # Appelle la méthode 'sound' du parent
        return "Bark"


class Cat(Animal):
    def sound(slef):
        super().sound()  # Appelle la méthode 'sound' du parent
        return "Meow"
