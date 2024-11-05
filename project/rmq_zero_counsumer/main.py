import requests
import os
from art import *

base_url = os.environ.get('BASE_URL','http://localhost:15672')
username = os.environ.get('USERNAME','guest')
password = os.environ.get('PASSWORD','guest')
deletion_queue = os.environ.get('TOPIC_QUEUES','queue_one','queue_two','queue_three')


def delete_unused_queue(queue_name, vhost_name):
    # Deletes a queue if it has no consumers
    print(f'Queue found for deletionin vhost {vhost_name}: {queue_name}')
    url = f'{base_url}/api/queues/{vhost_name}/{queue_name}'
    response = requests.delete(url, auth=(username, password), verify=False)

    if response.status_code == 204:
        print(f'Succesfully delete {queue_name} from {vhost_name}')
    else:
        print(f'Failed to delete {queue_name} from {vhost_name}')


def fetch_hosts():
    # Fetches all virtual hosts
    url = f'{base_url}/api/vhosts'
    response = requests.get(url, auth=(username, password), verify=False)
    response.raise_for_status()
    return response.json()


def fetch_queues(vhost_name):
    # Fetches all Queue
    url = f'{base_url}/api/queues/{vhost_name}?name={delete_unused_queue}&use_regex=true&pagination=false'
    response = requests.get(url, auth=(username, password), verify=False)
    response.raise_for_status()
    return response.json()


def analyze_and_queue_delete(vhost_name):
    # Queue analyzes and deletion
    print(f'Analyzing queue in vhost: {vhost_name}')
    queues = fetch_queues(vhost_name)

    for queue in queues:
        queue_name = queue['name']
        consumer = queue['consumers']
        if consumer == 0:
            delete_unused_queue(queue_name, vhost_name)


def main():
    print(text2art("RabbitMQ Queue Cleanup"))

    if not all([base_url, username, password, deletion_queue]):
        print('Missing or empty environaments variable(s)')
        return
    
    try:
        vhosts = fetch_hosts()
        for vhost in vhosts:
            vhost_name = vhost['name']
            analyze_and_queue_delete(vhost_name)

    except requests.exceptions.RequestException as e:
        print(f'rror while fetching vhosts or queue: {e}')

    
if __name__ == "__main__":
    main()