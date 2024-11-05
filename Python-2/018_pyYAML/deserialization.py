import yaml

data = {'name': 'John', 'age': 30, 'city': 'New York'}

yaml_data = yaml.dump(data)
print(yaml_data)

# custom formatting
yaml_data = yaml.dump(data, default_flow_style= False)
print(yaml_data)