import yaml

# to load single file
with open('student.yaml','r') as file:
    yaml_data = yaml.load(file, Loader=yaml.FullLoader)

print(yaml_data)


yaml_string = """
name: John
age: 30
---
name: Alice
age: 25
"""

# to load multiple file

yaml_data = yaml.load_all(yaml_string, Loader=yaml.FullLoader)

for doc in yaml_data:
    print(doc)