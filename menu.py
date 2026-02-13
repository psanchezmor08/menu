import streamlit as st
import streamlit.components.v1 as components

# =====================================================
# CONFIGURACIÓN INICIAL
# =====================================================
st.set_page_config(page_title="Panel de Gestión ADA", page_icon="diseño/logo-icono (1).png", layout="wide")

# =====================================================
# GESTIÓN DE CSS GLOBAL
# =====================================================
def cargar_estilos_css():
    estilo_css = """
    <style>
    :root {
        --verde-junta: #0b6e3c;
        --verde-hover: #158f4a;
        --verde-claro: #e7f6ed;
        --blanco: #ffffff;
        --gris-claro: #f4f6f9;
        --texto-oscuro: #1f2937;
    }
    .stApp { background-color: var(--blanco); color: var(--texto-oscuro); }
    header[data-testid="stHeader"] { background-color: var(--blanco); border-bottom: 4px solid var(--verde-junta); padding: 0.5rem; }
    header::after { display: none !important; }
    header img { max-height: 60px !important; object-fit: contain; }
    
    section[data-testid="stSidebar"] { background-color: var(--verde-junta); padding-top: 1rem; }
    section[data-testid="stSidebar"] * { color: var(--blanco) !important; font-size: 15px; }
    
    div[data-testid^="stKey-nav_"] button {
        all: unset; 
        width: 90% !important; 
        margin: 0 auto !important; 
        display: flex; 
        justify-content: center; 
        align-items: center;
        padding: 12px 0px; 
        margin-bottom: 8px !important; 
        border-radius: 6px; 
        cursor: pointer;
        font-weight: 500; 
        color: var(--blanco) !important; 
        background-color: rgba(255,255,255,0.1); 
        border: 1px solid rgba(255,255,255,0.2);
        transition: background 0.2s;
        box-sizing: border-box;
    }
    div[data-testid^="stKey-nav_"] button:hover { 
        background-color: var(--verde-hover); 
        border-color: var(--blanco);
    }
    
    .main { padding: 2rem; }
    
    /* Estilos generales para botones pequeños */
    .stButton > button {
        background-color: var(--verde-junta); color: var(--blanco); border-radius: 6px; border: none;
        padding: 0.5rem 1rem; font-weight: 600;
    }
    .stButton > button:hover { background-color: var(--verde-hover); }
    input, textarea { border-radius: 6px !important; }
    footer { visibility: hidden; }
    
    [data-testid="stVerticalBlockBorderWrapper"] {
        border: 2px solid #e0e0e0;
        border-radius: 10px;
        padding: 20px;
        background-color: #f9f9f9;
    }
    </style>
    """
    st.markdown(estilo_css, unsafe_allow_html=True)

# Cargamos el CSS global
cargar_estilos_css()

# =====================================================
# INTERFAZ DE USUARIO
# =====================================================
st.markdown("<h1 style='text-align: center;'>🚀 Panel de Control Central</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Selecciona la herramienta que deseas abrir</p>", unsafe_allow_html=True)
st.write("---")

# Estilo específico para sobreescribir los botones de este panel y hacerlos grandes (integrado con el tema verde)
st.markdown("""
    <style>
    div.stButton > button:first-child {
        height: 150px !important;
        width: 100% !important;
        font-size: 28px !important;
        font-weight: bold !important;
        border-radius: 20px !important;
        background-color: var(--verde-junta) !important;
        color: white !important;
        transition: 0.3s !important;
        border: none !important;
    }
    div.stButton > button:hover {
        background-color: var(--verde-hover) !important;
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



