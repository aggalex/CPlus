from .. import Rule
from ..identifier import Identifier
import regex

class Generics(Rule):

    class TypeList(Rule):

        COMMA = regex.compile(r",")

        def __init__(self, string):
            from .type import Type
            self.PATTERN = [
                (Type, self.COMMA, self.__class__),
                Type
            ]
            super().__init__(string)
            if self.pattern_choice == 1:
                self.types = [self.match]
            else:
                self.types = [self.match[Type]] + self.match[Generics.TypeList].types
            
    DIAMOND_OPEN = regex.compile(r"<")
    DIAMOND_CLOSE = regex.compile(r">")

    PATTERN = (DIAMOND_OPEN, TypeList, DIAMOND_CLOSE)

    def __init__(self, string):
        super().__init__(string)
        self.types = self.match[Generics.TypeList].types

    def __getitem__(self, key):
        return self.types[key]

    def __len__(self):
        return len(self.types)
        