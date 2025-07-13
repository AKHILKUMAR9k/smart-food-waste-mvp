import streamlit as st
import speech_recognition as sr
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
from dotenv import load_dotenv

load_dotenv()

# Simple fallback if agent module doesn't exist
try:
    from aiagent.agent import load_agent
    agent = load_agent()
except:
    agent = None

st.set_page_config(page_title="Smart Food Surplus AI", layout="centered")
st.title("🎤🧠 Voice-Enabled Food Waste Assistant")

# Text Input
st.markdown("### 🔍 Ask a Question")
text_query = st.text_input("Type here or use the voice recorder below",
                           key="text_input")

# Voice Input
st.markdown("#### 🎙️ Speak a Question (click and talk)")
if st.button("🎧 Start Recording"):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("Listening...")
        audio = r.listen(source)
        try:
            spoken_text = r.recognize_google(audio)
            st.success(f"You said: {spoken_text}")
            text_query = spoken_text
        except:
            st.error("Sorry, I couldn't understand your voice.")

# Run Agent
if text_query:
    if agent:
        with st.spinner("Analyzing with AI..."):
            try:
                response = agent.run(text_query)
                st.success("✅ AI Suggestion:")
                st.write(response)
            except Exception as e:
                st.error(f"Error running agent: {str(e)}")
    else:
        st.warning("AI agent not available. Please check your agent configuration.")

# Load data with error handling
try:
    df = pd.read_csv("data/surplus_predictions.csv")
    data_available = True
except FileNotFoundError:
    st.warning("Surplus predictions data not found. Please run the predictor model first.")
    data_available = False
    df = None

st.markdown("---")
st.markdown("### 📊 Insights Dashboard")

if data_available and df is not None:
    if st.button("📦 Show Surplus by Store"):
        fig, ax = plt.subplots()
        sns.barplot(data=df,
                    x="store",
                    y="surplus_units",
                    hue="suggested_action",
                    ax=ax)
        ax.set_title("Surplus by Store & Action")
        st.pyplot(fig)

    if st.button("⏳ Expiry Breakdown"):
        fig, ax = plt.subplots()
        sns.histplot(data=df, x="days_to_expiry", bins=10, kde=True)
        ax.set_title("Items by Days to Expiry")
        st.pyplot(fig)
else:
    st.info("Dashboard data not available. Run the predictor model to generate data.")
