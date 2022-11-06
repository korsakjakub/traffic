import unittest

from road import Road


class MyTestCase(unittest.TestCase):
    def test_pbc(self):
        road = Road([0, 1, 2])
        self.assertEqual(road[0], road[3])
        self.assertEqual(road[1], road[4])
        self.assertEqual(road[2], road[-1])
        self.assertEqual(road[5], 2)
        self.assertEqual(road[-3], 0)


if __name__ == '__main__':
    unittest.main()
