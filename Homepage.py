
# import module
import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="AI Project",
)

st.title("AI Intern Project")
img = Image.open("images/image.png")
st.image(img, width=600)

