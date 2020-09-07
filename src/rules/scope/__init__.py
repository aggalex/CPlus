from .. import Rule
from .scope_contents import ScopeContents
import regex

class Scope(Rule):

    PATTERN = regex.compile(r"{([^{}]*(?R))*[^{}]*}")

    def get_subscopes(self):
        match = self.match.group()[1:-1]
        subscopes = [Scope(match.group()) for match in self.PATTERN.finditer(match)]
        return tuple({
                "scope": scope,
                "sub": scope.get_subscopes()
            }
        for scope in subscopes)

    def get_contents(self, cls):
        if not issubclass(cls, ScopeContents):
            raise TypeError(f"Expected class that inherits from ScopeContents, got {cls}")
        return cls(self.match.group()[1:-1])

    def __str__(self):
        return str(self.match)
