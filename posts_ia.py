import streamlit as st
import os
from dotenv import load_dotenv
import google.generativeai as genai

# Carrega variáveis de ambiente do .env
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Configura a API do Gemini
genai.configure(api_key=api_key)

# Define o modelo fixo para evitar erro de depreciação
MODEL_NAME = "models/gemini-1.5-flash"  # você também pode usar "models/gemini-1.5-flash" |  "models/gemini-1.5-pro"

# Interface do app
st.title("Post-Pronto 🚀")
conteudo = st.text_input("Conteúdo")
publico = st.text_input("Público-alvo")
tom = st.selectbox("Tom de voz", ["Amigável", "Profissional", "Urgente", "Divertido"])

if st.button("Gerar"):
    prompt = f"""
Você é um copywriter especialista. Gere:
1) Um carrossel de Instagram. Me devolva a resposta em Markdown, separando claramente os slides do carrossel.
2) Uma descrição atrativa para o post.

Conteúdo: {conteudo}
Público-alvo: {publico}
Tom de voz: {tom}
"""

    try:
        with st.spinner("Gerando conteúdo com Gemini..."):
            model = genai.GenerativeModel(model_name=MODEL_NAME)
            response = model.generate_content(prompt)
            st.subheader("Carrossel Instagram")
            st.markdown(response.text)
    except Exception as e:
        st.error(f"Erro ao gerar resposta: {e}")
