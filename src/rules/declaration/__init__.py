from .. import Rule
from .type import Type
from ..identifier import Identifier
import regex

class Declaration(Rule):

    POINTER_STARS = regex.compile(r"(\*\s*)*")

    PATTERN = (Type, POINTER_STARS, Identifier)

    def __init__(self, string):
        super().__init__(string)
        self.type = self.match[Type]
        self.pointer_depth = self.match[self.POINTER_STARS].group().count("*")
        self.name = self.match[Identifier].match.group()