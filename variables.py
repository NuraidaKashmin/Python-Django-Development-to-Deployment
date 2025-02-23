# A variable is a container for a value, which can be of various types

'''
This is a 
multiline comment
or docstring (used to define a functions purpose)
can be single or double quotes
'''

"""
VARIABLE RULES:
  - Variable names are case sensitive (name and NAME are different variables)
  - Must start with a letter or an underscore
  - Can have numbers but can not start with one
"""


#x = 1
#y = 2.5
# name = 'Brad'
# is_cool = True


x, y, name, is_cool = (1, 2.5, 'Brad', True)
print(x, y, name, is_cool)

x = str(x)
print(type(x))

y = int(y)
print(type(y))

z = float(y)
print(type(z))

print(x,y,z)