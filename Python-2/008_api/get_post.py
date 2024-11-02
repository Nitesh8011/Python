import requests

data={
    'userid': 1,
    'title': 'foo',
    'body': 'bar'
}
url = 'https://jsonplaceholder.typicode.com/posts'

response = requests.post(url, json=data)

if response.status_code == 201:
    print(f'Success! New post added with ID {response.json()["id"]}')
else:
    print(f'Error: {response.status_code}')

# user_id = input("Enter the input you want to get: ")
id = f'https://jsonplaceholder.typicode.com/posts/{response.json()["id"]}'

# print(id)

response = requests.get(id)

if response.status_code == 200:
    print(response.json())
else:
    print('Error: ',response.status_code)