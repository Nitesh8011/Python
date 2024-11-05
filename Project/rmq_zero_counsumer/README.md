# RabbitMQ Queue Cleaner

This project provides a script to analyze RabbitMQ queues and delete any queues with zero consumers across all virtual hosts. It's useful for cleaning up unused queues to save resources and maintain a tidy RabbitMQ environment.

## Features
- Analyzes all queues in specified virtual hosts.
- Deletes queues with zero consumers.
- Configurable environment variables for easy customization.
- Designed to run both locally and in Docker.

## Requirements
- **Python 3.x**
- **RabbitMQ API** (HTTP API enabled on RabbitMQ)
- **Docker** (optional, for containerization)

## Environment Variables

The script requires certain environment variables for RabbitMQ access and configuration. 

| Variable      | Default               | Description                                         |
|---------------|-----------------------|-----------------------------------------------------|
| `BASE_PATH`   | `http://localhost:43853` | Base URL for RabbitMQ API.                      |
| `USERNAME`    | `guest`               | Username for RabbitMQ API authentication.           |
| `PASSWORD`    | `guest`               | Password for RabbitMQ API authentication.           |
| `TOPIC_QUEUES`| `Queue names`         | List of topic queues to analyze using regex matching. |

## Usage

### Running Locally

1. **Install Dependencies**:
   Install the required Python libraries with:
   ```bash
   pip install requests art