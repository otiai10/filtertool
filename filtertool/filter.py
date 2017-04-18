from parser import Parser

class Filter:

	def __init__(self, depth = 10, count = 3, freq = 0.2):
		self.depth = depth
		self.variant_count = count
		self.variant_freq = freq

	def match(self, line):
		[ch, pos, ref, depth, varieties, qualities] = line.split()
		depth = int(depth)
		if depth < self.depth: return []
		parser = Parser(ch, pos, ref, depth, varieties)	
		variants = parser.parse().variants()
		return filter(lambda v: self.__match(v), variants)

	def __match(self, v):
		if v.count < self.variant_count: return False
		if v.freq()  < self.variant_freq:  return False
		return True
		
