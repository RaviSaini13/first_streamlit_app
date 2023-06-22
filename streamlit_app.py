import streamlit

streamlit.title('Hello World ! First Streamlit App')
streamlit.header('Application Menu')
streamlit.text('Learn Snowflake')
streamlit.text('Create GitHub Account')
streamlit.text('Create Streamlit Account through GitHub')
streamlit.text('Provide Access to Streamlit')
streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega3 and Oatmeal')
streamlit.text('🥗 Kale, Spinach and Rocket Smoothie')
streamlit.text('🥑🍞 Avocado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas as pd
my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
# Lets put some picklist to choose the fruits
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
streamlit.dataframe(my_fruit_list)
