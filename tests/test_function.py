import unittest
from src.rules.function import Function, Declaration, Variable
from src.rules.declaration.type import Type
from src.rules import MatchError

class TestFunction(unittest.TestCase):

    def test_init(self):
        function = Function("""
        void *alloc(size_t size, int n) {
            return calloc(size, n)
        }
        """)

        self.assertEqual(function.declaration.name, "alloc")
        self.assertEqual(function.declaration.type.name, "void")
        self.assertEqual(function.declaration.pointer_depth, 1)
        
        args = [
            ("size_t", "size"),
            ("int", "n")
        ]

        for i in range(len(function.args)):
            found = function.args[i].declaration
            to_match = args[i]
            self.assertEqual(found.type.name, to_match[0])
            self.assertEqual(found.name, to_match[1])

        self.assertEqual(function.scope.match.group(), """{
            return calloc(size, n)
        }""")