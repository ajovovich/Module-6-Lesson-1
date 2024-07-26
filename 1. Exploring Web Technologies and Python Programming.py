#Task 1:Setting Up a Python Virtual Environment and Installing Packages
import requests 
import json

response = requests.get('https://pokeapi.co/api/v2/pokemon/pikachu')
json_data = response.text

#Task 2: Fetching Data from the Pokémon API

pikachu_data = json.loads(json_data)

print(pikachu_data['name'])
print(pikachu_data['abilities'])

#Task 3: Analyzing and Displaying Data

def fetch_pokemon_data(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
    response = requests.get(url)
    data = response.json()
    return data

def calculate_average_weight(pokemon_list):
    total_weight = 0
    for pokemon in pokemon_list:
        total_weight += pokemon['weight']
    return total_weight / len(pokemon_list)

pokemon_names = ["pikachu", "bulbasaur", "charmander"]
pokemon_data = []

for name in pokemon_names:
    data = fetch_pokemon_data(name)
    if data:
        pokemon_data.append(data)

average_weight = calculate_average_weight(pokemon_data)

for pokemon in pokemon_data:
    print(f'Name: {pokemon['name']}')
    abilities = [ability['ability']['name'] for ability in pokemon['abilities']]
    print(f"Abilities: {','.join(abilities)}")
    print(f"Weight: {pokemon['weight']}")

print(f'Average weight: {average_weight}')