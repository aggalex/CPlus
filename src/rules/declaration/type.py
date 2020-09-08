from .. import Rule
from ..namespaced_identifier import NamespacedIdentifier
from ..scope import Scope
from enum import IntEnum
from .struct_contents import StructContents
import regex

class Type(Rule):

    KEYWORD = regex.compile(r"struct|union|enum")

    PATTERN = [
        (KEYWORD, NamespacedIdentifier, Scope),
        (KEYWORD, Scope),
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

        if self.match.__class__ != dict:
            self.type = self.Type.NAMED
            self.__set_name(self.match)
            return
        
        self.type = self.Type.from_keyword(self.match[self.KEYWORD].group())

        try:
            self.__set_name(self.match[NamespacedIdentifier])
        except KeyError:
            self.name = None

        self.scope = self.match[Scope]
        self.contents = self.match[Scope].get_contents(StructContents)

    def __set_name(self, ns_ident):
        self.name = ns_ident.identifiers[-1]
        self.namespaces = ns_ident.identifiers[:-1]