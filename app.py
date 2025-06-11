import streamlit as st
from script_generator import ScriptGenerator
from tts_engine import TTSEngine
from utils import generate_storyboard, get_sound_effects_list

# Title
st.title("🎬 Video Script Generator & TTS System")

# Inputs
topic = st.text_input("Enter your topic", "solar energy")
video_type = st.selectbox("Select video type", ["educational", "promotional", "storytelling"])
length = st.selectbox("Script length", ["short", "long"])
language = st.selectbox("Language", ["en", "hi", "fr", "es", "de"])
voice_id = st.text_input("Edge TTS Voice ID (optional)", "")

# Voice fallback map
voice_map = {
    "en": "en-US-JennyNeural",
    "hi": "hi-IN-SwaraNeural",
    "fr": "fr-FR-DeniseNeural",
    "es": "es-ES-ElviraNeural",
    "de": "de-DE-KatjaNeural"
}

if st.button("🎙️ Generate Script & Audio"):
    # Script
    generator = ScriptGenerator()
    script = generator.generate_script(topic, video_type, length, language=language)

    st.subheader("🎥 Generated Script")
    st.text_area("Script", script.content, height=400)

    # Storyboard
    sb_path = generate_storyboard(script.content)
    st.success(f"📑 Storyboard saved at: {sb_path}")

    # TTS
    tts = TTSEngine()
    selected_voice = voice_id or voice_map.get(language, "en-US-JennyNeural")
    st.write("Generating TTS audio...")
    audio_file = tts.generate_speech(script.content, language=language, voice_id=selected_voice)
    st.audio(audio_file)

    # Downloads
    with open(audio_file, "rb") as f:
        st.download_button("⬇️ Download Audio", f, file_name="output.mp3")
    with open(sb_path, "r") as f:
        st.download_button("⬇️ Download Storyboard", f, file_name="storyboard.txt")
    st.download_button("⬇️ Download Script", script.content, file_name="script.txt")

    # SFX
    st.subheader("🎵 Suggested Sound Effects")
    for sfx in get_sound_effects_list():
        st.markdown(f"- {sfx}")
