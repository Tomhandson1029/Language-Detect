import streamlit as st
from langdetect import detect
from langcodes import Language
from deep_translator import GoogleTranslator

def detect_language(text):
    try:
        language_code = detect(text)
        language = Language(language_code).display_name()
    except:
        language = "unknown"
    return language

def translate_text(text, target_language):
    translator = GoogleTranslator(source='auto', target=target_language)
    translated_text = translator.translate(text)
    return translated_text

def main():
    st.title("Text Translator")

    input_text = st.text_area("Enter the text you want to translate:", height=50)

    if input_text:
        detected_language = detect_language(input_text)
        if detected_language != "unknown":
            st.markdown(f"Detected language: {detected_language}")
        else:
            st.warning("Could not detect language. Please try again.")

    target_language = st.selectbox("Choose the target language:", [
            "en - English", "fr - French", "es - Spanish", "de - German",
            "hi - Hindi", "mr - Marathi", "it - Italian", "pt - Portuguese",
            "nl - Dutch", "ru - Russian","ja - Japanese", "ko - Korean",
            "zh - Chinese", "ar - Arabic"
        ])
    target_language_code = target_language.split(" - ")[0]

    translated_text = translate_text(input_text, target_language_code)
    st.markdown(f'<div style="border: 2px solid white; padding: 20px;">{translated_text}</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
