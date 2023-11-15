import streamlit
[theme]
primaryColor="#F63366"
backgroundColor="#FFFFFF"
secondaryBackgroundColor="#F0F2F6"
textColor="#262730"
font="sans serif"

#streamlit.markdown("<h1 style='text-align: center; color: grey;'>RAYA</h1>",unsafe_allow_html=True)
#image = Image.open('https://unsplash.com/photos/assorted-sliced-citrus-fruits-on-brown-wooden-chopping-board-1CsaVdwfIew')
#streamlit.image(image, caption='Sunrise by the mountains')
logo=streamlit.image("https://assets.mofoprod.net/network/images/Raya_fbtlwo_FMQwLtk.original.jpg",width=200)

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


