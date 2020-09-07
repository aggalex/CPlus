import unittest
from src.rules.declaration.type import Type
from src.rules.variable import Variable
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

        variables = {name: Variable(name) for name in typenames}

        for t in variables.keys():
            variable = variables[t]
            self.assertEqual(variable.declaration.type.type, Type.Type.NAMED)
            self.assertEqual(variable.declaration.type.pattern_choice, 2)
            self.assertEqual(variable.declaration.type.name, t.split(" ")[0])
            self.assertEqual(variable.declaration.name, t.split(" ")[1])
            self.assertEqual(variable.evaluation, None)

    def test_type_identifier_array(self):
        self.assertEqual(Variable("int *run[][]").declaration.pointer_depth, 3)
        self.assertEqual(Variable("char **str[]").declaration.pointer_depth, 3)

    def type_type_identifier_evaluation(self):
        self.assertEqual(Variable('int *run[][] = get_run("tht", "r+")').declaration.pointer_depth, '= get_run("tht", "r+")')
        self.assertEqual(Variable("char *str = malloc(12 * sizeof(char))").evaluation, "= malloc(12 * sizeof(char))")

    def test_struct(self):
        struct = Variable(r"""
        
        struct point {
            int x;
            int y;
        } point_x[]

        """)

        self.assertEqual(struct.declaration.type.type, Type.Type.STRUCT)
        self.assertEqual(struct.declaration.type.name, "point")
        self.assertEqual(struct.declaration.type.pattern_choice, 0)
        self.assertEqual(struct.declaration.type.scope.match.group(), r"""{
            int x;
            int y;
        }""")
        self.assertEqual(struct.declaration.name, "point_x")
        self.assertEqual(struct.declaration.pointer_depth, 1)
        self.assertEqual(struct.evaluation, None)
    
    def test_struct_evaluation(self):
        struct = Variable(r"""
        
        struct {
            int x;
            int y;
        } unnamed_point[][12] = get_points(5, 12)

        """)

        self.assertEqual(struct.declaration.type.type, Type.Type.STRUCT)
        self.assertEqual(struct.declaration.type.name, None)
        self.assertEqual(struct.declaration.type.pattern_choice, 1)
        self.assertEqual(struct.declaration.type.scope.match.group(), r"""{
            int x;
            int y;
        }""")
        self.assertEqual(struct.declaration.name, "unnamed_point")
        self.assertEqual(struct.declaration.pointer_depth, 2)
        # self.assertEqual(struct.evaluation, "= get_points(5, 12)") TODO
