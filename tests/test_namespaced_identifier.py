import unittest
from src.rules.namespaced_identifier import NamespacedIdentifier
from src.rules import MatchError

class TestIdentifier(unittest.TestCase):

    def test_identifier(self):
        self.assertEqual(NamespacedIdentifier("_asda_sd234").identifiers[0].match.group(), "_asda_sd234")
        self.assertEqual(NamespacedIdentifier("ASdaSdA345345SDSS").identifiers[0].match.group(), "ASdaSdA345345SDSS")
        self.assertEqual(NamespacedIdentifier("point").identifiers[0].match.group(), "point")
        with self.assertRaises(MatchError):
            NamespacedIdentifier("234asd")
        with self.assertRaises(MatchError):
            NamespacedIdentifier("*()*****")

    def test_namespaced_identifier(self):
        def match(names_str, names_lst):
            found_lst = [ident.match.group() for ident in NamespacedIdentifier(names_str).identifiers]
            self.assertEqual(found_lst, names_lst)
        match("list::add", ["list", "add"])
        match("very::long::namespace::nesting::nearly::there::function1", [
            "very",
            "long",
            "namespace",
            "nesting",
            "nearly",
            "there",
            "function1"
        ])
        match("collections::hash_map::new", ["collections", "hash_map", "new"])