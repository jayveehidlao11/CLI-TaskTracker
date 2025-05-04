import json

data = {
    "name": "John",
    "age": 30,
    "city": "New York",
    'ASD': 'asd'
}

with open('output.json', 'w') as file:
    json.dump(data, file, indent=4)  # indent for pretty printing