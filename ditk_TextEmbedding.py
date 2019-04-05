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

		sentences -- list of token obtained from the dataset
		benchmarks -- list of pre-defined benchmarks as strings
		benchmark_flag -- boolean value to indicate if the dataset is a benchmark or not
		metrics -- dictionary of evaluation metrics along with their computed values after testing
		"""
		self.sentences = []
		self.benchmarks = ['conll2003', 'cornellMD', 'categorical']
		self.benchmark_flag = 0
		self.metrics = {}

	def read_Dataset():
		pass

	def readCornellMovieDataset():
		pass

	def readCategoricalDataset():
		pass

	def clean_conll2003(text, to_lower=False):
    # clean the text: no weird or special characters
    text = unidecode(text.decode("utf-8"))
    # normalize numbers
    text = re.sub(r"[0-9]", "1", text)
    if to_lower:
        text = text.lower()
    return text

	def readCoNll2003(self, to_lower=False, sources=["data/conll2003/train.txt"]):
		for fname in sources:
            tokens = []
            for line in open(fname):
                if line.startswith("-DOCSTART- -X- -X-"):
                    if tokens:
                        yield tokens
                    tokens = []
                elif line.strip():
                    tokens.append(clean_conll2003(line.split()[0], to_lower))
                else:
                    tokens.append('')
            yield tokens

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
		

	def evaluate(self):
		"""
		Task - Evaluates a pre-trained model on the test dataset and returns the evaluation metrics as a dictionary

		Input:
		model -- path to the pre-trained model
		filename -- path to the evaluation/test dataset
		
		return: 
		Dictionary of {evaluation_metric<string>:calculated_value<float>}
		"""
		pass
