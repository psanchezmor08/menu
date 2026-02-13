import streamlit as st
import streamlit.components.v1 as components

# =====================================================
# CONFIGURACIÓN INICIAL
# =====================================================
# Se actualiza el icono de la página con la ruta exacta
st.set_page_config(
    page_title="Consola de Gestión", 
    page_icon="diseño/ada-icono (1).png",  # <--- Ruta del icono actualizada
    layout="wide"
)

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
    
    .main { padding: 2rem; }
    
    /* Ajuste de botones del panel central */
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
        box-shadow: 0 4px 6px rgba(0,0,0,0.1); /* Sombra para resaltar los botones */
    }
    div.stButton > button:hover {
        background-color: var(--verde-hover) !important;
        transform: scale(1.02);
        box-shadow: 0 6px 12px rgba(0,0,0,0.15);
    }
    </style>
    """
    st.markdown(estilo_css, unsafe_allow_html=True)

# Cargamos el CSS global
cargar_estilos_css()

# =====================================================
# INTERFAZ DE USUARIO
# =====================================================

# Colocamos la foto arriba del título, centrada en la pantalla
try:
    c1, c2, c3 = st.columns([1, 2, 1]) # La columna central es más ancha para la imagen
    with c2:
        st.image("diseño/ADA-vc-color (1).jpg", use_container_width=True)
except Exception:
    # Si por algún motivo no encuentra la ruta exacta, muestra un aviso
    st.warning("No se pudo cargar la imagen. Comprueba que la ruta 'diseño/ADA-vc-color (1).png' es correcta.")

# Títulos
st.markdown("<h1 style='text-align: center;'>🚀 Panel de Control Central</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Selecciona la herramienta que deseas abrir</p>", unsafe_allow_html=True)
st.write("---")

# Función para abrir los enlaces en una pestaña nueva
def redirigir(url):
    js = f"window.open('{url}', '_blank')"
    components.html(f"<script>{js}</script>", height=0)

# Crear cuadrícula para los botones (Añadido un pequeño espacio central para separar)
st.markdown("<br>", unsafe_allow_html=True)
col1, col_espacio, col2 = st.columns([1, 0.1, 1])

with col1:
    if st.button("📄 PEMA"):
        redirigir("http://10.162.130.164:7777")
        
    st.markdown("<br>", unsafe_allow_html=True) # Espacio vertical
    
    if st.button("📂 INVENTARIO"):
        redirigir("http://10.162.130.164:8501")

with col2:
    if st.button("🧾 FACTUBAM"):
        redirigir("http://10.162.130.164:8502")
        
    st.markdown("<br>", unsafe_allow_html=True) # Espacio vertical
    
    if st.button("📊 RPT (ADJUN)"):
        redirigir("http://10.162.130.164:8503")

st.markdown("<br>", unsafe_allow_html=True)
st.write("---")
st.caption("Conectado al nodo Proxmox: 10.162.130.164")

