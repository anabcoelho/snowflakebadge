import streamlit as sl
import pandas as pd


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
