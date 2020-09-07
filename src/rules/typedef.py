from . import Rule
from .declaration import Declaration
import regex

class Typedef(Rule):

    TYPEDEF = regex.compile(r"typedef")
    SEMICOLON = regex.compile(r";")

    PATTERN = (TYPEDEF, Declaration, SEMICOLON)

    def __init__(self, string):
        super().__init__(string)
        self.type = self.match[Declaration].type
        self.name = self.match[Declaration].name
