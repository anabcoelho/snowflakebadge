import streamlit as sl
import pandas as pd
import requests as req
import snowflake.connector
from urllib.error import URLError


def insert_row_snowflake(new_fruit):
  with my_cnx.cursor() as my_cur:
    my_cur.execute(f"insert into fruit_load_list values ('{new_fruit}')")
    return "Thanks for adding " + new_fruit


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



sl.header("Fruityvice Fruit Advice!")

def get_fruityvice_data(this_fruit_choice):
  sl.write('The user entered ', this_fruit_choice)
  fruityvice_response = req.get("https://fruityvice.com/api/fruit/" + this_fruit_choice)
  fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
  return fruityvice_normalized

try:
  fruit_choice = sl.text_input('What fruit would you like information about?','Kiwi')
  if not fruit_choice:
      sl.error("Please select a fruit to get information")
  else:

    back_from_function = get_fruityvice_data(fruit_choice)
    sl.dataframe(back_from_function)
  
except:
  sl.error()
  


my_cnx = snowflake.connector.connect(**sl.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from fruit_load_list")
my_data_rows = my_cur.fetchall()

sl.header('A lista de fruta tem:')

def get_fruit_load_list():
  with my_cnx.cursor() as my_cur:
    my_cur.execute("select * from fruit_load_list")
    return my_cur.fetchall()

#adciona um botão
if streamlit.button('Get Fruit Load List'):
  my_cnx = snowflake.connector.connect(**sl.secrets["snowflake"])
  my_data_rows = get_fruit_load_list()
  my_cnx.close()
  sl.dataframe(my_data_rows)

  
 


fruit_choice = sl.text_input('What fruit would you like information about?','Jackfruit')
print(insert_row_snowflake(fruit_choice))

sl.stop()



