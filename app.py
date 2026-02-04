import streamlit as st
import google.generativeai as genai
from PIL import Image
import sys

# ---- STREAMLIT CONFIG ----
st.set_page_config(page_title="Recipe Generator", page_icon="🍳")

# ---- DEBUG (remove later if you want) ----
st.write("Python:", sys.version)

# ---- CONFIGURE GEMINI ----
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

# ---- GEMINI FUNCTION ----
def get_response(prompt, image):
    model = genai.GenerativeModel("models/gemini-1.0-pro-vision-latest")
    response = model.generate_content(
        [prompt, image],
        generation_config={"temperature": 0.4}
    )
    return response.text

# ---- UI ----
st.title("🍳 Smart Recipe Generator")

uploaded_file = st.file_uploader(
    "Upload an image of ingredients",
    type=["jpg", "jpeg", "png"]
)

prompt = """
Analyze the image of food ingredients.
Create ONE detailed recipe that can be made using them.

Include:
1. Dish name
2. Ingredients list
3. Step-by-step cooking instructions
4. Healthiness and nutrition summary
"""

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_container_width=True)

    if st.button("Get Recipe"):
        with st.spinner("Cooking something tasty..."):
            try:
                result = get_response(prompt, image)

                if not result or not result.strip():
                    st.error("No response generated. Try another image.")
                else:
                    st.subheader("🍽 Recipe")
                    st.write(result)

            except Exception as e:
                st.error("Gemini failed to respond.")
                st.exception(e)


