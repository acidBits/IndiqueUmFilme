import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


col1, col2, col3 = st.columns(3)
with col1:
    genero1 = st.selectbox("Gênero 1", "", key="g1")
with col2:
    genero2 = st.selectbox("Gênero 2", "", key="g2")
with col3:
    genero3 = st.selectbox("Gênero 3","", key="g3")

# Gêneros selecionados
#generos_escolhidos = [g for g in [genero1, genero2, genero3] if g]
#entrada_usuario = ", ".join(generos_escolhidos)

# Recomendar filmes
if st.button("🔍 Pesquisar"):
    st.write("")



