'''
module filter
'''
from filtertool.parser import Parser

class Filter(object):
    '''
    Filter class implements filter
    '''
    def __init__(self, depth=10, count=3, freq=0.2):
        self.depth = depth
        self.variant_count = count
        self.variant_freq = freq


    def match(self, line):
        '''
        :return: if this line should be called or not
        '''
        [ch, pos, ref, depth, varieties, _] = line.split()[:6]
        depth = int(depth)
        if depth < self.depth:
            return []
        parser = Parser(ch, pos, ref, depth, varieties)
        variants = parser.parse().variants()
        return filter(self.__match, variants)


    def __match(self, v):
        '''
        :return: if this **Variant** should be called or not
        '''
        if v.count < self.variant_count:
            return False
        if v.freq() < self.variant_freq:
            return False
        return True
