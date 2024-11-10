import streamlit as st
from scraper import extract_text
from translator import translate_article

st.title("Tradutor de Artigos")
st.write("Insira uma URL de artigo para extrair e traduzir o conteúdo para o português.")

# Campo de entrada para a URL
url = st.text_input("URL do artigo", "https://dev.to/dhanush9952/method-references-in-java-4690")

# Botão para iniciar a tradução
if st.button("Traduzir"):
    # Extrai o texto da URL fornecida
    text = extract_text(url)
    
    if text:
        # Traduz o artigo para o português
        artigo = translate_article(text, "português")
        st.write("Artigo Traduzido:")
        st.markdown(artigo)
    else:
        st.error("Falha ao extrair o texto da URL. Verifique se a URL está correta.")
