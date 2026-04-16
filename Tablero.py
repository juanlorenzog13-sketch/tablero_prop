import streamlit as st
from streamlit_drawable_canvas import st_canvas

# ---------- CONFIG ----------
st.set_page_config(page_title="Tablero Pink", layout="wide")

# ---------- CUSTOM CSS (PINK THEME) ----------
st.markdown("""
<style>
/* Background */
.stApp {
    background: linear-gradient(135deg, #ffe4f0, #ffd1e6);
}

/* Title */
h1 {
    text-align: center;
    color: #ff2e88;
    font-weight: 800;
    letter-spacing: 1px;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: #fff0f6;
    border-right: 2px solid #ffc2dd;
}

/* Sidebar titles */
section[data-testid="stSidebar"] h2, 
section[data-testid="stSidebar"] h3 {
    color: #d63384;
}

/* Sliders */
.stSlider > div {
    color: #d63384;
}

/* Selectbox */
div[data-baseweb="select"] {
    border-radius: 10px;
    border: 2px solid #ff99cc;
}

/* Color pickers */
input[type="color"] {
    border-radius: 50%;
    border: none;
    width: 50px;
    height: 50px;
}

/* Canvas container */
.css-1kyxreq, .stCanvas {
    border-radius: 20px;
    border: 3px solid #ff99cc;
    box-shadow: 0px 10px 30px rgba(255, 0, 128, 0.2);
    padding: 10px;
    background: white;
}

/* Section headers */
h2, h3 {
    color: #ff4da6;
}
</style>
""", unsafe_allow_html=True)

# ---------- TITLE ----------
st.title("💗 Tablero de Dibujo")

# ---------- SIDEBAR ----------
with st.sidebar:
    st.subheader("🎨 Propiedades")

    st.markdown("### 📐 Dimensiones")
    canvas_width = st.slider("Ancho", 300, 700, 500, 50)
    canvas_height = st.slider("Alto", 200, 600, 300, 50)

    st.markdown("### ✏️ Herramienta")
    drawing_mode = st.selectbox(
        "Modo de dibujo",
        ("freedraw", "line", "rect", "circle", "transform", "polygon", "point"),
    )

    st.markdown("### 🖌️ Estilo")
    stroke_width = st.slider('Grosor de línea', 1, 30, 15)
    stroke_color = st.color_picker("Color de trazo", "#ff2e88")

    st.markdown("### 🧱 Fondo")
    bg_color = st.color_picker("Color de fondo", "#ffffff")

# ---------- MAIN CANVAS ----------
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    canvas_result = st_canvas(
        fill_color="rgba(255, 105, 180, 0.3)",  # pink fill
        stroke_width=stroke_width,
        stroke_color=stroke_color,
        background_color=bg_color,
        height=canvas_height,
        width=canvas_width,
        drawing_mode=drawing_mode,
        key=f"canvas_{canvas_width}_{canvas_height}",
    )

# ---------- FOOTER ----------
st.markdown(
    "<p style='text-align:center; color:#ff4da6; margin-top:20px;'>Hecho con estilo 💅</p>",
    unsafe_allow_html=True
)
