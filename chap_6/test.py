"""
Usages:
./test.py (reads out entire dict list)
.test.py thiskey thisvalue (sets 'thiskey' and 'thisvalue' in dict)

"""

import sys
from assignment4 import ConfigDict

cd = ConfigDict('revanalysis.config')

#if 2 arguments on the command line set a key and value in object dict
if len(sys.argv) == 3:
	key = sys.argv[1]
	value = sys.argv[2]
	print('writing data: {0}, {1}'.format(key, value))
	cd[key] = value

#if 1 arg on the command line treat as a key and show value
elif len(sys.argv) == 2:
	print('reading a value')
	key = sys.argv[1]
	print('the value for {0} is {1}'.format(sys.argv[1], cd[key]))

#if no arg on the command show all keys
else:
	print('keys/values:')
	for key in cd.keys():
		print('	{0} = {1}'.format(key, cd[key]))
