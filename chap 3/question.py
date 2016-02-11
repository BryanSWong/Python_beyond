'''
This assignment was to build a class called MaxSizeList that takes
a nuber that represents the max size of the list will return after 
such only a set number of elemetns will be returned.
'''

from assignments import MaxSizeList

a = MaxSizeList(3)
b = MaxSizeList(1)

a.push("hey")
a.push("hi")
a.push("let's")
a.push("go")

b.push("hey")
b.push("hi")
b.push("let's")
b.push("go")

print(a.get_list()) # results should be ["hi", "let's", "go"]
print(b.get_list()) # results should be ["go"]