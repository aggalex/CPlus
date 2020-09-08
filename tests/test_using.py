import unittest
from src.rules.using import Using, NamespacedIdentifier
from src.rules import MatchError

class TestIdentifier(unittest.TestCase):

    def test_using(self):
        names = [
            "std::list",
            "is::this::really::a::NameSpace",
            "this::though::is::a::namespace",
            "in::a::namespace::far::far::away::there::was::an::ObjectWithVeryLongName",
            "std::math::Point"
        ]

        namespaces = [NamespacedIdentifier(ns) for ns in names]
        to_match = [ns.identifiers for ns in namespaces]
        using_namespaces = [Using(f"using {ns};") for ns in names]
        found = [using.namespace.identifiers for using in using_namespaces]

        self.assertEqual(to_match, found)