import csv
import sys
from filter   import Filter

def scan(f, fltr):
	pool = []
	for i, line in enumerate(f.readlines()):
		if i != 0 and i % 500 == 0: sys.stderr.write('.')
		if i % 100000 == 0: sys.stderr.write("{0}\n".format(i))
		# if i != 0 and i % 100000 == 0: break
		try:
			for v in fltr.match(line): pool += [v.compose()]
		except Exception as err:
			sys.stderr.write(line)
			raise err
	return pool

def write_result(result):
	with open("result.csv", "w") as f:
		csv.writer(f, delimiter="\t").writerows(result)
		

def main():
	fltr = Filter()
	with open("test.pileup", "r") as f:
		result = scan(f, fltr)
		sys.stderr.write("FOUND: {0}\n".format(len(result)))
		write_result(result)

if __name__ == "__main__":
	main()
