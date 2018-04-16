"""
Singleton Decorator to define singleton class
"""


class SingletonClass(object):
	"""
		A decorator class to define any class as singleton
	"""

	def __init__(self, klass):
		"""
		Init method
		:param klass: class name
		"""
		self.klass = klass
		self.instance = None

	def __call__(self, *args, **kwargs):
		"""
		Overwrite __class__ method
		:param args: list of arguments
		:param kwargs: list of key, value args
		:return: class instance
		"""
		if self.instance is None:
			self.instance = self.klass(*args, **kwargs)
		return self.instance
