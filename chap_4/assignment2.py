import datetime, csv, sys, abc

'''
example of using the datetime
dt_str = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
'''

class WriteFile(object):
	__metaclass__ = abc.ABCMeta

	@abc.abstractmethod
	def write(self, input):
		pass

class LogFile(WriteFile):

	dt_str = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')

	def __init__(self, fName):
		self.target = open(fName, 'w')

	def write(self, input):
		self.target.write(self.dt_str + "\t")
		self.target.write(input + "\n")

class DelimFile(WriteFile):

	def __init__(self, fName, delim):
		self.target = csv.writer(open(fName, 'wb'))
		
	def write(self, input):
		self.target.writerow(input)