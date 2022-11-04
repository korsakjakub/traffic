from action import Action


class Car:
    def __init__(self, position: int, velocity: int = 0, action: Action = None):
        self.position = position
        self.velocity = velocity
        self.action = action

    def accelerate(self):
        self.velocity += 1
        self._move()
        return self

    def brake(self):
        self.velocity -= 1
        self._move()
        return self

    def random_slowdown(self):
        self.velocity = 0
        return self

    def _move(self):
        self.position += self.velocity
