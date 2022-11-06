from config import Config


class Car:
    def __init__(self, position: int, velocity: int = 0, params=None):
        if params is None:
            params = {}
        self.position = position
        self.velocity = velocity
        self.road_size = params["road_size"] if "road_size" in params else None

    def accelerate(self, road_size):
        self.velocity += 1
        self._move(road_size)
        return self

    def brake(self):
        self.velocity = 0
        return self

    def random_slowdown(self):
        self.brake()
        return self

    def _move(self, rs):
        self.position += self.velocity
        if self.position >= rs:
            self.position -= rs
        elif self.position < 0:
            self.position += rs
