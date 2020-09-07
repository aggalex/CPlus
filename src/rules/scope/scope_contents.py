from .. import Rule

# pylint: disable=no-member.

class ScopeContents(Rule):

    def __init__(self, string):
        self.PATTERN = [
            self.CONTENT,
            (self.__class__, self.CONTENT)
        ]
        super().__init__(string)
        if self.pattern_choice == 0:
            self.patterns = [self.match]
        else:
            self.patterns = self.match[ScopeContents] + [self.match[self.PATTERN[1]]]