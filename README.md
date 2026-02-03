# 🍳 AI Recipe Generator from Ingredient Images

An AI-powered recipe generation application that analyzes an image of food ingredients and generates a complete cooking recipe with preparation steps, instructions, and nutritional insights.

Built using Google Gemini Vision capabilities and deployed as an interactive Streamlit web app.

---

## 🚀 Features

- Upload an image of raw ingredients
- AI-powered ingredient understanding using Gemini Vision
- Step-by-step recipe generation
- Ingredient preparation and cooking instructions
- Health and nutritional assessment of the dish
- Simple, interactive web UI

---

## 🧠 Tech Stack

- **Python**
- **Streamlit** (UI & app framework)
- **Google Gemini 1.5 Flash** (Multimodal reasoning)
- **Pillow** (Image processing)
- **python-dotenv** (Environment variable management)

---

## 📸 How It Works

1. User uploads an image of ingredients
2. The image is processed and sent to the Gemini Vision model
3. The model analyzes visible ingredients
4. A complete recipe is generated including:
   - Preparation steps
   - Cooking instructions
   - Health and nutrition summary

---

## 🔐 Environment Variables

Create a `.env` file locally (not required on Streamlit Cloud):

```env
GOOGLE_API_KEY=your_google_gemini_api_key
