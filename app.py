import google.generativeai as genai
import os
from dotenv import load_dotenv
import streamlit as st
from PIL import Image

# Load environment variables from .env file
load_dotenv()
# Set up Google Generative AI API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

#Gemini respons function
def get_response(input_promt, image):
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content([input_promt, image[0]])
    return response.text.strip()

#image handling function
def handle_image(uploaded_file):
    if uploaded_file is not None:
        byte_data = uploaded_file.getvalue()
        image_parts = [{
            "mime_type" : uploaded_file.type,
            "data" : byte_data
        }]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")
    
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

input_promt = """Analyze the image of the ingredients and provide a detailed recipe of a dish that can be made using them.Provide inegredient preparation steps and cooking instructions in step-by-step format.   
......
Finally you can mention whether the meal is healthy or not and provide a brief summary of the overall nutritional value of the meal."""

if submit:
    if uploaded_file is None:
        st.warning("Please upload an image of ingredients first.")
    else:
        input_image = handle_image(uploaded_file)
        response = get_response(input_promt, input_image)
        st.header("Response from Gemini:")
        st.write(response)

user_input = st.text_input("")