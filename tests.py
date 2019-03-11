import unittest

from foo import bar


class TestStringMethods(unittest.TestCase):

    def test_bar(self):
        self.assertEqual(bar(), 1)
