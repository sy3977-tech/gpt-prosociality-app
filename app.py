import streamlit as st
# Copyright (c) 2025 sy3977-tech
# Licensed under the MIT License
# Language Prosociality Predictor - Demo App

import streamlit as st
# Page configuration
st.set_page_config(page_title="Language Prosociality Predictor", layout="wide")

# Title and authors
st.title("Demo: Predicting language prosociality using LLMs")

# Introduction
st.markdown("""
This demo accompanies the paper English as a Lingua Franca Promotes Non-native Consumer Donations (Du et al. 2025) and 
can be used for predicting experimental treatment effects on U.S. adults. 
To manage costs of hosting this demo publicly, it uses GPT-5-mini.

""")

st.markdown("---")

# Section 1: Language Selection
st.markdown("### 1. Select Language")
language_options = ["English", "Mandarin", "Spanish", "Estonian", "Japanese", "Custom"]
selected_language = st.selectbox("Choose a language:", language_options, key="language")

# Show custom input if "Custom" is selected
if selected_language == "Custom":
    custom_language = st.text_input("Enter custom language:")

st.markdown("---")

# Section 2: Dependent Variable
st.markdown("### 2. Dependent Variable")
st.markdown("Choose an attitude or decision, to estimate a treatment effect.")

dependent_var_options = [
    "How likely are you going to donate?",
    "How likely are you going to share the message on social media?",
    "How sympathetic did you feel while reading the message?",
    "How connected did you feel toward the beneficiary?"

]

selected_dependent_var = st.radio(
    "Select a dependent variable:",
    dependent_var_options,
    key="dependent_var"
)

st.markdown("---")

# Section 3: Treatment
st.markdown("### 3. Treatment")
st.markdown("Write a message or vignette exactly as it would appear in a survey experiment.")

treatment_text = st.text_area(
    "Enter your treatment message:",
    height=200,
    placeholder="Type your message here..."
)

st.markdown("---")

# Submit button
if st.button("Submit", type="primary"):
    if treatment_text.strip() == "":
        st.error("⚠️ Please enter a treatment message before submitting.")
    else:
        st.success("✅ Form submitted successfully!")
        
        # Display the collected information
        st.markdown("### Your Submission:")
        st.write(f"**Language:** {selected_language}")
        if selected_language == "Custom" and 'custom_language' in locals():
            st.write(f"**Custom Language:** {custom_language}")
        st.write(f"**Dependent Variable:** {selected_dependent_var}")
        st.write(f"**Treatment Message:** {treatment_text}")
        
        # This is where you would add API calls to GPT or your model
        st.info("🤖 Model prediction would appear here...")
