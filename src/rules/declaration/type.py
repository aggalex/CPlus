from .. import Rule
from ..namespaced_identifier import NamespacedIdentifier
from ..scope import Scope
from enum import IntEnum
from .struct_contents import StructContents
from .generics import Generics
import regex

class Type(Rule):

    KEYWORD = regex.compile(r"struct|union|enum")

    PATTERN = [
        (KEYWORD, NamespacedIdentifier, Scope),
        (KEYWORD, Scope),
        (KEYWORD, NamespacedIdentifier, Generics),
        (KEYWORD, NamespacedIdentifier),
        (NamespacedIdentifier, Generics),
        NamespacedIdentifier,
    ]

    class Type(IntEnum):
        NAMED=0
        STRUCT=1
        UNION=2
        ENUM=3

        @classmethod
        def from_keyword(cls, key):
            keys = {
                "struct": Type.Type.STRUCT,
                "union": Type.Type.UNION,
                "enum": Type.Type.ENUM
            }
            return keys[key]

    def __init__(self, string):
        super().__init__(string)

        self.namespaces = []

        self.generics = None

        if self.pattern_choice == 4:
            self.generics = self.match[Generics]
            self.type = self.Type.NAMED
            self.__set_name(self.match[NamespacedIdentifier])
            return

        if self.pattern_choice == 5:
            self.type = self.Type.NAMED
            self.__set_name(self.match)
            return
        
        self.type = self.Type.from_keyword(self.match[self.KEYWORD].group())

        try:
            self.__set_name(self.match[NamespacedIdentifier])
        except KeyError:
            self.name = None

        try:
            self.scope = self.match[Scope]
        except KeyError:
            self.scope = None
            self.contents = None

        if self.scope != None:
            self.contents = self.scope.get_contents(StructContents)
            try:
                self.base = next(member.declaration.type for member in self.contents.members if member.declaration.name == "base")
            except StopIteration:
                pass

    def __set_name(self, ns_ident):
        self.name = ns_ident.identifiers[-1]
        self.namespaces = ns_ident.identifiers[:-1]