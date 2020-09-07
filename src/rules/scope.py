from . import Rule
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

    def __str__(self):
        return str(self.match)
