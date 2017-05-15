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


class Fishers(MFAlgorithm):
    '''
    implements fisher test
    '''
    def __init__(self, p=0.8):
        super(Fishers, self).__init__()
        self.pvalue = float(p)

    def match(self, line, key):
        '''
        match execute Fisher test
        '''
        x = line.variants[0]
        y = line.variants[1]
        table = [
            [x.dictionary[key], x.depth - x.dictionary[key]],
            [y.dictionary[key], y.depth - y.dictionary[key]]
        ]
        _, pvalue = scipy.stats.fisher_exact(table)
        return pvalue > self.pvalue

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
            self.alg = Fishers(alg["params"]["p"])
        else:
            raise Exception("No MFAlgorithm exists with name:", alg["name"])


    def match(self, line, key):
        '''
        match
        '''
        if self.alg is None or isinstance(self.alg.match, types.MethodType) is False:
            return True
        return self.alg.match(line, key)
