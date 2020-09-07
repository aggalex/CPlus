from ..variable import Variable
from ..scope.scope_contents import ScopeContents, Rule
import regex

class StructContents(ScopeContents):

    class Member(Rule):

        SEMICOLON = regex.compile(r";")
        PATTERN = (Variable, SEMICOLON)

        def __init__(self, string):
            super().__init__(string)
            self.variable = self.match[Variable]

    CONTENT = Member

    def __init__(self, string):
        super().__init__(string)
        self.members = [p.variable for p in self.patterns]