import requests

BASE = "http://127.0.0.1:5000/"

response = requests.get(BASE+"people/Max Musterman/32/Max.Mustermann@smail.th-koeln.de/Male")

print(response.json())