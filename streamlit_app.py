import streamlit as st
import time 
from streamlit_extras.switch_page_button import switch_page 

st.set_page_config(page_title="Login | Meu App", page_icon="🔐")

usuarios = {
    "lilian": "1234",
    "admin": "admin123",
    "usuario1": "senha456"
}

st.sidebar.header("Área de Login")
usuario_input = st.sidebar.text_input("Usuário", placeholder="Digite seu nome de usuário")
senha_input = st.sidebar.text_input("Senha", placeholder="Digite sua senha", type="password")

if st.sidebar.button("Entrar"):
    if usuario_input in usuarios and usuarios[usuario_input] == senha_input:
        st.success(f"✅ Bem-vindo, {usuario_input}!")
        st.session_state["usuario_logado"] = usuario_input
    else:
        st.error("❌ Usuário ou senha incorretos!")

if "usuario_logado" in st.session_state:
    st.sidebar.success(f"🎉 Logado como {st.session_state['usuario_logado']}")
    st.write("📌 Agora você pode acessar as funcionalidades do app!")
else:
    st.warning("⚠️ Faça login para continuar.")
