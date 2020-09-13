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
            from ..comment import Comment
            from ..include import Include
            from ..preprocessor import Preprocessor

            self.PATTERN = [
                (Variable, self.SEMICOLON),
                Include,
                Preprocessor,
                Typedef,
                Function,
                Using,
                Namespace,
                Comment,
            ]

            super().__init__(string)
            if self.pattern_choice == 0:
                self.match = self.match[Variable]

    def __init__(self, string):
        super().__init__(string)