import requests
import json

# Kubernetes API URL and other configurations
api_url = 'https://your-kubernetes-api-server-url/api/v1'  # Replace with your API server URL
token = 'your_bearer_token'  # Replace with your authentication token

# Kubernetes or your API headers (use bearer token for authentication)
headers = {
    'Authorization': f'Bearer {token}',
    'Content-Type': 'application/json',
    'Accept': 'application/json'
}

# Sample GET request to list namespaces
def get_namespaces():
    url = f"{api_url}/namespaces"
    try:
        response = requests.get(url, headers=headers, verify=False)  # 'verify=False' to skip SSL verification
        response.raise_for_status()  # Check for errors
        return response.json()  # Parse JSON response
    except requests.exceptions.RequestException as e:
        print(f"Error fetching namespaces: {e}")
        return None

# Sample POST request to create a pod (example)
def create_pod():
    url = f"{api_url}/namespaces/default/pods"
    pod_manifest = {
        "apiVersion": "v1",
        "kind": "Pod",
        "metadata": {
            "name": "example-pod"
        },
        "spec": {
            "containers": [
                {
                    "name": "nginx",
                    "image": "nginx:latest",
                    "ports": [{"containerPort": 80}]
                }
            ]
        }
    }

    try:
        response = requests.post(url, headers=headers, data=json.dumps(pod_manifest), verify=False)
        response.raise_for_status()  # Check for errors
        return response.json()  # Pod creation result
    except requests.exceptions.RequestException as e:
        print(f"Error creating pod: {e}")
        return None

# Sample PUT request
