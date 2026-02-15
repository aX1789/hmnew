import requests

url =  "https://restcountries.com/v3.1/name/japan"
responce = requests.get(url)
content_dict = responce.json()



print("*** ІНФОРМАЦІЯ ПРО КРАЇНУ ***")
print(f"Official name: {content_dict[0]["name"]["official"]}")
print(f"Capital city: {content_dict[0]["capital"]}")
print(f"Flag: {content_dict[0]["flag"]}")
print(f"Population: {content_dict[0]["population"]}")
print(f"Geographic location: {content_dict[0]["latlng"][0]} широта та {content_dict[0]["latlng"][1]} довгота")

rd = "https://catfact.ninja/fact"
answer = requests.get(rd)
result1 = answer.json()
print(f"fun fact: {result1["fact"]}")

sp =  "https://zenquotes.io/api/random"
letitbe = requests.get(sp)
result2  = letitbe.json()
print(f"random fact: {result2[0]["q"]}")
