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
            self.assertEqual(declaration.type.pattern_choice, 3)
            self.assertEqual(declaration.type.namespaces, [])
            self.assertEqual(declaration.type.name, t.split(" ")[0])
            self.assertEqual(declaration.name, t.split(" ")[1])

    def test_generics(self):
        declaration = Declaration("List<int> add<int>")
        self.assertEqual(declaration.type.generics[0].name, "int")
        self.assertEqual(declaration.generics[0].name, "int")
        self.assertEqual(len(declaration.type.generics), 1)
        self.assertEqual(len(declaration.generics), 1)

        declaration = Declaration("HashMap<String, List<int>> assign<List<int>>")
        self.assertEqual(declaration.type.generics[0].name, "String")
        self.assertEqual(declaration.type.generics[1].name, "List")
        self.assertEqual(declaration.type.generics[1].generics[0].name, "int")
        self.assertEqual(len(declaration.type.generics[1].generics), 1)
        self.assertEqual(len(declaration.type.generics), 2)
        self.assertEqual(declaration.generics[0].name, "List")
        self.assertEqual(declaration.generics[0].generics[0].name, "int")
        self.assertEqual(len(declaration.type.generics[1].generics), 1)
        self.assertEqual(len(declaration.type.generics), 2)

        declaration = Declaration("Point<G> set")
        self.assertEqual(declaration.type.generics[0].name, "G")
        self.assertEqual(len(declaration.type.generics), 1)
        self.assertEqual(declaration.generics, None)

        declaration = Declaration("G new<G>")
        self.assertEqual(declaration.generics[0].name, "G")
        self.assertEqual(len(declaration.generics), 1)
        self.assertEqual(declaration.type.generics, None)

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
        self.assertEqual(struct.type.scope.match.group(), r"""{
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
        self.assertEqual(struct.type.scope.match.group(), r"""{
            int x;
            int y;
        }""")
        self.assertEqual(struct.name, "unnamed_point")
