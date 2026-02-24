import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Carregando os dados
url = "https://raw.githubusercontent.com/acidBits/Hello_world_app/refs/heads/main/movies.csv"
df = pd.read_csv(url)

df['generos'] = df['generos'].fillna("")

# Inicializando o vetorizador
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df['generos'])

# Tratando os gêneros: separando por vírgula e limpando espaços
generos_series = df['generos'].dropna().apply(lambda x: [g.strip() for g in x.split(',')])

# Achata a lista e extrai os únicos
generos_unicos = sorted(set(g for sublist in generos_series for g in sublist))
generos_unicos.insert(0, "")

#-------------------------------------------------------------------------------
# Função de Recomendação
def recomendar_por_genero(generos_usuario, df, vectorizer, X):
    # Vetor do gênero informado pelo usuário
    genero_vetor = vectorizer.transform([generos_usuario])

    # Calculando similaridade entre o input e os filmes
    similaridade = cosine_similarity(genero_vetor, X)[0]

    # Ordenando os filmes com maior similaridade
    df['similaridade'] = similaridade
    recomendacoes = df.sort_values(by=['similaridade','pontuacao'], ascending=False).head()

    return recomendacoes[['filme','pontuacao','ano','generos','similaridade']].reset_index(drop=True)

#-------------------------------------------------------------------------------
# Interface Streamlit
st.title("🎬 Recomendador de Filmes por Gênero")

col1, col2, col3 = st.columns(3)
with col1:
    genero1 = st.selectbox("Gênero 1", generos_unicos, key="g1")
with col2:
    genero2 = st.selectbox("Gênero 2", generos_unicos, key="g2")
with col3:
    genero3 = st.selectbox("Gênero 3", generos_unicos, key="g3")

# Gêneros selecionados
generos_escolhidos = [g for g in [genero1, genero2, genero3] if g]
entrada_usuario = ", ".join(generos_escolhidos)

# Botão de pesquisa
if st.button("🔍 Pesquisar"):
    recomendacoes = recomendar_por_genero(entrada_usuario, df, vectorizer, X)
    st.subheader("Filmes recomendados:")
    st.dataframe(recomendacoes, hide_index=True)
