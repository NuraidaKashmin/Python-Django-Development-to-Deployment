# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

name = 'Ron'
age = 30

# concatenate
print('Hello I am '+ name + 'I am '+ str(age)  )

# String Formatting

#arguments by position
print('{}, {}, {}'.format('a', 'b', 'c'))
print('{1}, {0}, {2}'.format('a', 'b', 'c'))

# arguments by name
print('My name is {name} and I am {age}'.format(name = name, age = age))

# F-Strings (only in 3.6+)
print(f'My name is {name} and I am {age}')



# String Methods
x = 'hEllo there world'
print(x.capitalize())
print(x.upper())
print(x.lower())
print(x.swapcase())
print(x.replace('world','everyone'))

sub = 'h'
print(x.count(sub))
print(x.startswith('hEllo'))
print(x.endswith('hello'))
print(x.find('E'))
print(x.split())
print(x.isalnum())
print(x.isalpha())
print(x.isnumeric())
