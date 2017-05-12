'''
Variant class
'''

class Variant(object):
    '''
    Variant represents variant
    '''
    def __init__(self, chrm, position, ref, alt, depth, count):
        self.chrm = chrm
        self.position = position
        self.ref = ref
        self.alt = alt
        self.depth = depth
        self.count = count


    def freq(self):
        '''
		:return: the frequency of this replacement
        '''
        return float(self.count) / self.depth


    def compose(self):
        '''
        :return: composed list, which is ready to output as CSV
        '''
        _id = "."
        return [self.chrm, self.position, _id, self.ref, self.alt, 60, "PASS", self.compose_info()]


    def compose_info(self):
        '''
        :return: info section of CSV
        '''
        return "NS={0},DP={1},AF={2}".format(self.count, self.depth, format(self.freq(), '.3f'))


    @classmethod
    def header(cls):
        '''
        :return: header
        '''
        return ["#CHROM", "POS", "ID", "REF", "ALT", "QUAL", "FILTER", "INFO"]


    @classmethod
    def meta(cls):
        '''
        :return: meta
        '''
        return [
            ["##INFO=<ID=NS,Number=1,Type=Integer>"],
            ["##INFO=<ID=DP,Number=1,Type=Integer>"],
            ["##INFO=<ID=AF,Number=A,Type=Float>"]
        ]
