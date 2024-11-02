import json

data = {'name': 'Nitesh', 'age': 24, 'city': 'Delhi'}

data['country'] = 'India'
data['age'] = 25

with open('output.json','w') as file:
    json.dump(data, file)

with open('output.json','r') as file:
    abc = json.load(file)

print(abc)
