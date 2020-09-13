from . import Rule
from .declaration.type import Generics, Type
from .function import Function
from .typedef import Typedef
import regex

class Template(Rule):

    class TemplateContents(Rule):
        
        PATTERN = [
            Function,
            Typedef,
            Type
        ]

    TEMPLATE = regex.compile("template")

    PATTERN = (TEMPLATE, Generics, TemplateContents)

    def __init__(self, string):
        super().__init__(string)
        self.generics = self.match[Generics]
        self.contents = self.match[self.TemplateContents]