# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

# simple tuple
# fruit_tuple = ('Apples', 'Oranges', 'Banana', 'Grapes')

# using constructor
fruit_tuple = tuple(('Apples', 'Oranges', 'Banana', 'Grapes'))

# print(fruit_tuple)
# print(len(fruit_tuple))

# print single value
# print(fruit_tuple[2])

# cannot change value
# fruit_tuple[2] = 'Mangoes'
# print(fruit_tuple)

# tuples with one value should have trailing comma
fruit_tuple_two = ('Mangoes', )

# del fruit_tuple_two

# print(fruit_tuple_two)
 


# A Set is a collection which is unordered and unindex. No duplicate members.

# create set
fruit_set = {'Apple', 'Orange', 'Mango'}
print(fruit_set)

# check if in set
print('Apple' in fruit_set)

# add to set
fruit_set.add('Grape')

# remove to set
fruit_set.remove('Apple')

print(fruit_set)

# clear set
fruit_set.clear()

# delete set
# del fruit_set

print(fruit_set)