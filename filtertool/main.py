'''
module main
'''
import csv
import sys
import getopt

from .args import Args
from .line import Line
from .filter import Filter
from .multi_filter import MultiFilter
from .mutation import Mutation

def scan(source, fltr, verbose=False, trial=False):
    '''
    :return: parsed variants pool and header
    '''

    pool = Mutation.meta()
    pool += [Mutation.header()]
    head = len(pool)

    l = source.readline()
    i = 0
    tmp = 0
    while l:
        i += 1
        if verbose and i % 500 == 0:
            if tmp > 0:
                sys.stderr.write('|')
            else:
                sys.stderr.write('.')
            tmp = 0
        if verbose and i % 100000 == 0:
            sys.stderr.write("{0}\n".format(i))
        if trial   and i % 100000 == 0:
            break
        try:
            line = Line(l.split())
            for mutation in fltr.call_mutations(line):
                tmp += 1
                pool += [mutation.compose()]
        except Exception as err:
            sys.stderr.write("\n\n>>> EXCEPTION <<<\n{}\n".format(l))
            raise err
        l = source.readline()

    return (pool, head)


def write_result(output_file, result):
    '''
    call me if you want to write result file
    '''
    with open(output_file, "w") as f:
        csv.writer(f, delimiter="\t").writerows(result)


def filtertool_main(argv=None):
    '''
    This function is a proxy to call main stream instead of pip/bin
    '''
    opts, _ = getopt.getopt(argv if argv else sys.argv[1:], 'i:o:d:c:f:a:vt', [
        "input=", "output=", "depth=", "count=", "freq=", "alg=", "verbose", "trial"
    ])
    args = Args()
    args.parse(opts)

    multi_filter = MultiFilter(alg=args.alg)

    fltr = Filter(args.depth, args.count, args.freq, multi_filter)
    read_closer = sys.stdin if args.input_file == "stdin" else open(args.input_file, "r")
    (result, head) = scan(read_closer, fltr, args.verbose, args.trial)
    read_closer.close()
    sys.stderr.write("FOUND: {0}\n".format(len(result) - head))
    write_result(args.output_file, result)

if __name__ == "__main__":
    filtertool_main(sys.argv[1:])
