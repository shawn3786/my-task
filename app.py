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
    text =  st.title("Welcome to Inventory App")
    text2 = st.write("Tap the image to continue...")
    text_position = (200, 30)  
    text2_postion = (180,480)
            
    draw.text(text_position, text, fill="black", font=font)
    draw.text2(text_position, text, fill="black", font=font)
    st.markdown("""
        <form action="" method="post">
            <button type="submit" name="go" style="border:none; background:none;">
                <img src="https://raw.githubusercontent.com/vindinvv/inventory-app/main/images/welcome.jpg"
                     style="width:100%; border-radius:10px;" alt="Welcome">
            </button>
        </form>
    """, unsafe_allow_html=True)
    if "go" in st.experimental_get_query_params():
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




