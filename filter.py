from variant import Variant

class Filter:

	def __init__(self, depth = 10, count = 3, freq = 0.2):
		self.depth = depth
		self.variant_count = count
		self.variant_freq = freq

	def match(self, line):
		[ch, pos, ref, depth, varieties, qualities] = line.split()
		depth = int(depth)
		if depth < self.depth: return None
		v = Variant(ch, pos, ref, depth, varieties)	
		v.parse()
		if v.count() < self.variant_count: return None
		if v.freq()  < self.variant_freq:  return None
		return v
