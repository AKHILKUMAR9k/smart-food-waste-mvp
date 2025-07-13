import streamlit as st
import speech_recognition as sr
from ai_agent.agent import load_agent
from dotenv import load_dotenv

load_dotenv()
agent = load_agent()

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
    with st.spinner("Analyzing with AI..."):
        response = agent.run(text_query)
    st.success("✅ AI Suggestion:")
    st.write(response)

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("data/surplus_predictions.csv")

st.markdown("---")
st.markdown("### 📊 Insights Dashboard")

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
