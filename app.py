import google.generativeai as genai
import os
from dotenv import load_dotenv
import streamlit as st
from PIL import Image

# # Load environment variables from .env file
# load_dotenv()
# # Set up Google Generative AI API key
# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

#Gemini respons function
def get_response(input_prompt, image):
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content([input_prompt, image])
    return response.text.strip()
    
# Streamlit app
st.set_page_config(page_title="Recipe generator", page_icon=":robot_face:")
st.header("Recipe Generator")
uploaded_file = st.file_uploader("Upload image of Ingredients", type=["jpg","jpeg","png"])
image = " "
if uploaded_file is not None:
    st.write("File uploaded successfully!")
    image = Image.open(uploaded_file)
    st.image(uploaded_file, caption="Uploaded Image", use_container_width=True)

submit = st.button("Get Recipe")

input_promt = """Analyze the uploaded image of food ingredients visible and provide a detailed recipe of a dish that can be made using them. Provide inegredient preparation steps and cooking instructions in step-by-step format.   
......
Finally you can mention whether the meal is healthy or not and provide a brief summary of the overall nutritional value of the meal."""

if submit:
    if uploaded_file is None:
        st.warning("Please upload an image of ingredients first.")
    else:
        response = get_response(input_promt, image)

        if not response:
            st.error("No response generated. Try another image.")
        else:
            st.header("Response from Gemini:")
            st.write(response)

user_input = st.text_input("")

