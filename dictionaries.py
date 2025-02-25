# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

# simple dictionary
person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 28
}

# using a constructor
# person = dict(first_name = 'John', last_name = 'Doe', age = 28)

# access value
print(person['first_name'])
print(person.get('last_name'))

# add key/value
person['phone'] = '12342536436'

# get keys
print(person.keys())

# get values
print(person.items())

# make copy
person2 = person.copy()
person2['city'] = 'Japan'
print(person2)


# remove item
del(person['age'])
person2.pop('phone')

# clear 
person2.clear()


print(person2)
print(person)

# list of dictionary
people = [
    {'name': 'Ron', 'age': 20},
    {'name': 'Kon', 'age': 23},
    {'name': 'Bon', 'age': 22}
]

print(people)
print(people[1]['name'])