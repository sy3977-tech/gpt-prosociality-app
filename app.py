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
can be used for predicting experimental treatment effects. 
To manage costs of hosting this demo publicly, it uses GPT-5-mini.

""")

st.markdown("---")

# Section 1: Treatment
st.markdown("### 1. Treatment.")
st.markdown("Write a message or vignette exactly as it would appear in a survey experiment.")

treatment_text = st.text_area(
    "",
    height=150,
    placeholder="Type your message here...",
    label_visibility="collapsed"
)

st.markdown("---")

# Section 2: Select Target Language
st.markdown("### 2. Select Target Language.")
st.markdown("Choose the language in which the message will be presented.")

language_options = [
    "Abkhaz", "Acehnese", "Acholi", "Afar", "Afrikaans", "Albanian", "Alur", 
    "Amharic", "Arabic", "Armenian", "Assamese", "Avar", "Awadhi", "Aymara", 
    "Azerbaijani", "Balinese", "Baluchi", "Bambara", "Baoulé", "Bashkir", 
    "Basque", "Batak Karo", "Batak Simalungun", "Batak Toba", "Belarusian", 
    "Bemba", "Bengali", "Betawi", "Bhojpuri", "Bikol", "Bosnian", "Breton", 
    "Bulgarian", "Buryat", "Cantonese", "Catalan", "Cebuano", "Chamorro", 
    "Chechen", "Chichewa", "Chinese (Simplified)", "Chinese (Traditional)", 
    "Chuukese", "Chuvash", "Corsican", "Crimean Tatar (Cyrillic)", 
    "Crimean Tatar (Latin)", "Croatian", "Czech", "Danish", "Dari", "Dhivehi", 
    "Dinka", "Dogri", "Dombe", "Dutch", "Dyula", "Dzongkha", "English", 
    "Esperanto", "Estonian", "Ewe", "Faroese", "Fijian", "Filipino", "Finnish", 
    "Fon", "French", "French (Canada)", "Frisian", "Friulian", "Fulani", "Ga", 
    "Galician", "Georgian", "German", "Greek", "Guarani", "Gujarati", 
    "Haitian Creole", "Hakha Chin", "Hausa", "Hawaiian", "Hebrew", "Hiligaynon", 
    "Hindi", "Hmong", "Hungarian", "Hunsrik", "Iban", "Icelandic", "Igbo", 
    "Ilocano", "Indonesian", "Inuktut (Latin)", "Inuktut (Syllabics)", "Irish", 
    "Italian", "Jamaican Patois", "Japanese", "Javanese", "Jingpo", 
    "Kalaallisut", "Kannada", "Kanuri", "Kapampangan", "Kazakh", "Khasi", 
    "Khmer", "Kiga", "Kikongo", "Kinyarwanda", "Kituba", "Kokborok", "Komi", 
    "Konkani", "Korean", "Krio", "Kurdish (Kurmanji)", "Kurdish (Sorani)", 
    "Kyrgyz", "Lao", "Latgalian", "Latin", "Latvian", "Ligurian", "Limburgish", 
    "Lingala", "Lithuanian", "Lombard", "Luganda", "Luo", "Luxembourgish", 
    "Macedonian", "Madurese", "Maithili", "Makassar", "Malagasy", "Malay", 
    "Malay (Jawi)", "Malayalam", "Maltese", "Mam", "Manx", "Maori", "Marathi", 
    "Marshallese", "Marwadi", "Mauritian Creole", "Meadow Mari", 
    "Meiteilon (Manipuri)", "Minang", "Mizo", "Mongolian", "Myanmar (Burmese)", 
    "Nahuatl (Eastern Huasteca)", "Ndau", "Ndebele (South)", 
    "Nepalbhasa (Newari)", "Nepali", "NKo", "Norwegian", "Nuer", "Occitan", 
    "Odia (Oriya)", "Oromo", "Ossetian", "Pangasinan", "Papiamento", "Pashto", 
    "Persian", "Polish", "Portuguese (Brazil)", "Portuguese (Portugal)", 
    "Punjabi (Gurmukhi)", "Punjabi (Shahmukhi)", "Quechua", "Qʼeqchiʼ", "Romani", 
    "Romanian", "Rundi", "Russian", "Sami (North)", "Samoan", "Sango", 
    "Sanskrit", "Santali (Latin)", "Santali (Ol Chiki)", "Scots Gaelic", 
    "Sepedi", "Serbian", "Sesotho", "Seychellois Creole", "Shan", "Shona", 
    "Sicilian", "Silesian", "Sindhi", "Sinhala", "Slovak", "Slovenian", 
    "Somali", "Spanish", "Sundanese", "Susu", "Swahili", "Swati", "Swedish", 
    "Tahitian", "Tajik", "Tamazight", "Tamazight (Tifinagh)", "Tamil", "Tatar", 
    "Telugu", "Tetum", "Thai", "Tibetan", "Tigrinya", "Tiv", "Tok Pisin", 
    "Tongan", "Tshiluba", "Tsonga", "Tswana", "Tulu", "Tumbuka", "Turkish", 
    "Turkmen", "Tuvan", "Twi", "Udmurt", "Ukrainian", "Urdu", "Uyghur", 
    "Uzbek", "Venda", "Venetian", "Vietnamese", "Waray", "Welsh", "Wolof", 
    "Xhosa", "Yakut", "Yiddish", "Yoruba", "Yucatec Maya", "Zapotec", "Zulu", 
    "Custom"  # Added "Custom" at the end
]

selected_language = st.selectbox("", language_options, key="language", label_visibility="collapsed")

# Show custom input if "Custom" is selected
if selected_language == "Custom":
    custom_language = st.text_input("Enter custom language:")

st.markdown("---")

# Section 3: Dependent Variable
st.markdown("### 3. Dependent Variable.")
st.markdown("Choose an attitude or behavioral intention to estimate the treatment effect.")

dependent_var_options = [
    "How likely are you going to donate?",
    "How likely are you going to share the message on social media?",
    "How sympathetic did you feel while reading the message?",
    "How connected did you feel toward the beneficiary?"
]

selected_dependent_var = st.radio(
    "",
    dependent_var_options,
    key="dependent_var",
    label_visibility="collapsed"
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
        st.write(f"**Treatment Message:** {treatment_text}")
        st.write(f"**Target Language:** {selected_language}")
        if selected_language == "Custom" and 'custom_language' in locals():
            st.write(f"**Custom Language:** {custom_language}")
        st.write(f"**Dependent Variable:** {selected_dependent_var}")
        
        # This is where you would add API calls to GPT or your model
        st.info("🤖 Model prediction would appear here...")
