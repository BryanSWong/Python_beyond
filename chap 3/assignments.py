class MaxSizeList(object):
	# set the __init__ variables and values needed.
	def __init__(self, value):
		self.setLength = value
		self.the_list = []
	# create a push function as a setter for adding to the list
	# also to adjsut the lsit automatically when the limit is reached
	def push(self, str):
		# the minus one is account for the 0 start for lists
		if len(self.the_list) <= self.setLength-1:
			self.the_list.append(str)
		else:
			self.the_list.pop()
			self.the_list.append(str)
	# used to retrive the list after the pushes
	def get_list(self):
		return self.the_list