import csv


class CSVReader(object):

	"""
	Main class to read CSV file
	"""
	def __init__(self, filename):
		if not isinstance(filename, basestring):
			raise ValueError("Invalid file name")
		self.filename = filename
		self.csv_data = []

	def _read_csv(self):
		"""
		Read csv file
		:return: list of data read from csv
		"""
		try:
			csv_fp = open(self.filename, 'rb')
			reader = csv.DictReader(csv_fp)
			for line in reader:
				self.csv_data.append(line)
			return self.csv_data
		except IOError as e:
			print e
			raise e
