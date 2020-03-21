# service-initializer-base-docker

Base Docker image for [Service Initializer](https://github.com/piotr-kalanski/service-initializer) tasks implemented using Docker.

# Run task using Docker image

    docker run -it --rm service-initializer-base-docker --name service_name --description service_description --parameters "{'param1':'value1','param2':'value2'}"

# Extending image

To create custom Docker image for new Task you need to provide:
- Dockerfile
- task.py with run_task method
- optionally install new python packages

## Dockerfile format for custom task

```
FROM piotrkalanski/service-initializer-base-docker

COPY task.py .

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
```

## task.py

You have to implement business logic for you custom task in *run_task* function:

```python
def run_task(name: str, description: str, parameters: dict):
    # place your code here
```
Meaning of input parameters:
- name - service name
- description - service description
- parameters - custom parameters to initialize service
