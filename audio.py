import streamlit as st
from audioldm import build_model
from audioldm import text_to_audio

st.title("AI Voice Generator")

input_text = st.text_input("Enter your text here:")
duration = st.slider("Time Duration in second", min_value=5, max_value=60, value=20)
sample_rate = st.selectbox("Sample Rate", [16000, 44000])
random_input = st.number_input("Random input:", value=42, step=1)

@st.cache_resource
def load_model():
    model = build_model()
    return model

model = load_model()

if st.button("Generate"):
    audio = text_to_audio(
        model=model,
        text=input_text,
        duration=duration,
        seed=random_input
    )
    st.audio(audio, format="audio/wav")
    st.download_button(label="Download Audio", data=audio, file_name="audio1.wav", mime="audio/wav")
    st.success("Audio generated successfully!")