from ..scope.scope_contents import ScopeContents, Rule
from . import Namespace
import regex

class NamespaceContents(ScopeContents):

    class Member(Rule):

        SEMICOLON = regex.compile(r";")

        def __init__(self, string):
            from ..variable import Variable
            from ..typedef import Typedef
            from ..function import Function
            from ..using import Using

            self.PATTERN = [
                (Variable, self.SEMICOLON),
                Typedef,
                Function,
                Using,
                Namespace
            ]

            super().__init__(string)
            self.variable = self.match[Variable]

    def __init__(self, string):
        super().__init__(string)