import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import requests

st.set_page_config(page_title="Pokemon Explorer", page_icon=":zap:",  initial_sidebar_state="expanded")


st.title("Pokemon Explorer!")
st.write("**Welcome to the Pokemon Explorer app! Select a Pokemon from the slider below to explore its details.**")

def get_details(poke_number):
    try:
        url = f'https://pokeapi.co/api/v2/pokemon/{poke_number}/'
        response = requests.get(url)
        pokemon = response.json()
        sprite_url = pokemon['sprites']['front_default']
        sprite_url2 = pokemon['sprites']['front_shiny']
        sprite_url3 = pokemon['sprites']['back_shiny']
        cry_url = pokemon["cries"]["latest"]
        return pokemon['name'], pokemon['height'], pokemon['weight'], len(pokemon['moves']), sprite_url, sprite_url2, sprite_url3, cry_url
    except:
        return 'Error', np.NAN, np.NAN, np.NAN, np.NaN, np.NaN


pokemon_number = st.number_input("**Select a Pokemon:**", min_value=1, max_value=150)


with st.expander("**Select Sprite Type**"):
    tab_labels = ["Normal", "Shiny", "Back"]
    selected_tab = st.radio("", tab_labels)

name, height, weight, moves, sprite_url, sprite_url2, sprite_url3, cry_url = get_details(pokemon_number)
height *= 10 

height_data = pd.DataFrame( {'Pokemon': ['Weedle', name, 'victreebel'], 
                             'Heights': [3, height, 170]})

colors = ['gray', 'red', 'blue']


graph = sns.barplot(data = height_data,
                    x = 'Pokemon',
                    y = 'Heights',
                    palette = colors)


left_col, middle_col, cent_col, right_col = st.columns([10,7, 7,10])

with left_col:

    if selected_tab == "Normal":
        st.image(sprite_url, width=300, use_column_width=True)
 
    elif selected_tab == "Shiny":
        st.image(sprite_url2, width=300, use_column_width=True)

    elif selected_tab == "Back":
        st.image(sprite_url3, width=300, use_column_width=True)

with right_col:

    st.write(f'**Name:** {name.title()}')
    st.write(f'**Height:** {height} cm')
    st.write(f'**Weight:** {weight} kg')
    st.write(f'**Move Count:** {moves}')


#for audio of latest battle cry:
st.write(f'Pokemon Battle Cry:')
st.audio(cry_url)

st.pyplot(graph.figure)
