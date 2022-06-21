import requests
import os

response = requests.get("https://jsonplaceholder.typicode.com/posts/1")

# response [200] para indicar que fue exitoso:
#print (response) 

#de tipo response:
#print (type(response))

#me da todo el codigo entre {}. Esto es un strig común y corriente
print(response.text)
print(type(response.text))
print("=" * 50)
print("\n")
#con mejor formato y de tipo diccionario
print(response.json())
print(type(response.json()))
