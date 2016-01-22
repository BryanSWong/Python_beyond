'''
this assignment require you to write the three classes
WriteFile, LogFile, and DelimFile and have LogFile and 
DelimFile inherit from WriteFile and make WriteFile an 
abstract class. and then make the following code work.
'''

from assignment2 import LogFile, DelimFile

log = LogFile('log.txt')
c = DelimFile('text.csv', ',')

log.write('this is a log message')
log.write('this is another log message')

c.write(['a', 'b', 'c', 'd'])
c.write(['1', '2', '3', '4'])