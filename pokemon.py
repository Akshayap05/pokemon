import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import requests


st.title("Pokemon Explorer!")
st.write("Welcome to the Pokemon Explorer app! Select a Pokemon from the slider below to explore its details.")

def get_details(poke_number):
    try:
        url = f'https://pokeapi.co/api/v2/pokemon/{poke_number}/'
        response = requests.get(url)
        pokemon = response.json()
        sprite_url = pokemon['sprites']['front_default']
        return pokemon['name'], pokemon['height'], pokemon['weight'], len(pokemon['moves']), sprite_url
    except:
        return 'Error', np.NAN, np.NAN, np.NAN


#for audio of latest battle cry:
#st.audio(data, format="audio/wav", start_time=0, *, sample_rate=None)

pokemon_number = st.slider("Pick a Pokemon", 
                           min_value=1, 
                           max_value=150)

name, height, weight, moves, sprite_url = get_details(pokemon_number)
height *= 10 

st.write(f'Name: {name.title()}')
st.write(f'Height: {height} cm')
st.write(f'Weight: {weight} kg')
st.write(f'Move Count: {moves}')

if sprite_url:
    st.image(sprite_url, caption=name.title(), use_column_width=True)
else:
    st.write("Image not available for this Pokemon.")
