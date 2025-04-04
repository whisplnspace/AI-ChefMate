import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load API Key from .env file
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

# Configure Gemini API
if not API_KEY:
    st.error("🚨 API Key is missing! Please add it to the .env file.")
    st.stop()

genai.configure(api_key=API_KEY)


# Function to Generate a Recipe
def generate_recipe(ingredients, dietary_preferences, cuisine, region):
    prompt = f"""
    You are a top Indian Chef 🇮🇳. Create a unique **{region} Indian** {cuisine} dish using these ingredients: {', '.join(ingredients)}.

    - **Dish Name**: Unique & authentic 🌿  
    - **Short Story**: The history or significance of this dish  
    - **Ingredients List** 🛒  
    - **Step-by-Step Cooking Instructions** 🍳  
    - **Cooking Time** ⏳  
    - **Serving Size** 🍽️  
    - **Spice Level Recommendation** 🌶️🔥  
    - **Best Food Pairing** (e.g., Roti, Rice, Chutney) 🥙  
    """

    response = genai.GenerativeModel("gemini-2.0-flash").generate_content(prompt)
    return response.text


# Function to Handle Chatbot Queries
def chat_with_ai(user_input):
    chat_prompt = f"""
    You are an expert **Indian cooking assistant** 🇮🇳. Answer this cooking-related question:
    "{user_input}"
    Keep your answer **short, practical, and helpful**.
    """

    response = genai.GenerativeModel("gemini-2.0-flash").generate_content(chat_prompt)
    return response.text


# 🎨 Streamlit UI Configuration
st.set_page_config(page_title="🍛 AI ChefMate - Indian Recipes & Chatbot", layout="centered")

# 🏵️ Sidebar
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/2718/2718224.png", width=120)
st.sidebar.title("🍛 **AI ChefMate - Indian Special**")
st.sidebar.write("🌿 Bringing the flavors of India to your kitchen!")

st.sidebar.markdown("---")
st.sidebar.write("💡 **Try Ingredients:** Paneer, Methi, Jeera, Dal, Rajma, Chicken...")

# 🌟 Main Section
st.markdown("<h1 style='text-align: center; color: #8B0000;'>👨‍🍳 Namaste! AI ChefMate 🇮🇳</h1>", unsafe_allow_html=True)
st.markdown(
    "<h3 style='text-align: center; color: #FF4500;'>Your AI-powered Indian Chef - Swag Se Banaye Khana! 🍲</h3>",
    unsafe_allow_html=True)

# 🌿 Input Fields (Indian Focus)
ingredients = st.text_input("🛒 **Ingredients** (comma-separated)", "paneer, methi, garlic, tomatoes")
dietary_preferences = st.text_input("🥗 **Dietary Preferences** (e.g., vegetarian, gluten-free)", "vegetarian")
cuisine = st.selectbox("🍽️ **Preferred Cuisine**",
                       ["Traditional", "Street Food", "Mughlai", "Punjabi", "South Indian", "Bengali", "Gujarati"])
region = st.selectbox("🗺️ **Select Region of India**", ["North India", "South India", "East India", "West India"])

# 🍛 Generate Recipe Button
if st.button("🍲 Generate Indian Recipe"):
    with st.spinner("Cooking something delicious... 🍳👨‍🍳"):
        recipe = generate_recipe(ingredients.split(","), dietary_preferences, cuisine, region)
    st.success("🎉 Your Traditional Indian Recipe is Ready!")
    st.subheader("🍽️ **Your AI-Generated Recipe:**")
    st.write(recipe)

st.markdown("---")

# 🗨️ Chatbot Section
st.subheader("🤖 Ask AI ChefMate - Your Cooking Assistant!")
st.write("Type your **Indian cooking-related** questions below, and AI ChefMate will help you! 🥘")

# User Input for Chatbot
user_question = st.text_input("💬 Ask a question (e.g., 'How to make soft rotis?')", "")

if st.button("💡 Get AI Advice"):
    if user_question:
        with st.spinner("Thinking... 🤔"):
            ai_response = chat_with_ai(user_question)
        st.write(f"**👨‍🍳 AI ChefMate Says:** {ai_response}")
    else:
        st.warning("⚠️ Please enter a question!")

# 🏵️ Footer
st.markdown("---")
st.markdown("<h4 style='text-align: center;'>🌿 Made with Love in India | Powered by Gemini AI 🇮🇳</h4>",
            unsafe_allow_html=True)
