#!/usr/bin/env python3


class Fish:
    def swim(sel):
        print("The fish is swimming")

    def habitat(sel):
        print("The fish lives in water")


class Bird:
    def fly(sel):
        print("The bird is flying")

    def habitat(sel):
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    def fly(self):
        print("The flying fish is soaring!")

    def swim(sel):
        print("The flying fish is swimming!")

    def habitat(sel):
        print("The flying fish lives both in water and the sky!")
