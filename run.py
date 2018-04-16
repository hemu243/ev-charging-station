import os
from data_initializer import stations, SingletonClass

class Runner(object):
	"""
	Main class which is used to run this project
	"""
	def __init__(self, distance_threshold):
		"""
		:param distance_threshold: distance threshold which is being used by algorithm to calculate
			right distance for
		"""
		if isinstance(distance_threshold, float) and distance_threshold > 0:
			self.distance_threshold = distance_threshold
		else:
			raise ValueError("Invalid threshold value (needs float value)")

	def run(self):
		"""
			Add run logic here
		:return:
		"""
		print self.distance_threshold
		singleton_stations = SingletonClass(stations.Stations)
		existing_stations = singleton_stations()
		existing_stations.initialized_data("AIzaSyAI2e4z9hZXQPrypTRU5XPUOznjZlfewmg")


if __name__ == "__main__":
	runner = Runner(50.0)
	runner.run()
