# Credit to MirzaSB for his help and insights to starting off.
import datetime

class WriteFile(object):
	# set up file name and  the formatter
	def __init__(self, fileName, formatter):
		self.target = open(fileName, 'w')
		self.formatter = formatter()

	# function to write input to file
	def write(self,input):
		# gets the file, then calls the formatter
		# then uses the formatters function and adds the input
		# then adds a new line for extra function calls
		self.target.write(self.formatter.write(input) + "\n")

	# meathod to close the file
	def close(self):
		self.target.close()

class CSVFormatter(object):

	def write(self, input):
		delim = "," # sets the delimitter 
		array = [] # sets a new list

		for item in input:
			# finds the delimitter and then quoting the item in list
			if delim in item:
				item = "\"" + item + "\""
				array.append(item)
			else:
				array.append(item)

		return delim.join(array)

class LogFormatter(object):
	# sets up the time stamp
	dt_str = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')

	def write(self, input):
		return self.dt_str + "\t" + input
