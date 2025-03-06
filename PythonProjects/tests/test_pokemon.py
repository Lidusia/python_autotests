import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '2c3f8d9af4ef8e79cc8cf2cda51ca1dd'
HEADER = {'Content-Type': 'application/json', 'trainer_token':TOKEN}
TRAINER_ID = '22793'

def test_status_code():
    response = requests.get(url=f'{URL}/trainers', headers = HEADER)
    assert response.status_code == 200

def test_trainer_name():
    response_get = requests.get(url = f'{URL}/me', headers = HEADER)
    assert response_get.json()["data"][0]["trainer_name"] == 'Шрекер'



def test_part_of_response():
    response_get = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID})
    assert response_get.json()["data"][0]['name'] == 'Масяндра'


@pytest.mark.parametrize('key, value', [('name', 'Масяндра'), ('trainer_id', TRAINER_ID), ('id', '252105')])
def test_parametrize(key, value):
    response_parametrize = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID})
    assert response_parametrize.json()["data"][0][key] == value