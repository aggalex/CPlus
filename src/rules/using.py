from . import Rule
from .namespaced_identifier import NamespacedIdentifier
from .scope import Scope
import regex

class Using(Rule):

    USING = regex.compile(r"using")
    SEMICOLON = regex.compile(r";")

    PATTERN = (USING, NamespacedIdentifier, SEMICOLON)

    def __init__(self, string):
        super().__init__(string)
        self.namespace = self.match[NamespacedIdentifier]