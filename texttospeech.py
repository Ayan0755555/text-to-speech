import streamlit as st
from gtts import gTTS

def text_to_speech(text, accent="en", c=0):
    tts = gTTS(text=text, lang=accent)
    tts.save(f"output{c}.mp3")
    return f"output{c}.mp3"

st.title("Text to Speech Converter")
st.write("Enter text below and convert it to speech.")

text_input = st.text_area("Enter your text here:")



accent = st.selectbox("Select Language", ["en", "hi", "fr", "de"])
c = 0
if st.button("Convert your text to speech"):
    if text_input.strip():
        audio_file = text_to_speech(text_input, accent,c)
        c += 1
        st.audio(audio_file, format="audio/mp3")
        with open(audio_file, "rb") as file:
            btn = st.download_button(
                label="Download Audio",
                data=file,
                file_name="output.mp3",
                mime="audio/mp3"
            )
    else:
        st.warning("Please enter some text to convert for speech.")    
