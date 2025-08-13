import requests

response = requests.get('https://api.github.com')
print(f"GitHub API status: {response.status_code}")
print(f"Response content: {response.json()}") 
print("Request completed successfully.")