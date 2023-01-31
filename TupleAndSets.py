# List is mutable whereas tuples are immutable
tup = (1, 2, 3, 4, 5)
print(tup)

# accessing values of tuple
print(tup[0])

# changing values of tuple
# tup[0]=0 #'tuple' object does not support item assignment
print(tup[0])

# methods of tuple
print(tup.index(3))
print(tup.count(2))

# SETS=>collection of unique elements,doesnot support duplicate values
#set doesnot follow a specific sequence
s = {54, 73, 45, 876,29,84,73,64,88}
print(s)
print(s)

#cannot access elements of sets using index value
#print(s[3]) #TypeError: 'set' object does not support indexing

s.remove(73)
print(s)

