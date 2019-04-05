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
		"""
		Shared data members initialized in the constructor -- 

		sentences -- input for each model as required by each method
		benchmarks -- list of pre-defined benchmarks as strings
		benchmark_flag -- boolean value to indicate if the dataset is a benchmark or not
		metrics -- dictionary of evaluation metrics along with their computed values after testing
		"""
		self.sentences = []
		self.benchmarks = ['conll2003', 'cornellMD', 'categorical', 'semEval']
		self.is_benchmark = 0
		self.metrics = {
							'conll2003' : ['precision', 'recall', 'F1'],
							'cornellMD' : ['precision', 'recall', 'F1'],
							'categorical' : ['mse'],
							'semEval' : ['pearseon_coeff']
						}

	@classmethod
	@abc.abstractmethod
	def read_Dataset(self, name, fileName):
		pass

	def readCornellMovieDataset(self, fileName):
		pass

	def readCategoricalDataset(self, fileName):
		pass

	def readCoNll2003(self, fileName):
		pass

	def readSemEval(self, fileName):
		pass
		
    @classmethod
	@abc.abstractmethod
	def train():
		"""
		args:	string
		return: string
		"""
		pass

	@classmethod
	@abc.abstractmethod
	def predict_embedding(self, input):
		"""
		Task - Predicts the embedding of the given string/sentence/file 

		args: string/ sentence/ file
		return: vector[int]: a vector embedding of the string/ sentence/ file
		"""

	@classmethod
	@abc.abstractmethod
	def predict_similarity(self, input1, input2):
		"""
		args: two strings/two sentences/two files
		return: similarity score (float)
		"""	
	@classmethod
	@abc.abstractmethod
	def evaluate(self, model, filename):
		"""
		Task - Evaluates a pre-trained model on the test dataset and returns the evaluation along with metrics as a dictionary

		Input:
		model -- path to the pre-trained model
		filename -- path to the evaluation/test dataset
		
		return: 
		Dictionary of {evaluation_metric<string>:calculated_value<float>}
		"""
		pass
