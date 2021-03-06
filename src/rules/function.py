from . import Rule
from .variable import Variable, Declaration
from .scope import Scope
import regex

class Arguments(Rule):

    COMMA = regex.compile(r",")

    def __init__(self, string):
        self.PATTERN = [
            (Variable, self.COMMA, Arguments),
            (Variable)
        ]
        super().__init__(string)
        if self.pattern_choice == 1:
            self.variables = [self.match]
        else:
            self.variables = [self.match[Variable]] + self.match[Arguments].variables

class Function(Rule):

    OPEN_PAREN = regex.compile(r"\(")
    CLOSE_PAREN = regex.compile(r"\)")
    SEMICOLON = regex.compile(r";")

    PATTERN = [
        (Declaration, OPEN_PAREN, Arguments, CLOSE_PAREN, Scope),
        (Declaration, OPEN_PAREN, Arguments, CLOSE_PAREN, SEMICOLON),
        (Declaration, OPEN_PAREN, CLOSE_PAREN, Scope),
        (Declaration, OPEN_PAREN, CLOSE_PAREN, SEMICOLON)
    ]

    def __init__(self, string):
        super().__init__(string)
        try:
            self.args = self.match[Arguments].variables
        except KeyError:
            self.arg = []
        self.declaration = self.match[Declaration]
        try:
            self.scope = self.match[Scope]
        except KeyError:
            self.scope = None