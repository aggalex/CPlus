import unittest

from src.rules.scope import Scope

class TestScope(unittest.TestCase):

    def test_empty(self):
        Scope(r"""
        {}{{{}}{}}
        """)
    
    def test_get_subscopes(self):
        scope = Scope(r"""
        {{{}}{}}
        """)
        scopes_found = scope.get_subscopes()
        self.assertEqual(scopes_found[0]["scope"].match.group(), r"{{}}")
        self.assertEqual(scopes_found[0]["sub"][0]["scope"].match.group(), r"{}")
        self.assertEqual(scopes_found[1]["scope"].match.group(), r"{}")
        self.assertEqual(scopes_found[0]["sub"][0]["sub"], ())
        self.assertEqual(scopes_found[1]["sub"], ())
        with self.assertRaises(IndexError):
            scopes_found[2]
        with self.assertRaises(IndexError):
            scopes_found[0]["sub"][1]

