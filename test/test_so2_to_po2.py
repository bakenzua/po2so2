from unittest import TestCase
import numpy as np
from po2so2 import severinghaus_so2_to_po2

class TestSo2ToPo2(TestCase):

    def test_scalar_calculation(self):
        so2 = 0.009699
        self.assertEqual(severinghaus_so2_to_po2(so2), 0.14837956952516507)
        so2 = 0.906809
        self.assertEqual(severinghaus_so2_to_po2(so2), 7.9487188248121701)

    def test_numpy_array_calculation(self):
        so2s = np.array([0.009699, 0.906809])
        self.assertEqual(severinghaus_so2_to_po2(so2s).size, 2)
