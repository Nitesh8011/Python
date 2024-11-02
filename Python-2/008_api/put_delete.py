import requests

url = 'https://jsonplaceholder.typicode.com/posts/1'

data = {
    'title' : 'quest',
    'body' : 'answer'
}

response = requests.put(url, json=data)

if response.status_code == 200:
    print(f"Success post updated {response.json()}")
else:
    print(f"Error {response.status_code()}")

response = requests.delete(url)

if response.status_code == 200:
    print(f"Success deleted")
else:
    print(f"Error {response.status_code()}")