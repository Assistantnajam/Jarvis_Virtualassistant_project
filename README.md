# Jarvis_Virtualassistant_project
🤖 J.A.R.V.I.S — Virtual Assistant
> **Just A Rather Very Intelligent System**
> A Python-based voice assistant inspired by Iron Man's JARVIS — listens to your voice, responds intelligently, and controls your computer.
---
⚙️ Features
Command	What to Say	What it Does
🌐 Open Google	"open google"	Opens Google in browser
📺 Open YouTube	"open youtube"	Opens YouTube in browser
📘 Open Facebook	"open facebook"	Opens Facebook in browser
💼 Open LinkedIn	"open linkedin"	Opens LinkedIn in browser
🎵 Play Music	"play [song name]"	Plays song from music library
🧮 Calculate	"calculate 5 plus 3"	Solves math expressions
🕐 Current Time	"time"	Tells the current time
📅 Current Date	"date"	Tells today's date
😂 Tell a Joke	"joke"	Tells a random joke
🔍 Wikipedia Search	"who is Elon Musk"	Searches and reads Wikipedia
🔇 Mute Volume	"mute"	Mutes system volume
📝 Open Notepad	"open notepad"	Opens Notepad app
🔢 Open Calculator	"open calculator"	Opens Calculator app
🗒️ Take a Note	"take a note"	Saves voice note to notes.txt
⚡ Shutdown PC	"shutdown"	Shuts down the computer
🔄 Restart PC	"restart"	Restarts the computer
---

🛠️ Tech Stack
Python 3.11
SpeechRecognition — listens to your voice via microphone
edge-tts — Microsoft Neural voices for natural speech output
pygame — plays the generated audio
pyttsx3 — offline text-to-speech engine
gTTS — Google Text-to-Speech
wikipedia — fetches Wikipedia summaries
pyjokes — generates random jokes
webbrowser — opens websites in browser
ctypes — controls system volume on Windows
---
📁 Project Structure
```
Jarvis_Virtualassistant/
│
├── main.py              # Main file — run this to start Jarvis
├── musicLibrary.py      # Dictionary of song names and their links
├── requirements.txt     # All required libraries
├── notes.txt            # Auto-created when you take a note
├── README.md            # This file
└── venv/                # Virtual environment (not uploaded to GitHub)
```
---
🚀 Getting Started
1. Clone the repository
```bash
git clone https://github.com/your-username/Jarvis_Virtualassistant.git
cd Jarvis_Virtualassistant
```
2. Create a virtual environment
```bash
py -3.11 -m venv venv
venv\Scripts\activate
```
3. Install all libraries
```bash
pip install -r requirements.txt
```
4. Run Jarvis
```bash
python main.py
```
---
🎙️ How to Use
Run `main.py`
Wait for Jarvis to say "Initializing Jarvis... Greetings Sir"
Say "Jarvis" — it will reply "Ya"
Now give your command — for example "open youtube" or "tell me a joke"
---
🎵 How to Add Songs
Open `musicLibrary.py` and add your songs like this:
```python
music = {
    "believer" : "https://www.youtube.com/watch?v=...",
    "shape of you" : "https://www.youtube.com/watch?v=...",
}
```
Then just say "play believer" and Jarvis will open it!
---
⚠️ Requirements
Windows OS
Working microphone
Internet connection
Python 3.11
---
🙋‍♂️ Author
Syed Najam ul Hassan
---

📄 License
This project is open source and available under the MIT License
---
> *"At your service, sir."* — JARVIS 🤖
