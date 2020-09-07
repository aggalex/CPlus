from . import Rule
from .declaration import Declaration
import regex

class Variable(Rule):

    ARRAY_INDICES = regex.compile(r"(\s*\[\s*[0-9]*\s*\])*")
    EVALUATION = regex.compile(r'=\s*([^;"]|"((\\")|[^"])*")*')

    PATTERN = [
        (Declaration, ARRAY_INDICES),
        (Declaration, ARRAY_INDICES, EVALUATION)
    ]

    def __init__(self, string):
        super().__init__(string)

        self.declaration = self.match[Declaration]
        self.declaration.pointer_depth += self.match[self.ARRAY_INDICES].group().count("[")
        try:
            self.evaluation = self.match[self.EVALUATION].match.group()
        except KeyError:
            self.evaluation = None
