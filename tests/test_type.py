import unittest
from src.rules.declaration.type import Type
from src.rules import MatchError

class TestScope(unittest.TestCase):

    def test_identifier(self):
        typenames = [
            "int",
            "char",
            "Object",
            "ObjectWithVeryLongName",
            "Point"
        ]

        types = {name: Type(name) for name in typenames}

        for t in types.keys():
            self.assertEqual(types[t].type, Type.Type.NAMED)
            self.assertEqual(types[t].pattern_choice, 2)
            self.assertEqual(types[t].name, t)


    def test_struct_named(self):
        struct = Type(r"""
        
        struct point {
            int x;
            int y;
        }

        """)

        self.assertEqual(struct.type, Type.Type.STRUCT)
        self.assertEqual(struct.name, "point")
        self.assertEqual(struct.pattern_choice, 0)
        self.assertEqual(struct.scope.match.group(), r"""{
            int x;
            int y;
        }""")

        members = [
            ("int", "x"),
            ("int", "y")
        ]
        for i in range(len(struct.contents.members)):
            found = struct.contents.members[i]
            to_match = members[i]
            self.assertEqual(found.declaration.name, to_match[1])
            self.assertEqual(found.declaration.type.name, to_match[0])

    def test_struct_unamed(self):
        struct = Type(r"""
        
        struct {
            int x;
            int y;
        }

        """)

        self.assertEqual(struct.type, Type.Type.STRUCT)
        self.assertEqual(struct.name, None)
        self.assertEqual(struct.pattern_choice, 1)
        self.assertEqual(struct.scope.match.group(), r"""{
            int x;
            int y;
        }""")
