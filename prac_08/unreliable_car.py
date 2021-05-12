from random import randint
from prac_08.car import Car

class Unreliable(Car):

    def __init__(self, name, fuel, reliability):
        """Initialise an UnreliableCar."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drives(self,distance):
        radon = randint(1,100)
        if radon>= self.reliability:
            distance = 0
        distancedrive = distance
        return distancedrive