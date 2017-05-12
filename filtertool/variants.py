'''
Variant class
'''

from filtertool.mutation import Mutation

class Variants(object):
    '''
    Variants represents variant
    '''
    def __init__(self, ch, position, ref, depth, dictionary):
        self.ch = ch
        self.pos = position
        self.ref = ref
        self.depth = depth
        self.dictionary = dictionary

    def freq_for_key(self, key):
        '''
		:return: the frequency of this replacement
        '''
        return float(self.dictionary[key]) / self.depth

    def valid_keys(self, depth, count, freq):
        '''
        :return: keys of dictionary, would be some of ['A','C','G','T']
        '''
        keys = []
        if self.depth < depth:
            return keys
        for key in self.dictionary.keys():
            if self.dictionary[key] < count:
                continue
            if self.freq_for_key(key) < freq:
                continue
            keys.append(key)
        return keys


    def mutation_for_key(self, key):
        '''
        mutation for key
        '''
        return Mutation(
            self.ch,
            self.pos,
            self.ref,
            key,
            self.dictionary[key],
            self.depth
        )
