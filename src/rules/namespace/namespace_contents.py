from ..scope.scope_contents import ScopeContents, Rule
import regex

class NamespaceContents(ScopeContents):

    class Member(Rule):

        SEMICOLON = regex.compile(r";")

        def __init__(self, string):
            from . import Namespace
            from ..variable import Variable
            from ..typedef import Typedef
            from ..function import Function
            from ..using import Using
            from ..comment import Comment
            from ..include import Include
            from ..preprocessor import Preprocessor
            from ..template import Template
            from ..declaration import Type

            self.PATTERN = [
                Comment,
                Include,
                Preprocessor,
                Namespace,
                Using,
                Template,
                Typedef,
                Function,
                (Variable, self.SEMICOLON),
                Type
            ]

            super().__init__(string)
            if self.pattern_choice == 0:
                self.match = self.match[Variable]

    def __init__(self, string):
        super().__init__(string)