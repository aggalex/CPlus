import unittest
from src.rules.declaration.type import Type
from src.rules.declaration import Declaration
from src.rules import MatchError

class TestDeclaration(unittest.TestCase):

    def test_type_identifier(self):
        typenames = [
            "int i",
            "char c",
            "Object some_object",
            "ObjectWithVeryLongName and_a_really_long_identifier",
            "Point rightmost"
        ]

        declarations = {name: Declaration(name) for name in typenames}

        for t in declarations.keys():
            declaration = declarations[t]
            self.assertEqual(declaration.type.type, Type.Type.NAMED)
            self.assertEqual(declaration.type.pattern_choice, 2)
            self.assertEqual(declaration.type.name, t.split(" ")[0])
            self.assertEqual(declaration.name, t.split(" ")[1])

    def test_struct(self):
        struct = Declaration(r"""
        
        struct point {
            int x;
            int y;
        } point_x

        """)

        self.assertEqual(struct.type.type, Type.Type.STRUCT)
        self.assertEqual(struct.type.name, "point")
        self.assertEqual(struct.type.pattern_choice, 0)
        self.assertEqual(struct.type.contents.match.group(), r"""{
            int x;
            int y;
        }""")
        self.assertEqual(struct.name, "point_x")
    
    def test_struct_unamed(self):
        struct = Declaration(r"""
        
        struct {
            int x;
            int y;
        } unnamed_point

        """)

        self.assertEqual(struct.type.type, Type.Type.STRUCT)
        self.assertEqual(struct.type.name, None)
        self.assertEqual(struct.type.pattern_choice, 1)
        self.assertEqual(struct.type.contents.match.group(), r"""{
            int x;
            int y;
        }""")
        self.assertEqual(struct.name, "unnamed_point")
