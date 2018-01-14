from unittest import TestCase
import numpy as np
from severinghaus_o2 import so2_to_po2

class TestSo2ToPo2(TestCase):

    def test_scalar_calculation(self):
        so2 = 0.009699
        self.assertEqual(so2_to_po2(so2), 0.14837913835623656)
        so2 = 0.906809
        self.assertEqual(so2_to_po2(so2), 7.9486957270191949)

    def test_numpy_array_calculation(self):
        so2s = np.array([0.009699, 0.906809])
        self.assertEqual(so2_to_po2(so2s).size, 2)
