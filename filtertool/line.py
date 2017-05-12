'''
Line
'''
from filtertool.parser import Parser

class Line(object):
    '''
    Line represents each line of pileup file.
    It should have following stuff
        1. Number of Chromosome
        2. Position Index
        3. Reference Base it should be
        4. Samples provided (e.g. Tumor sample, Normal sample)
    '''
    def __init__(self, columns):
        [ch, pos, ref] = columns[:3]
        self.ch = ch
        self.pos = pos
        self.ref = ref
        self.variants = self.__parse_columns(columns[3:])

    def __parse_columns(self, cols):
        '''
        parses rest columns except for `ch`, `pos`, `ref`
        '''
        self.variants = []
        for i in range(0, len(cols) / 3):
            [depth, varieties, _] = cols[i*3:(i+1)*3]
            parser = Parser(self.ch, self.pos, self.ref, int(depth), varieties)
            self.variants.append(parser.parse().variants())
        return self.variants
