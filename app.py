import streamlit as st
from PIL import Image
import os

st.set_page_config(page_title="Inventory App", layout="centered")
welcome_image_path = "shawn3786/my-task/wellcome.jpg"
img = Image.open(welcome_image_path)
st.image(img, caption="Let's get started!", use_column_width=True)


