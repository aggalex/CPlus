from .. import Rule
from ..identifier import Identifier
from ..scope import Scope
from enum import IntEnum
import regex

class Type(Rule):

    KEYWORD = regex.compile(r"struct|union|enum")

    PATTERN = [
        (KEYWORD, Identifier, Scope),
        (KEYWORD, Scope),
        Identifier,
        # (regex.compile(r"typedef"), Type, Identifier),
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

        if self.match.__class__ != dict:
            self.type = self.Type.NAMED
            self.name = self.match.match.group()
            return
        
        self.type = self.Type.from_keyword(self.match[self.KEYWORD].group())

        try:
            self.name = self.match[Identifier].match.group()
        except KeyError:
            self.name = None

        self.contents = self.match[Scope]
