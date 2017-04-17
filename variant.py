import sys
class Variant:

	def __init__(self, chrm, position, ref, depth, s):
		self.chrm = chrm
		self.position = position
		self.ref = ref
		self.s = s
		self.depth = depth
		self.__nega = 0
		self.__d = {}

	def parse(self):
		i = 0
		while i < len(self.s):
			if self.s[i] in {".", ","}:
				i += 1
				self.__nega += 1
			elif self.s[i] in {"$", "^"}:
			 	i += 1
			elif self.s[i] in {"*"}:
				i += 1
				self.__nega += 1
			elif self.s[i] in {"+", "-"}:
				self.__nega += 1
				try: indel = int(self.s[i+1]); i += (indel + 2 + 1)
				except: i += 1
			elif self.s[i] in {"A", "T", "G", "C", "a", "t", "g", "c"}:
				self.__d[self.s[i]] = self.__d[self.s[i]] + 1 if self.__d.has_key(self.s[i]) else 1
				i += 1
			# else:
			# 	self.__count += 1
			# 	self.__length += 1
			# 	i += 1
			else: i += 1
		
		return self

	def alt(self):
		return ''.join(self.__d.keys())

	def count(self):
		return self.depth - self.__nega

	def freq(self):
		return float(self.depth - self.__nega)/self.depth
