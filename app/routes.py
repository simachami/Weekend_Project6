from flask import render_template, jsonify
from app import app
import requests


@app.route("/get_pokemon/<string:pokemon_name>")
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

