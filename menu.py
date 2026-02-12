import streamlit as st
import streamlit.components.v1 as components

# Configuración estética
st.set_page_config(page_title="Consola de Gestión", page_icon="🖥️", layout="wide")

st.markdown("<h1 style='text-align: center;'>🚀 Panel de Control Central</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Selecciona la herramienta que deseas abrir</p>", unsafe_allow_html=True)
st.write("---")

# Estilo de botones grandes y centrados
st.markdown("""
    <style>
    div.stButton > button:first-child {
        height: 150px;
        width: 100%;
        font-size: 28px;
        font-weight: bold;
        border-radius: 20px;
        background-color: #1f77b4;
        color: white;
        transition: 0.3s;
    }
    div.stButton > button:hover {
        background-color: #2e86c1;
        transform: scale(1.02);
    }
    </style>
    """, unsafe_allow_html=True)

# Función para redirigir
def redirigir(url):
    js = f"window.open('{url}')"
    components.html(f"<script>{js}</script>", height=0)

# Crear cuadrícula de 2x2 para los botones
col1, col2 = st.columns(2)

with col1:
    if st.button("📄 PEMA"):
        redirigir("http://10.162.130.164:7777")
    
    if st.button("📂 INVENTARIO"):
        redirigir("http://10.162.130.164:8501")

with col2:
    if st.button("🧾 FACTUBAM"):
        redirigir("http://10.162.130.164:8502")
    
    if st.button("📊 RPT (ADJUN)"):
        redirigir("http://10.162.130.164:8503")

st.write("---")
st.caption("Conectado al nodo Proxmox: 10.162.130.164")