class DITK_TextEmbedding():

	# Any shared data strcutures or methods should be defined as part of the parent class.
	# A list of shared arguments should be defined for each of the following methods and replace (or precede) *args.
	# The output of each of the following methods should be defined clearly and shared between all methods implemented by members of the group.

	"""
	Benchmarks:
		1. CornelMovieDataset: sentence
			e.g. "uncompromising french director robert bresson's " lancelot of the lake..."
		2. CoNll2003: NER
			e.g. ["LOC","Afghanistan"]
		3. CategoricalDataset:
			e.g. ["Office Services Coordinator", 69222.18]
	"""

	def __init__(self):
		pass

	def read_Dataset():
		pass

	def readCornellMovieDataset():
		pass

	def readCategoricalDataset():
		pass

	def readCoNll2003():
		pass

	def train():
		"""
		args:	string
		return: string
		"""
		pass

	def predict():
		"""
		args: string: a sentence to embed
		return: vector[int]: a vector embedding of
		"""
		pass

	def evaluate():
		"""
		args: 	string:
				float:
		return: string:
				float:
		"""
		pass
