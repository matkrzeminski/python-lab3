import requests
from pprint import pprint


URL = "https://hp-api.herokuapp.com/api/characters"


response = requests.get(URL)

data = response.json()

# print(set([item.get("species") for item in data]))
# pprint([item for item in data if item.get("species") == "human"])

print("Wybierz postać:")
print("1. Postacie z określonym kolorem oczu? ")
print("2. Postacie z określonym gatunkiem? ")
option = input("Wybierz opcję: ")
if option == "1":
    eye_color = input("Podaj kolor oczu: ")
    pprint([item for item in data if item.get("eyeColour") == eye_color])
elif option == "2":
    species = input("Podaj gatunek: ")
    pprint([item for item in data if item.get("species") == species])
else:
    print("Nie ma takiej opcji")
