import requests
import json

# Define the API endpoint and your API key
OPENAI_API_BASE = "https://api.endpoints.anyscale.com/v1"
OPENAI_API_KEY = "esecret_fxc1jyx5upy14ty93j93hbuvt9"

# Define the data payload
data = {
    "model": "codellama/CodeLlama-34b-Instruct-hf",
    "messages": [{"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": "Hello!"}],
    "temperature": 0.7
}

# Define headers
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {OPENAI_API_KEY}"
}

# Make the POST request
response = requests.post(f"{OPENAI_API_BASE}/chat/completions", data=json.dumps(data), headers=headers)

# Check for a successful response
if response.status_code == 200:
    result = response.json()
    print(result)
else:
    print(f"Request failed with status code {response.status_code}: {response.text}")
