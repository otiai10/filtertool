'''
module filter
'''

class Filter(object):
    '''
    Filter class implements filter
    '''
    def __init__(self, depth=10, count=3, freq=0.2, multi_filter=None):
        self.depth = depth
        self.variant_count = count
        self.variant_freq = freq
        self.multi_filter = multi_filter


    def call_mutations(self, line):
        '''
        let's call mutations!!!
        :return: list of `Mutation` instances
        '''
        return self.__find_matched(line)

    def __find_matched(self, line):
        '''
        __match
        '''

        if self.multi_filter is not None and len(line.variants) < self.multi_filter.required_samples:
            raise ValueError("The input pileup file doesn't have enough samples to apply specified algorithm ({0})".format(type(self.multi_filter.alg).__name__))

        mutations = []

        first = line.variants[0]
        for key in first.valid_keys(self.depth, self.variant_count, self.variant_freq):
            if self.multi_filter is None or self.multi_filter.match(line, key):
                mutations.append(first.mutation_for_key(key))

        return mutations
