import sys
class Variant:

	def __init__(self, chrm, position, ref, depth, s):
		self.chrm = chrm
		self.position = position
		self.ref = ref
		self.s = s
		self.depth = depth
		self.__nega = 0
		self.tokens = []

	def parse(self):
		i = 0
		while i < len(self.s):
			if self.s[i] in {".", ","}:
				# self.tokens += [self.s[i]]
				i += 1
				self.__nega += 1
			# elif self.s[i] in {"$", "^"}:
			# 	# Skip
			# 	i += 1
			# elif self.s[i] in {"+", "-"}:
			# 	len_indel = int(self.s[i+1])
			# 	self.tokens += [self.s[i:(i + len_indel + 2)]]
			# 	i += (len_indel + 2 + 1)
			# 	self.__count += 1
			# 	self.__length += 1
			# else:
			# 	self.__count += 1
			# 	self.__length += 1
			# 	i += 1
			else: i += 1
		
		return self


	def count(self):
		return self.depth - self.__nega

	def freq(self):
		return float(self.depth - self.__nega)/self.depth
