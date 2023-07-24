from flask import request, jsonify
from flask_jwt_extended import get_jwt_identity, jwt_required
import requests
from . import bp as api
from app.models import Pokemon, User


@api.route("/get_pokemon/<string:pokemon_name>")
def get_pokemon(pokemon_name):
    base_url = "https://pokeapi.co/api/v2/pokemon/"
    url = f"{base_url}{pokemon_name.lower()}"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        pokemon_data = response.json()
        # Process the data as needed and return it to the user
        return jsonify(pokemon_data)
    else:
        return f"Error: {response.status_code}"
    

from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Replace with your own PokeAPI URL
POKEAPI_URL = "https://pokeapi.co/api/v2/pokemon"

@api.route('/add_pokemon', methods=['POST'])
def add_pokemon():
    # Get the data sent by the client
    data = request.get_json()
    if not data:
        return jsonify({"message": "No data provided."}), 400

    # Extract relevant data for the new Pokemon
    name = data.get('name')
    types = data.get('types', [])
    weight = data.get('weight', 0)
    height = data.get('height', 0)

    # Prepare the payload for the PokeAPI call
    payload = {
        "name": name,
        "types": types,
        "weight": weight,
        "height": height
    }

    # Make the PokeAPI call to simulate adding a new Pokemon
    response = requests.post(POKEAPI_URL, json=payload)

    if response.status_code == 201:
        return jsonify({"message": "Pokemon added successfully!"}), 201
    else:
        return jsonify({"message": "Failed to add the Pokemon."}), 500

if __name__ == '__main__':
    app.run(debug=True)

    
