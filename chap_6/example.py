import sys

try:
	arg = sys.argv[1]
	num = int(arg)

except(IndexError, ValueError):
	exit('Enter an single number only please')

print "thanks for the int"