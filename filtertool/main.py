import csv
import sys, getopt
from filter import Filter
from variant import Variant

def scan(f, fltr, verbose=False, trial=False):
	pool = Variant.meta()
	pool += [Variant.header()]
	head = len(pool)
	for i, line in enumerate(f.readlines()):
		if verbose and i % 500 == 0: sys.stderr.write('.')
		if verbose and i % 100000 == 0: sys.stderr.write("{0}\n".format(i))
		if trial   and i % 100000 == 0: break
		try:
			for v in fltr.match(line): pool += [v.compose()]
		except Exception as err:
			sys.stderr.write(line); raise err
	return (pool, head)

def write_result(output_file, result):
	with open(output_file, "w") as f:
		csv.writer(f, delimiter="\t").writerows(result)
		

def filtertool_main(argv = []):
	argv = sys.argv[1:] if len(argv) == 0 else argv
	opts, args = getopt.getopt(argv, 'i:o:d:c:f:vt', [
		"input=", "output=", "depth=", "count=", "freq=", "verbose", "trial"
	])	
	input_file = ''
	output_file = 'result.vcf'
	depth = 10
	count = 3
	freq = 0.2
	verbose = False
	trial = False
	for opt, arg in opts:
		if opt in ("-v", "--verbose"): verbose = True
		elif opt in ("-t", "--trial"): trial = True
		elif opt in ("-i", "--input"): input_file = arg
		elif opt in ("-o", "--output"): output_file = arg
		elif opt in ("-d", "--depth"): depth = int(arg)
		elif opt in ("-c", "--count"): count = int(arg)
		elif opt in ("-f", "--freq"): freq = float(arg)
	fltr = Filter(depth, count, freq)
	with open(input_file, "r") as f:
	 	(result, head) = scan(f, fltr, verbose, trial)
	 	sys.stderr.write("FOUND: {0}\n".format(len(result) - head))
	 	write_result(output_file, result)

if __name__ == "__main__":
	filtertool_main(sys.argv[1:])
