from . import Rule
from .identifier import Identifier
import regex
import os

class Include(Rule):

    INCLUDE = regex.compile (r"#\s*include")

    PATH_OPEN = regex.compile (r'<|"')
    PATH_CLOSE = regex.compile (r'>|"')

    PATH = regex.compile (
            r"([^\"\*\/\:<>\?\\\|]*\\)*[^\"\*\/\:<>\?\\\|]*" if os.name == "nt" else
            r"([^/]*/)*[^/]*"
        )

    PATTERN = (INCLUDE, PATH_OPEN, PATH, PATH_CLOSE)

    def __init__(self, string):
        super().__init__(string)

        assert( (self.match[self.PATH_OPEN].group() == '<' and self.match[self.PATH_CLOSE].group() == '>') or
                (self.match[self.PATH_OPEN].group() == self.match[self.PATH_CLOSE].group() == '"'))

        self.path = self.match[self.PATH].group()
        self.is_relative = self.match[self.PATH_OPEN].group() == '"'
        self.is_cplus = self.match[self.PATH].group().endswith(".hp")