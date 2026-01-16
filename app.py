import streamlit as st
import requests
import io
from PIL import Image

# Configuración visual de la página
st.set_page_config(page_title="AlohomoraIA", page_icon="🔑", layout="centered")

# Estilo CSS para que se vea mágico y oscuro
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    h1 { color: #FFD700; text-shadow: 2px 2px #4b0082; }
    .stButton>button { 
        background-color: #4b0082; color: white; border-radius: 20px;
        border: 2px solid #FFD700; width: 100%; font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center;'>🔑 AlohomoraIA</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #aaa;'><i>Desbloquea el arte cuántico con un hechizo</i></p>", unsafe_allow_html=True)

# --- CONFIGURACIÓN DE LA LLAVE ---
#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
API_TOKEN = "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"
API_URL = "https://api-inference.huggingface.co/models/black-forest-labs/FLUX.1-schnell"
headers = {"Authorization": f"Bearer {API_TOKEN}"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.content

# --- INTERFAZ DE USUARIO ---
with st.container():
    prompt = st.text_input("Escribe el secreto que deseas visualizar:", placeholder="Ej: Un fénix de cristal en el espacio...")
    
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        boton_hechizo = st.button("✨ ¡ALOHOMORA!")

if boton_hechizo:
    if prompt and API_TOKEN != "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":
        with st.spinner("Lanzando el encantamiento..."):
            # Master Prompt para darle el estilo único a tu marca
            master_prompt = f"AlohomoraIA style: {prompt}, magical atmosphere, cinematic lighting, hyper-detailed, golden sparkles, 8k"
            
            image_bytes = query({"inputs": master_prompt})
            
            try:
                image = Image.open(io.BytesIO(image_bytes))
                st.image(image, caption="Desbloqueado por AlohomoraIA", use_container_width=True)
                st.balloons()
            except:
                st.error("Error: El hechizo es demasiado débil. Revisa tu API Key o intenta más tarde.")
    else:
        st.warning("Asegúrate de escribir algo y de configurar tu Llave key.")

st.markdown("---")
st.caption("Hecho con magia y IA © 2026 AlohomoraIA")
