'''
multi_filter
'''
from abc import ABCMeta, abstractmethod
import types
import scipy.stats

class MFAlgorithm(object):
    '''
    MFAlgorithm defines interface of MultiFilter Algorithm
    '''
    __metaclass__ = ABCMeta

    @abstractmethod
    def match(self, line, key):
        '''
        :return: if this filter allow this line for key
        '''
        return False

    @abstractmethod
    def required_samples(self):
        '''
        : return: number of required samples
        '''
        return 1


class Fishers(MFAlgorithm):
    '''
    implements fisher test
    '''
    def __init__(self, p=0.1):
        super(Fishers, self).__init__()
        self.pvalue = float(p if p is not None else 0.1)

    def match(self, line, key):
        '''
        match execute Fisher test
        '''
        x = line.variants[0]
        y = line.variants[1]
        table = [
            [x.dictionary.get(key, 0), x.depth - x.dictionary.get(key, 0)],
            [y.dictionary.get(key, 0), y.depth - y.dictionary.get(key, 0)]
        ]
        _, pvalue = scipy.stats.fisher_exact(table)
        return pvalue < self.pvalue

    def required_samples(self):
        return 2

class MultiFilter(object):
    '''
    MultiFilter defines a filter which can evaluate multi samples.
    e.g. Tumor, Normal
    '''
    def __init__(self, alg=None):
        self.alg = alg
        if alg is None:
            return
        if alg["name"] in ("fishers", "Fishers"):
            self.alg = Fishers(p=alg["params"].get("p"))
        else:
            raise Exception("No MFAlgorithm exists with name:", alg["name"])


    def match(self, line, key):
        '''
        match
        '''
        if self.alg is None or isinstance(self.alg.match, types.MethodType) is False:
            return True
        return self.alg.match(line, key)

    def required_samples(self):
        '''
        required_samples
        '''
        if self.alg is None or isinstance(self.alg.match, types.MethodType) is False:
            return 1
        return self.alg.required_samples()
