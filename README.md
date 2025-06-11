# 🎬 Video Script Generator & TTS System

Generate engaging video scripts with realistic AI voiceovers in multiple languages using a single click.

🔗 **Live Demo:**  
[👉 Open App](https://video-script-generator-with-tts-8ox4lamds9hhgg5mmwepvo.streamlit.app/)

---

## ✨ Features

- ✅ AI-powered script generation (educational, promotional, storytelling)
- 🗣️ Multilingual TTS using **Edge TTS** (free, no API quota needed)
- 🎤 Voice selection via Voice ID (e.g., en-US-JennyNeural, hi-IN-SwaraNeural)
- 🎞️ Storyboard generation with timestamped scenes and visual suggestions
- 🎵 Sound effects library – automatic suggestions
- 📦 Downloadable outputs: script, storyboard, and voiceover audio

---

## 🧠 Technologies Used

- [Streamlit](https://streamlit.io/) – Frontend UI
- [Google Gemini 1.5 Flash](https://makersuite.google.com/app) – Script generation
- [Edge TTS](https://github.com/rany2/edge-tts) – Free multilingual TTS engine
- Python 3.8+

---

## 🚀 How to Run Locally

### 1. Clone the repo

```bash
git clone https://github.com/your-username/video-script-generator.git
cd video-script-generator
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Set up `.env` file

Create a `.env` file and add your [Google AI Studio](https://makersuite.google.com/app) API key:

```
GOOGLE_API_KEY=your_gemini_api_key_here
```

### 4. Run the Streamlit app

```bash
streamlit run app.py
```

---

## 📁 Project Structure

```
├── app.py                 # Main Streamlit interface
├── script_generator.py    # Handles Gemini-based script creation
├── tts_engine.py          # Edge TTS text-to-speech logic
├── utils.py               # Storyboard and SFX generator
├── production_planner.py  # Generates scene timing and structure
├── requirements.txt       
└── storyboards/           # Auto-saved storyboard text files
```

---

## 📌 Edge TTS Voice Examples

| Language     | Voice ID              |
|--------------|------------------------|
| English (US) | en-US-JennyNeural     |
| Hindi        | hi-IN-SwaraNeural     |
| French       | fr-FR-DeniseNeural    |
| Spanish      | es-ES-ElviraNeural    |
| German       | de-DE-KatjaNeural     |

[🔗 Full List of Voices](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/language-support#text-to-speech)

---

## 🙋‍♂️ Author

Made with ❤️ by [Your Name]

Feel free to connect on [LinkedIn](https://linkedin.com/) or [GitHub](https://github.com/)

---

## 📝 License

This project is licensed under the MIT License – use freely and modify as needed.
