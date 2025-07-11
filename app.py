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
    text = ("Welcome to Inventory App")
    text_position = (200, 30)  
            
    draw.text(text_position, text, fill="black", font=font)
    st.image(img, caption="Let's get started!", use_column_width=True)
    if st.button("👉 Click to Continue"):
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
if st.button("📦 Start Inventory"):
    import streamlit as st
from PIL import Image

# ----------------------------
# Step 1: Store items as list of dictionaries
# ----------------------------
inventory_items = [
    {"name": "Milk", "image": "images/milk.jpg"},
    {"name": "Bread", "image": "images/bread.jpg"},
    {"name": "Eggs", "image": "images/eggs.jpg"},
    {"name": "Butter", "image": "images/butter.jpg"}
]

# Session State: to remember position and values
if 'index' not in st.session_state:
    st.session_state.index = 0

if 'quantities' not in st.session_state:
    st.session_state.quantities = {}

if 'skipped' not in st.session_state:
    st.session_state.skipped = []

# ----------------------------
# Step 2: Show Current Item
# ----------------------------
current = inventory_items[st.session_state.index]
st.subheader(f"Item: {current['name']}")

# Display Image
image = Image.open(current['image'])
st.image(image, width=200)

# Quantity Input
qty = st.number_input("Enter quantity:", min_value=0, step=1, key=current['name'])

# ----------------------------
# Step 3: Buttons
# ----------------------------
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Back"):
        if st.session_state.index > 0:
            st.session_state.index -= 1

with col2:
    if st.button("Skip"):
        st.session_state.skipped.append(current['name'])
        st.session_state.index += 1

with col3:
    if st.button("Next"):
        st.session_state.quantities[current['name']] = qty
        st.session_state.index += 1

# ----------------------------
# Step 4: End of List
# ----------------------------
if st.session_state.index >= len(inventory_items):
    st.success("✅ Inventory complete!")

    st.write("### Collected Quantities:")
    for item, q in st.session_state.quantities.items():
        st.write(f"{item}: {q}")

    st.write("### Skipped Items:")
    for item in st.session_state.skipped:
        st.write(f"❌ {item}")

    # Optionally, provide download option later


