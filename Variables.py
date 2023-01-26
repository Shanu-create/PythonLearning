# No need to specify the type of variable, it automatically takes it when a value is assigned
x = 8
print(x)

print(x + 13)

# print(abc) #error:name 'abc' is not defined

# _ (understore takes the value of prev output)

name = 'youtube'
print(name)
# print(name ' is playing') # throws error
print(name + ' is playing')
print(name[0])
print(len(name))
# print(name[8]) # IndexError: string index out of range
print(name[6])
print(name[0:3])  # start index and end index minus 1
print(name[0:])  # start from 0,until end of string
print(name[:6])  # start from begining of string and end till 6-1
print(name[-1])  # last character of string
print(name[-6:-1])
print(name[3:10])  # no error ,display till end

# changing string
# name[0:3]='my' #'str' object does not support item assignment
# strings in python are immutable
print('my ' + name[3:])
