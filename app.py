import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import os
import time


st.session_state.page = "welcome"
st.session_state.start_time = time.time()
def go_to_menu():
    st.session_state.page = "menu"
if st.session_state.page == "welcome":

    image_path = "wellcome.jpg"
    img = Image.open(image_path).convert("RGBA")  
    draw = ImageDraw.Draw(img)
             
    font = ImageFont.load_default()
    text = "Welcome to Inventory App"
    text_position = (200, 30)  
            
    draw.text(text_position, text, fill="black", font=font)
    st.image(img, use_column_width=True)

    if time.time() - st.session_state.start_time > 3:
        go_to_menu()
elif st.session_state.page == "menu":
    st.title("📋 What would you like to do?")

    col1, col2 = st.columns(2)
    with col1:
        st.button("📦 Start Inventory")
        st.button("🚫 Add Finished Item")
    with col2:
        st.button("🛒 Make New Order")
        st.button("⚠️ Check Low Stock")



