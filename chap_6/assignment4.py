import os.path, sys

class ConfigDict(dict):

	def __init__(self, filename):
		self._filename = filename
		
		try:
			with open(self._filename) as fh:
				for line in fh:
					line = line.rstrip()
					key, value = line.split('=')
					dict.__setitem__(self, key, value)

		except IOError as e:
			print "The file does not exist."
			sys.exit()
		
	def __setitem__(self, key, value):
		dict.__setitem__(self, key, value)
		
		with open(self._filename, 'w') as fh:
				for key, value in self.items():
					fh.write('{0}={1}\n'.format(key, value))

	def __getitem__(self, key):
		try:
			dict.__getitem__(self, key)
			return self.get(key)
		except KeyError, e:
			raise ConfigKeyError(self, key)


class ConfigKeyError(Exception):
	def __init__(self,key,error):
		self.key = key
		self.extra = error

	def __str__(self):
		return "Key %s not found. Avaiable keys: %s" %(self.extra, self.key.keys())