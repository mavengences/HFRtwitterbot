import requests
import json

# Define the API endpoint and your API key
OPENAI_API_BASE = "https://api.endpoints.anyscale.com/v1"
OPENAI_API_KEY = "esecret_fxc1jyx5upy14ty93j93hbuvt9"
resortName='Mammoth Mountain, CA'

# Define the API endpoint URL
url = "https://www.hfrweather.com/hfrapi/pullSnowForecastsFree"

# Make a POST request
snowOutput = requests.post(url)

# Check if the request was successful (status code 200)
if snowOutput.status_code == 200:
    # Print the response content
    print("Response Content:")
    #print(snowOutput.text)
else:
    # If the request was not successful, print an error message
    print(f"Request failed with status code {snowOutput.status_code}")
    
dictionaryResorts=eval(snowOutput.text)


inputData=dictionaryResorts[resortName]

# Define the data payload
data = {
    "model": "codellama/CodeLlama-34b-Instruct-hf",
    "messages": [{"role": "system", "content": "Here is the weather forecasts for "+str(resortName)+": "+str(inputData)+" make this sound like a meterologist and limit it to 280 characters"}, {"role": "user", "content": "How is the weather over the next 5 days at "+str(resortName)+"?"}],
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
