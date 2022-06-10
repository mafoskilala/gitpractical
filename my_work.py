Import streamlit as st

from PIL import img
img= Image.open("food Img.jpg")

st.image(img, width= 400)
