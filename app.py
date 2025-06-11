import streamlit as st
from script_generator import ScriptGenerator
from tts_engine import TTSEngine
from production_planner import ProductionPlanner
from utils import get_sound_effects_list, generate_storyboard
import json

script_gen = ScriptGenerator()
tts = TTSEngine()
planner = ProductionPlanner()

st.set_page_config(page_title="Video Script Generator", layout="wide")
st.title("Video Script Generator & TTS System")

with st.sidebar:
    st.header("Configuration")
    topic = st.text_input("Enter your topic")
    video_type = st.selectbox("Select video type", ["educational", "promotional", "storytelling"])
    length = st.select_slider("Script length", options=["short", "medium", "long"])
    language = st.selectbox("Language", ["en", "es", "fr", "de"])
    voice_id = st.text_input("ElevenLabs Voice ID (optional)", value="EXAVITQu4vr4xnSDxMaL")

if st.button("Generate Script & Audio") and topic:
    with st.spinner("Generating script..."):
        script = script_gen.generate_script(topic, video_type, length, language)

        st.header("Generated Script")
        st.subheader(script.title)
        st.write("Hook:", script.hook)
        st.write("Content:", script.content)
        st.write("Call to Action:", script.call_to_action)

        with st.spinner("Generating audio..."):
            audio_file = tts.generate_speech(script.content, language=language, voice_id=voice_id)
            st.audio(audio_file)

        with st.spinner("Creating production plan..."):
            production_plan = planner.create_plan(script, audio_file)
            st.header("Production Plan")
            st.json(production_plan.scenes)

        st.download_button("Download Script", script.content, "script.txt", "text/plain")
        with open(audio_file, 'rb') as f:
            st.download_button("Download Audio", f, "audio.mp3", "audio/mp3")
        st.download_button("Download Plan", json.dumps(production_plan.scenes, indent=2), "plan.json")

        with st.spinner("Generating Storyboard..."):
            sb_path = generate_storyboard(script.content)
            with open(sb_path, "r") as f:
                st.download_button("Download Storyboard", f, "storyboard.txt", "text/plain")

        st.header("Add Sound Effects (Optional)")
        effects = get_sound_effects_list()
        selected_effect = st.selectbox("Choose a sound effect", effects)
        if selected_effect:
            st.audio(f"sounds/{selected_effect}")
else:
    st.info("Enter a topic and click 'Generate Script & Audio'")
