import unittest
from src.rules.include import Include
from src.rules import MatchError

class TestInclude(unittest.TestCase):

    def test_relative(self):
        paths = [
            r"list.hp",
            r"server_module.hp",
            r"includes\module.hp",
            r"..\includes\asd.hp"
        ]

        found = [Include(f'#include "{path}"') for path in paths]
        self.assertEqual(paths, [include.path for include in found])
        
        for include in found:
            self.assertEqual(include.is_relative, True)
    
    def test_absolute(self):
        paths = [
            r"stdio.hp",
            r"stdlib.hp",
            r"sys\thread.hp"
        ]

        found = [Include(f'#include <{path}>') for path in paths]
        self.assertEqual(paths, [include.path for include in found])
        
        for include in found:
            self.assertEqual(include.is_relative, False)