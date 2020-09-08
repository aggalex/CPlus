from . import Rule
from .namespaced_identifier import NamespacedIdentifier
from .scope import Scope
import regex

class Identifier(Rule):

    NAMESPACE = regex.compile(r"namespace")

    PATTERN = (NAMESPACE, NamespacedIdentifier, Scope)

    def __init__(self, string):
        super().__init__(string)
        self.name = self.match[NamespacedIdentifier]
        self.scope = self.match[Scope]
