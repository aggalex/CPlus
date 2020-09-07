from . import Rule
from .identifier import Identifier
import regex

class NamespacedIdentifier(Rule):

    NAMESPACE_OP = regex.compile(r"::")

    def __init__(self, string):
        self.PATTERN = [
            (Identifier, self.NAMESPACE_OP, NamespacedIdentifier),
            Identifier
        ]
        super().__init__(string)
        if self.pattern_choice == 1:
            self.identifiers = [self.match]
        else:
            self.identifiers = [self.match[Identifier]] + self.match[NamespacedIdentifier].identifiers
