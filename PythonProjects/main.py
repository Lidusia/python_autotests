import requests


URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '2c3f8d9af4ef8e79cc8cf2cda51ca1dd'
HEADER = {'Content-Type': 'application/json', 'trainer_token':TOKEN}


body_create = {
    "name": "Масяндра",
    "photo_id": 182
}


body_name_change = {
    "pokemon_id": "252105",
    "name": "generate",
    "photo_id": 182
}

body_pokeball = {
    "pokemon_id": "252105"
}


response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)

message = response_create.json()['message']
print(message)

response_name_change = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_name_change)
print(response_name_change.text)

response_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_pokeball)
print(response_pokeball.text)

