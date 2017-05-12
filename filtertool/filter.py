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
        self.multi_filter = None


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
        mutations = []

        first = line.variants[0]
        for key in first.valid_keys(self.depth, self.variant_count, self.variant_freq):
            if self.multi_filter is None or self.multi_filter.match(line):
                mutations.append(first.mutation_for_key(key))

        return mutations
