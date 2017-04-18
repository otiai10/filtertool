from variant import Variant

class Parser:

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
				key = self.s[i].upper()
				self.__d[key] = self.__d[key] + 1 if self.__d.has_key(key) else 1
				i += 1
			else: i += 1
		return self

	def variants(self):
		"""
		:return: detected Variants
		"""
		return map(lambda k: self.variant_for_key(k), self.__d.keys())


	def variant_for_key(self, key):
		"""
		:return: Variant object for key
		"""
		return Variant(self.chrm, self.position, self.ref, key, self.depth, self.__d[key])
	

