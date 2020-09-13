from . import Rule
import regex

class Comment(Rule):

    PATTERN = regex.compile(r"(\/\/[^\n]*\n)|(\/\*(?s).*\*\/)")