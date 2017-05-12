'''
Args class
'''

class Args(object):
    '''
    Args represents cli arguments
    '''
    def __init__(self):
        self.input_file = ''
        self.output_file = 'result.vcf'
        self.depth = 10
        self.count = 3
        self.freq = 0.2
        self.verbose = False
        self.trial = False


    def parse(self, opts):
        '''
        parse
        '''
        for opt, arg in opts:
            if opt in ("-v", "--verbose"):
                self.verbose = True
            elif opt in ("-t", "--trial"):
                self.trial = True
            elif opt in ("-i", "--input"):
                self.input_file = arg
            elif opt in ("-o", "--output"):
                self.output_file = arg
            elif opt in ("-d", "--depth"):
                self.depth = int(arg)
            elif opt in ("-c", "--count"):
                self.count = int(arg)
            elif opt in ("-f", "--freq"):
                self.freq = float(arg)
        return self
