import json
import requests

response = requests.get("http://jsonplaceholder.typicode.com/todos")
todos = json.loads(response.text)


