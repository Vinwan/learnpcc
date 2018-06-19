from random import choice

class RandomWalk():
    """a new random class"""

    def __init__(self, num_points=5000):
        # init RandomWalk value
        self.num_points = num_points

        # all RandomWalk begin(0, 0)
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):

        # seirel random walk untill the length
        while len(self.x_values) < self.num_points:
            x_step = self.get_step()
            y_step = self.get_step()

            # refuse autochthonous step
            if x_step == 0 and y_step == 0:
                continue

            # next x and y points
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)

    def get_step(self):
        # decision forward direction and distance
        x_direction = choice([1, -1])
        x_distance = choice([0, 1, 2, 3, 4])
        x_step = x_direction * x_distance
        return x_step

        y_direction = choice([1, -1])
        y_distance = choice([0, 1, 2, 3, 4])
        y_step = y_direction * y_distance
        return y_step
