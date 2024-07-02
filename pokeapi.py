import requests
import json

# JSON responses take the form of a dictionary

response = {
    "name": "Pikachu",
    "type": "electric",
    "base_experience": 112
}

print(response["base_experience"])

response = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu") # Request information about a certain pokemon

# json_data = response.text  # Testing things out
# print(json_data)
# data = json.loads(json_data)
# print(data)

poke_data = response.json()
# print(poke_data)

print(poke_data["name"].title()) # Pokemon name
print(poke_data["sprites"]["other"]["dream_world"]["front_default"])  # Default image
print(poke_data["types"][0]["type"]["name"]) # Pokemon type
print(poke_data["id"]) # pokemon id


def pokedex():
    pokemon = input("Which pokemon are you looking for? ")

    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon.lower()}")

    if response.status_code == 200:
        poke_data = response.json()

        poke_dict = {
            "name": poke_data["name"],
            "sprite": poke_data["sprites"]["other"]["dream_world"]["front_default"],
            "type": poke_data["types"][0]["type"]["name"],
            "id": poke_data["id"]
        }

        return poke_dict
    else:
        return "Bad response, try again!"

stuff = pokedex()

print(stuff)

# print(pokedex())

print(stuff["name"])