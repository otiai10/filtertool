'''
filtertool.mutation
'''


class Mutation(object):
    '''
    Mutation represents called mutation.
    It is **JUST** responsible to output VCF file's row as CSV format.
    '''
    def __init__(self, ch, pos, ref, alt, count, depth):
        self.ch = ch
        self.pos = pos
        self.ref = ref
        self.alt = alt
        self.count = count
        self.depth = depth

    def compose(self):
        '''
        :return: composed list, which is ready to output as CSV
        '''
        _id = "."
        return [self.ch, self.pos, _id, self.ref, self.alt, 60, "PASS", self.compose_info()]


    def compose_info(self):
        '''
        :return: info section of CSV
        '''
        af = format(float(self.count/self.depth), ".3f")
        return "NS={0},DP={1},AF={2}".format(self.count, self.depth, af)


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
