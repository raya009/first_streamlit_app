import streamlit


#streamlit.markdown("<h1 style='text-align: center; color: grey;'>RAYA</h1>",unsafe_allow_html=True)
#image = Image.open('https://unsplash.com/photos/assorted-sliced-citrus-fruits-on-brown-wooden-chopping-board-1CsaVdwfIew')
#streamlit.image(image, caption='Sunrise by the mountains')
logo=streamlit.image("data:image/png;base64,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",width=100)

#logo=streamlit.image("https://images.unsplash.com/photo-1511688878353-3a2f5be94cd7?q=80&w=1974&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",width=200)


streamlit.title('My Parents New Healthy Diner!!!!')
streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avacado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
#streamlit.dataframe(my_fruit_list)
my_fruit_list = my_fruit_list.set_index('Fruit')
#Let's put a pick list here so they can pick the fruit they want to include
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
#display the table on page
streamlit.dataframe(fruits_to_show)

# New section to display fruityvice api response 
import requests
streamlit.header("Fruityvice Fruit Advice!")
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response)
