from . import Rule
from .variable import Variable, Declaration
from .scope import Scope
import regex

class Function(Rule):

    class Arguments(Rule):

        COMMA = regex.compile(r",")

        PATTERN = [
            (Variable, COMMA, Function.Arguments),
            (Variable)
        ]

        def __init__(self, string):
            super().__init__(string)
            if self.pattern_choice == 1:
                self.variables = [self.match]
            else:
                self.variables = self.match[Function.Arguments] + [self.match[Variable]]

    OPEN_PAREN = regex.compile(r"(")
    CLOSE_PAREN = regex.compile(r")")

    PATTERN = (Declaration, OPEN_PAREN, Function.Arguments, CLOSE_PAREN, Scope)

    def __init__(self, string):
        super().__init__(string)
        self.args = self.match[Function.Arguments].variables
        self.declaration = self.match[Declaration]
        self.scope = self.match[Scope]