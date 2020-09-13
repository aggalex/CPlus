from .. import Rule
from .type import Type
from .generics import Generics
from ..namespaced_identifier import NamespacedIdentifier
import regex

class Declaration(Rule):

    POINTER_STARS = regex.compile(r"(\*\s*)*")

    PATTERN = [
        (Type, POINTER_STARS, NamespacedIdentifier, Generics),
        (Type, POINTER_STARS, NamespacedIdentifier)
    ]

    def __init__(self, string):
        super().__init__(string)
        self.type = self.match[Type]
        self.pointer_depth = self.match[self.POINTER_STARS].group().count("*")
        self.name = self.match[NamespacedIdentifier].identifiers[-1]
        self.namespaces = self.match[NamespacedIdentifier].identifiers[:-1]

        try:
            self.generics = self.match[Generics]
        except KeyError:
            self.generics = None