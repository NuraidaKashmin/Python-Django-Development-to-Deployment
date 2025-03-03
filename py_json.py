# JSON is commonly used with data APIS. Here how we can parse JSON into a Python dictionary


import json

# sample json

userJSON = '{"first_name":"John","last_name": "Doe", "age":20 }'

# parse to dictionary
user = json.loads(userJSON)

print(user)
print(user['first_name'])


car = {'make': 'Ford', 'model': 'Mustang', 'year': 1970}


carJSON = json.dumps(car)
print(carJSON)
