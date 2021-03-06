'''parser for lines of pileup'''
import re
from .variants import Variants

class Parser(object):
    '''
    Parser is a configurable parser
    '''

    def __init__(self, ch, position, ref, depth, s):
        self.ch = ch
        self.position = position
        self.ref = ref
        self.s = s
        self.depth = depth
        self.__nega = 0
        self.__d = {}

        self.__re_num = re.compile("(^[0-9]+)")


    def parse(self):
        '''
        parse parses
        '''
        i = 0
        while i < len(self.s):
            if self.s[i] in {".", ","}:
                i += 1
                self.__nega += 1
            elif self.s[i] in {"$"}:
                i += 1
            elif self.s[i] in {"^"}:
                i += 2
            elif self.s[i] in {"*"}:
                i += 1
                self.__nega += 1
            elif self.s[i] in {"+", "-"}:
                self.__nega += 1
                m = self.__re_num.match(self.s[i+1:])
                skip = 1 + len(m.group(0)) + int(m.group(0)) if m is not None else 1
                i += skip
            elif self.s[i] in {"A", "T", "G", "C", "a", "t", "g", "c"}:
                key = self.s[i].upper()
                self.__d[key] = self.__d[key] + 1 if self.__d.has_key(key) else 1
                i += 1
            else: i += 1

        return self


    def variants(self):
        '''
        :return: detected Variants
        '''
        return Variants(self.ch, self.position, self.ref, self.depth, self.__d)
