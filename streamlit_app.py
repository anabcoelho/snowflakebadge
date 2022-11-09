import streamlit as sl
import pandas as pd
import requests as req
import snowflake.connector


sl.title('O jantar po')

sl.header('piu!')
sl.text('🥣 Qual o cereal favorito do vampiro? A veia')
sl.text('🥗 Qual a vitamina mais engraçada? A vitamina KKKKKKKKKKKK')
sl.text('🐔 Ovin ou a galin')
sl.text('''Duas formigas se encontraram e pararam para conversar:
- Oi, qual é o seu nome?
- Fu.
- Fu o quê?
- Fu Miga!''')

sl.header('🥝🍇🍌🥭 boracozinhar 🥝🍇🍌🥭')

lista_fruta = pd.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')

#mudando o index
lista_fruta = lista_fruta.set_index('Fruit')

# colocar um filtrozin
meufiltro = sl.multiselect("escolhe a fruta:", list(lista_fruta.index),['Avocado','Strawberries'])

mostra_pramim = lista_fruta.loc[meufiltro]
# Display the table on the page.

sl.dataframe(mostra_pramim)


fruityvice_response = req.get("https://fruityvice.com/api/fruit/watermelon")
sl.header("Fruityvice Fruit Advice!")

fruit_choice = sl.text_input('What fruit would you like information about?','Kiwi')
sl.write('The user entered ', fruit_choice)
#sl.text(fruityvice_response.json() #só escreve o json

# write your own comment -what does the next line do? 
fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
# uma tabela ne
sl.dataframe(fruityvice_normalized)


my_cnx = snowflake.connector.connect(**sl.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from fruit_load_list")
my_data_rows = my_cur.fetchall()

sl.header('A lista de fruta tem:')


sl.dataframe(my_data_rows)


fruit_choice = sl.text_input('What fruit would you like information about?','Jackfruit')
insert_row_snowflake(fruit_choice)

def insert_row_snowflake(new_fruit):
  with my_cnx.cursor() as my_cur:
    my_cur.execute(f"insert into fruit_load_list values ('{new_fruit}')")
    return "Thanks for adding " + new_fruit



