import array as a

arr = a.array('i', [55, 47, 83, -9, 23])

for i in range(len(arr)):
    print(arr[i])
print('----------------------------------------')
#copying an array
newArr=a.array(arr.typecode,(a*a for a in arr))

for i in range(len(newArr)):
    print(newArr[i])

print('----------------------------------------')

#using while loop
i=0
while i<len(newArr):
    print(newArr[i])
    i+=1

# get elements of an array from user
userArr=a.array('i',[])
n=int(input('Enter the length of the array'))

for i in range(n):
    x=int(input('Enter the value'))
    userArr.append(x)

for i in range(n):
    print(userArr[i])

searchEle=int(input("Enter the search element"))
print(userArr.index(searchEle))