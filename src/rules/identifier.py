from . import Rule
import regex

class Identifier(Rule):

    PATTERN = regex.compile(r"[A-Za-z_][A-Za-z_0-9]*")