"""
Unit tests for bud_get module.

Usage:
    python -m unittest discover
"""
import unittest
import os
from bud_get import bud_get

IN_DATA = "./tests/data/test_data_0.csv"
OUT_DATA = "./tests/data/test_data_0_out.csv"

class TestBudget(unittest.TestCase):
    """ Budget unit test. """
    @classmethod
    def setUpClass(cls):
        """ Setup operations for this test case. """
        if os.path.isfile(OUT_DATA):
            os.remove(OUT_DATA)

    def test_filter(self):
        """ Filter input data. """
        results = bud_get.filter_csv(IN_DATA)
        self.assertIsNotNone(results)
        self.assertEqual(len(results), 13)

        self.assertEqual(results[0]['Trans Date'], '09/24/2015')
        self.assertEqual(results[1]['Trans Date'], '09/24/2015')
        self.assertEqual(results[2]['Trans Date'], '09/24/2015')
        self.assertEqual(results[3]['Trans Date'], '10/12/2015')
        self.assertEqual(results[len(results) - 1]['Trans Date'], '01/01/2016')

        self.assertEqual(results[0]['Amount'], '4.55')
        self.assertEqual(results[1]['Amount'], '11.81')
        self.assertEqual(results[2]['Amount'], '12.19')
        self.assertEqual(results[3]['Amount'], '4.55')
        self.assertEqual(results[len(results) - 1]['Amount'], '4.00')

    def test_write(self):
        """ Filter and write resulting data. """
        self.assertFalse(os.path.isfile(OUT_DATA))

        results = bud_get.filter_csv(IN_DATA)
        self.assertIsNotNone(results)

        bud_get.write_csv(results, OUT_DATA)
        self.assertTrue(os.path.isfile(OUT_DATA))
