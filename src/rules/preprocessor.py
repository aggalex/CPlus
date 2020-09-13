from . import Rule
import regex

class Preprocessor(Rule):

    PATTERN = regex.compile(r"#(\\\n|[^\n])*")