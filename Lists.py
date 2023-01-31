nums = [87, 45, 39, 75]

# accessing elements of list
print(nums[0])
print(nums[3])
print(nums[1:])
print(nums[-1])

#inserting an element at index 1
nums.insert(1,10)
print(nums)

#inserting an element at end
nums.append(99)
print(nums)

#inserting multiple value to list
nums.extend([11,22,33,44,55])
print(nums)
# returns the number of occurences of an element
print(nums.count(99))

#returns the index of an element
print(nums.index(99))

#to remove an element
nums.remove(10)
print(nums)

#removes the element with the given index value
nums.pop(0)
print(nums)

#removes the last element
nums.pop()

#list can have elements of any type
newlist=[nums,'shanu']
print(newlist)

nums.sort()
print(nums)
nums.reverse()
print(nums)

#returns the minimum and max of the list
print(min(nums))
print(max(nums))

#print(min(newlist)) #'<' not supported between instances of 'str' and 'list'

#sum of all numbers of the list
print(sum(nums))