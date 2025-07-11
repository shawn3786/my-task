import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import os
image_path = "wellcome.jpg"
img = Image.open(image_path).convert("RGBA")  
draw = ImageDraw.Draw(img)

font = ImageFont.load_default()
text = "Welcome to Inventory App"
text_position = (200, 30)  # (x, y)

draw.text(text_position, text, fill="black", font=font)
st.image(img, use_column_width=True)
