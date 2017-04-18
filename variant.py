
class Variant:

	def __init__(self, chrm, position, ref, alt, depth, count):
		self.chrm = chrm
		self.position = position
		self.ref = ref
		self.alt = alt
		self.depth = depth
		self.count = count

	def freq(self):
		"""
		:return: the frequency of this replacement
		"""
		return float(self.count) / self.depth

	def compose(self):
		return [self.chrm, self.position, self.ref, self.alt, self.depth, self.count, self.freq()]
