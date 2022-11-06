import unittest
from time_space_plotter import fix_pbc_artifacts


class TestPlotter(unittest.TestCase):
    def test_fix_pbc_artifacts(self):
        data = [
            [[0, 1, 2, 3, 0], [1, 2, 2, 2, 4, 2, 3]],
            [[0, 1, 1, 2, 2, 4, 4, 0, 0, 1, 1, 2, 2, 4, 4]]
        ]

        got = [fix_pbc_artifacts(data[i]) for i in range(len(data))]
        want = [
            [[0, 1, 2, 3], [0, 0, 0, 0, 0], [1, 2, 2, 2, 4], [0, 0, 0, 0, 0, 2, 3]],
            [[0, 1, 1, 2, 2, 4, 4], [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 2, 2, 4, 4]]
        ]
        [self.assertEqual(len(want[i]), len(got[i])) for i in range(len(want))]
        for j in range(len(want)):
            for i in range(len(want[j])):
                self.assertListEqual(got[j][i], want[j][i])


if __name__ == '__main__':
    unittest.main()
