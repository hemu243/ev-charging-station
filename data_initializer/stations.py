import os
import requests
import json
import hashlib
from data_initializer import SingletonClass, csv_reader

class Stations(object):
	"""
	A class which hold existing stations information like address, latitude and longitude etc..
	"""
	def __init__(self):
		"""
		Initialized existing gas or EV stations
		"""
		current_path = os.path.abspath(os.path.dirname(__file__))
		singleton_csv_reader = SingletonClass(csv_reader.CSVReader)
		self.resource_folder = os.path.join(current_path, "..", "resources")
		self.cached_lat_lgt_file_path = os.path.join(self.resource_folder, "lt_gt_cache.json")
		# Store csv reader reference
		self.csv_reader_instance = singleton_csv_reader(os.path.join(self.resource_folder, "alt_fuel_stations.csv"))
		self.csv_reader_instance.read_csv()
		print len(self.csv_reader_instance.csv_data)

	def initialized_data(self, api_key):
		"""

		:param api_key:
		:return:
		"""
		self._get_lat_and_lgt(api_key)

	def _initialized_cache(self):
		"""
		Read already initialized address, longitude and latitude
		:return:
		"""
		if not os.path.exists(self.cached_lat_lgt_file_path):
			return {}
		with open(self.cached_lat_lgt_file_path, 'r') as fp:
			json_data = json.load(fp)
		return json_data

	def _save_cache(self, json_data):
		"""
		Store json data to cache file
		:param json_data: json data
		:return: None
		"""
		with open(self.cached_lat_lgt_file_path, 'w+') as fp:
			fp.write(json.dumps(json_data))

	def _get_lat_and_lgt(self, api_key, limit=2400, time_delay=20):
		"""
		Get longitude and latitude for address stored in csv_reader instance
		:param api_key: google api key to get geo location,
				refer - https://developers.google.com/maps/documentation/geocoding/start for more info
		:param limit: since google api has some limit on API call, which is 2500/day, and 50/sec
				refer - https://developers.google.com/maps/documentation/geocoding/usage-limits for
				more information
		:param time_delay (ms): delay between each request so we will not hit per sec limit
		:return:
		"""
		# https://maps.googleapis.com/maps/api/geocode/json?address=Winnetka&key=YOUR_API_KEY
		cache_json_data = self._initialized_cache()
		for cdata in self.csv_reader_instance.csv_data:
			pass
		cdata = self.csv_reader_instance.csv_data[0]
		## Fuel Type Code
		## Street Address
		## City
		## State
		## Zip
		## Latitude
		## Longitude
		address = "1600 Amphitheatre Parkway, Mountain View, CA"
		address_hash = hashlib.sha256(address).hexdigest()
		if cache_json_data.get(address_hash):
			print "No operation"
			return
		req = requests.get("https://maps.googleapis.com/maps/api/geocode/json", {"address": address, "key": api_key})
		if req.status_code == 200:
			cache_json_data[address_hash] = req.json()['results'][0]
			self._save_cache(cache_json_data)
		else:
			# save cache and raise warning
			self._save_cache(cache_json_data)
			raise RuntimeWarning("Failed to get longitude and latitude for address={0}, status_code="
							 "{1}, reason={2}".format(address, req.status_code, req.reason))



