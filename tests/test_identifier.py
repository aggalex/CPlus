import unittest
from src.rules.identifier import Identifier
from src.rules import MatchError

class TestIdentifier(unittest.TestCase):

    def test_identifier(self):
        self.assertEqual(Identifier("_asda_sd234").match.group(), "_asda_sd234")
        self.assertEqual(Identifier("ASdaSdA345345SDSS").match.group(), "ASdaSdA345345SDSS")
        self.assertEqual(Identifier("point").match.group(), "point")
        with self.assertRaises(MatchError):
            Identifier("234asd")
        with self.assertRaises(MatchError):
            Identifier("*()*****")