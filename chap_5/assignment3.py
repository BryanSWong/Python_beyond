import os

class ConfigDict(dict):
	def __init__(self, filename):
		self._filename = filename
		self.arr = {} # array to store items found
		if os.path.isfile(self._filename):
			with open(self._filename) as fh:
				for line in fh:
					line = line.rstrip()
					key, val = line.split('=')
					#sets a dict with the read key and values
					add = {key : val}
					self.arr.update(add)
					dict.__setitem__(self, key, val)

	def __setitem__(self, key, value):
		dict.__setitem__(self, key, value)
		with open(self._filename, 'w') as fh:
			for key in self.arr:
				fh.write('{0}={1}\n'.format(key, self.arr[key]))
			#writes the extra created items
			fh.write('{0}={1}\n'.format(key, value))

"""
sql_query=SELECT this FROM that WHERE condition
email_to=me@mydomain.com
num_retries=5
"""