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
        self.assertEqual(struct.contents.match.group(), r"""{
            int x;
            int y;
        }""")
    
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
        self.assertEqual(struct.contents.match.group(), r"""{
            int x;
            int y;
        }""")
