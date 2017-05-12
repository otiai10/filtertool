'''
module main
'''
import csv
import sys
import getopt
from filtertool.filter import Filter
from filtertool.variant import Variant
from filtertool.args import Args

def scan(source, fltr, verbose=False, trial=False):
    '''
    :return: parsed variants pool and header
    '''

    pool = Variant.meta()
    pool += [Variant.header()]
    head = len(pool)
    line = source.readline()

    i = 0
    while line:
        i += 1
        if verbose and i % 500 == 0:
            sys.stderr.write('.')
        if verbose and i % 100000 == 0:
            sys.stderr.write("{0}\n".format(i))
        if trial   and i % 100000 == 0:
            break
        try:
            for v in fltr.match(line):
                pool += [v.compose()]
        except Exception as err:
            sys.stderr.write(line)
            raise err
        line = source.readline()

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
    opts, _ = getopt.getopt(argv if argv else sys.argv[1:], 'i:o:d:c:f:vt', [
        "input=", "output=", "depth=", "count=", "freq=", "verbose", "trial"
    ])
    args = Args()
    args.parse(opts)

    fltr = Filter(args.depth, args.count, args.freq)
    read_closer = sys.stdin if args.input_file == "stdin" else open(args.input_file, "r")
    (result, head) = scan(read_closer, fltr, args.verbose, args.trial)
    read_closer.close()
    sys.stderr.write("FOUND: {0}\n".format(len(result) - head))
    write_result(args.output_file, result)

if __name__ == "__main__":
    filtertool_main(sys.argv[1:])
