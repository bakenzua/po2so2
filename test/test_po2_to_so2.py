from unittest import TestCase
import numpy as np
from po2so2 import thomas_po2_to_so2

class TestPo2ToSo2(TestCase):

    def test_scalar_calculation(self):
        po2 = 5.653266
        self.assertEqual(thomas_po2_to_so2(po2, kpa=False), 0.010272119260622511)
        po2 = 125.0
        self.assertEqual(thomas_po2_to_so2(po2, kpa=False), 0.98428832449680714)

    def test_numpy_array_calculation(self):
        po2s = np.array([1.884422, 2.512563, 3.140704, 3.768844])
        self.assertEqual(thomas_po2_to_so2(po2s).size, 4)
