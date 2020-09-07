import unittest
from src.rules.declaration.type import Type
from src.rules.declaration.struct_contents import StructContents, Variable
from src.rules import MatchError

class TestStructContents(unittest.TestCase):

    def test_init(self):
        contents = StructContents(r"""
        
            int x;
            int y;
            char x;
            struct {
                int x;
                int y;
            } point;

        """)

        members = [
            "int x",
            "int y",
            "char x",
            """struct {
                int x;
                int y;
            } point"""
        ]

        for i in range(len(contents.members)):
            found = contents.members[i]
            to_match = Variable(members[i])
            self.assertEqual(found.declaration.name, to_match.declaration.name)
            self.assertEqual(found.declaration.type.name, to_match.declaration.type.name)
            self.assertEqual(found.declaration.type.type, to_match.declaration.type.type)
            self.assertEqual(found.declaration.pointer_depth, to_match.declaration.pointer_depth)

