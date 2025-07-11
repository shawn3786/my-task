import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import os

if "page" not in st.session_state:
    st.session_state.page = "welcome"

if st.session_state.page == "welcome":

    image_path = "wellcome.jpg"
    img = Image.open(image_path).convert("RGBA")  
    draw = ImageDraw.Draw(img)
             
    font = ImageFont.load_default()
    text = "Welcome to Inventory App"
    text_position = (200, 30)  
            
    draw.text(text_position, text, fill="black", font=font)
    st.image(img, use_column_width=True)
     clicked = st.button(" ", key="fullscreen", help="Click anywhere", use_container_width=True)
    if clicked:
        st.session_state.page = "menu"
        st.rerun()

elif st.session_state.page == "menu":
        st.title("📋 What would you like to do?")

        col1, col2 = st.columns(2)
        with col1:
            st.button("📦 Start Inventory")
            st.button("🚫 Add Finished Item")
        with col2:
            st.button("🛒 Make New Order")
            st.button("⚠️ Check Low Stock")


