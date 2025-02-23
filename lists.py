# A List is a collection which is ordered and changeable. Allows duplicate members.

# numbers = [1,2,3,4,5,6]

# using a constructor
numbers = list((1,2,3,4,5,6))

fruits = ['Apples', 'Oranges', 'Banana', 'Grapes']

# print(type(numbers))

# get value
print(fruits[2])

# get len
print(len(fruits))

# append to list
fruits.append('Mangoes')
print(fruits)

# remove from list
fruits.remove('Grapes')
print(fruits)

# insert into position
fruits.insert(1, 'Pears')
print(fruits)

# remove from position
fruits.pop(3)
print(fruits)

# reverse list
fruits.reverse()
print(fruits)

# sort list
fruits.sort()
print(fruits)

# reverse sort
fruits.sort(reverse=True)
print(fruits)