# get_data.py

import requests
import json

print("REQUESTING SOME DATA FROM THE INTERNET...")

request_url = "https://raw.githubusercontent.com/prof-rossetti/intro-to-python/master/data/products/1.json"
response = requests.get(request_url)
parsed_response1 = json.loads(response.text)
print(parsed_response1["name"])


request_url = "https://raw.githubusercontent.com/prof-rossetti/intro-to-python/master/data/products.json"
response = requests.get(request_url)
parsed_response2 = json.loads(response.text)
for p in parsed_response2:
    print(p["name"]), p["id"]

request_url = "https://raw.githubusercontent.com/prof-rossetti/intro-to-python/master/data/gradebook.json"
response = requests.get(request_url)
parsed_response3 = json.loads(response.text)

grades = []
students = parsed_response3["students"]
for x in students:
    grades.append(x["finalGrade"])

print(min(grades))
print(max(grades))


