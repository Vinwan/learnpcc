from random import randint

class Die():
    """docstring for Die."""
    def __init__(self, num_sides=6):
        # default 6 sides for die
        self.num_sides = num_sides

    def roll(self):
        """return between 1 and die sides numbers"""
        return randint(1, self.num_sides)
