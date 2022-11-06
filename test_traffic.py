import unittest

from car import Car
from road import Road
from traffic import Traffic


class MyTestCase(unittest.TestCase):
    def test_get_initial_traffic(self):
        traffic = Traffic()
        traffic.get_initial_traffic(10)
        self.assertEqual(len(traffic.road), 10)
        for car in traffic.road:
            self.assertIsNotNone(car.position)
            self.assertIsNotNone(car.velocity)
            self.assertEqual(type(car.position), int)
            self.assertEqual(type(car.velocity), int)

    def test_evaluate_distances(self):
        traffic_instances = [
            Traffic(params={"road_size": 3, "road": Road([Car(position=0), Car(position=2)])}),
            Traffic(params={"road_size": 10, "road": Road([Car(position=i) for i in range(10)])}),
            Traffic(params={"road_size": 10, "road": Road([Car(position=4), Car(position=5)])})
        ]
        got = [traffic.evaluate_distances() for traffic in traffic_instances]
        want = [[1, 0], [0 for _ in range(10)], [0, 8]]
        self.assertEqual(len(got), len(want))
        for i in range(len(want)):
            self.assertListEqual(want[i], got[i])

    def test_move_cars(self):
        tr = [
            Traffic(params={"road_size": 10, "road": Road([Car(position=i) for i in range(10)])}),
            Traffic(params={"road_size": 10, "road": Road([Car(position=4), Car(position=5)])}),
            Traffic(params={"road_size": 3, "road": Road([Car(position=0), Car(position=2)])})
        ]
        got = [traffic.move_cars().get_cars_positions() for traffic in tr]
        want = [[i for i in range(10)], [4, 6], [1, 2]]
        self.assertEqual(len(got), len(want))
        for i in range(len(want)):
            self.assertListEqual(want[i], got[i])


if __name__ == '__main__':
    unittest.main()
