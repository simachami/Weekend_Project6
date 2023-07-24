from flask import render_template, redirect, flash, url_for, g, jsonify
from flask_login import current_user, login_required
import requests
from app import app
from app.forms import PokemonForm, UserSearchForm
from app.models import User, Pokemon
from . import bp


@app.before_request
def before_request():
    g.search_form = UserSearchForm()
    g.poke_form = PokemonForm()


@bp.post('/post')
def post():
    if g.poke_form.validate_on_submit():
        #If something was typed in, try to use that value to get a pokeapi response
        base_url = "https://pokeapi.co/api/v2/pokemon/"
        url = f"{base_url}{g.poke_form.name.data.lower()}"
        
        response = requests.get(url)
        
        if response.status_code == 200:
            pokemon_data = response.json()

            # Extract relevant data for the new Pokemon
            name = pokemon_data.get('name')
            weight = pokemon_data.get('weight', 0)
            height = pokemon_data.get('height', 0)

            # Prepare the payload for the PokeAPI call
            payload = {
                "name": name,
                "weight": weight,
                "height": height
            }

        else:
            return {"message": "Failed to add the Pokemon."}, response.status_code

        #test prints to verify data
        print(payload)
        print(payload['height'])
        
        #TODO - update the post = Pokemon to also take the payload['height'] and payload['weight']

        post = Pokemon(name=g.poke_form.name.data, height = payload['height'] , weight=payload['weight'], user_id = current_user.user_id)
        post.commit()
        flash('Pokemon added', category='success')
    return redirect(url_for('social.profile', username = current_user.username))


@bp.route('/profile/<username>')
@login_required
def profile(username):
    user = User.query.filter_by(username=username).first()
    if user:
        pokemons = user.pokemons
        return render_template('profile.jinja', username=username, pokemons=pokemons)
    else:
        flash(f'User: {username} is not valid!', category='warning')
        return redirect(url_for('main.home'))
    

# @bp.post('user-search')
# def user_search():
#     return redirect(url_for('social.profile', username=g.search_form.username.data))


@bp.post('user-search')
def user_search():
    pokemon = Pokemon.query.filter_by(user_id = current_user.user_id, name=g.search_form.username.data).first()
    if not pokemon:
        return {"message": "Failed to find Pokemon. Please try again!"}
    print(pokemon)
    pokemon.delete()
    
    flash(message='Pokemon removed!', category='success')
    return redirect(url_for('social.profile', username = current_user.username))
