import streamlit as st
from pathlib import Path

st.markdown("## Manual :books: ")

with open("art.pdf", "rb") as pdf_file:
    PDFbyte = pdf_file.read()

section = "## Seleção da ERB e Receptor\n- Para definir a localização da ERB e do receptor, é necessário definí-las nos seguintes campos. Após digitar os campos, pressione enter"
st.markdown(section, unsafe_allow_html=True)
st.image('assets/origin_destiny.png')

section = "## Definição das Variáveis\n- Na barra esquerda, é possível entrar com os valores do modelo que servem de entrada para o modelo"
st.markdown(section, unsafe_allow_html=True)
st.image('assets/side_bar.png')

with st.sidebar:
    st.subheader("Faça o Download da ART aqui")
    st.download_button(label="Download ART",
                    data=PDFbyte,
                    file_name="art.pdf",
                    mime='application/octet-stream')
