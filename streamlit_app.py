import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity 

# Carregando os dados
url = "https://raw.githubusercontent.com/acidBits/Hello_world_app/refs/heads/main/movies.csv"
df = pd.read_csv(url)

# Tratando os gêneros: separando por vírgula e limpando espaços
generos_series = df['generos'].dropna().apply(lambda x: [g.strip() for g in x.split(',')])

# Achata a lista e extrai os únicos
generos_unicos = sorted(set(g for sublist in generos_series for g in sublist))
generos_unicos.insert(0,"")


col1, col2, col3 = st.columns(3)
with col1:
    genero1 = st.selectbox("Gênero 1", generos_unicos, key="g1")
with col2:
    genero2 = st.selectbox("Gênero 2", generos_unicos, key="g2")
with col3:
    genero3 = st.selectbox("Gênero 3",generos_unicos, key="g3")

# Gêneros selecionados
generos_escolhidos = [g for g in [genero1, genero2, genero3] if g]
entrada_usuario = ", ".join(generos_escolhidos)

# Recomendar filmes
if st.button("🔍 Pesquisar"):
    st.write(entrada_usuario)



