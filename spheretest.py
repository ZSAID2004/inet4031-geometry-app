import unittest
import sphere
import math

class sphereTest(unittest.TestCase):

    def test_volume1(self):
        # radius = 1 → (4/3)π(1³) = 4.18879...
        expected = (4/3) * math.pi * (1 ** 3)
        self.assertAlmostEqual(sphere.volume(1), expected)

    def test_volume2(self):
        # radius = 2 → (4/3)π(8) = 33.510...
        expected = (4/3) * math.pi * (2 ** 3)
        self.assertAlmostEqual(sphere.volume(2), expected)

    def test_volume3(self):
        # radius = 5 → (4/3)π(125) = 523.598...
        expected = (4/3) * math.pi * (5 ** 3)
        self.assertAlmostEqual(sphere.volume(5), expected)

if __name__ == '__main__':
    unittest.main()
