import regex

# pylint: disable=no-member.

WHITESPACE = regex.compile(r"\s*")

class Rule:

    def __init__(self, string):
        # self.string = string
        # if self.PATTERN.__class__ != list:
        #     self.match = self.PATTERN.search(string)
        # else: 
        #     for patterns in self.PATTERN:
        #         if patterns.__class__ == tuple:
        #             for pattern in patterns:
        #                 if self.pattern.__class__ == MatchInfo:
        #                     self.match = self.pattern()
        #         elif match := patterns.search(string):
        #             self.match = match
        #             break
        # if not self.match:
        #     raise MatchError(string, self.PATTERN.__class__)
        # self.start, self.end = self.match.span()
        self.string = string

        patterns = None

        if self.PATTERN.__class__ == tuple:
            patterns = [self.PATTERN]
        elif self.PATTERN.__class__ != list:
            patterns = [(self.PATTERN,)]
        else:
            patterns = self.PATTERN

        self.match = {}
        self.end = -1

        self.pattern_choice = 0
        for pattern in patterns:
            end = 0
            for segment in pattern if pattern.__class__ == tuple else (pattern,):
                print(f"String: '{string[end:]}'")
                ws_data = WHITESPACE.match(string[end:])
                _, ws_end = ws_data.span()
                end += ws_end
                print(f"WSSTR: '{string[end:]}'")
                data = None
                if segment.__class__ == type and issubclass(segment, Rule):
                    try:
                        print(f"MATCHING {segment.__name__} WITH {string[end:]}")
                        data = segment(string[end:])
                        end += data.end
                    except MatchError as err:
                        print(f"Match failed: {err}")
                        data = None
                else:
                    data = segment.match(string[end:])
                    if data:
                        _, data_end = data.span()
                        end += data_end
                if not data:
                    self.match = {}
                    break
                self.match[segment] = data
            self.end = end

            if len(self.match) != 0:
                break

            self.pattern_choice += 1
                    
        if len(self.match) == 0:
            raise MatchError(string, self.__class__)

        if len(self.match) == 1:
            self.match = list(self.match.values())[0]

    def __eq__(self, obj):
        return obj.__class__ is Rule and obj.match.group() == obj.match.group()

class MatchError(Exception):

    def __init__(self, string, match_cls = Rule, message = None):
        self.string = string
        self.match_cls = match_cls
        self.message = message if message else f"Class {match_cls.__name__} found no match for: \n {string}"