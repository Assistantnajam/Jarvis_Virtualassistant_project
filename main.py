import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
from gtts import gTTS
import pygame
import os
import datetime
import pyjokes
import wikipedia
import ctypes

# pip install pocketsphinx pyjokes wikipedia

recognizer = sr.Recognizer()
engine = pyttsx3.init() 

# This function uses the pyttsx3 library to convert text to speech offline. 
# It runs synchronously and waits for the speech to finish before returning.
def speak_old(text):
    engine.say(text)
    engine.runAndWait()

# This function converts text to an mp3 audio file using Google Text-to-Speech (gTTS), 
# plays it using pygame, and then deletes the temporary mp3 file once playback is finished.
def speak(text):
    tts = gTTS(text)
    tts.save('temp.mp3') 

    # Initialize Pygame mixer
    pygame.mixer.init()

    # Load the MP3 file
    pygame.mixer.music.load('temp.mp3')

    # Play the MP3 file
    pygame.mixer.music.play()

    # Keep the program running until the music stops playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    
    pygame.mixer.music.unload()
    os.remove("temp.mp3") 

# This function processes the recognized voice commands spoken by the user and determines 
# what action Jarvis should take based on the keywords found in the command string.
def processCommand(c):
    if "open google" in c.lower():
        speak("Opening Google sir")
        webbrowser.open("https://google.com")
    
    elif "open facebook" in c.lower():
        speak("Opening Facebook sir")
        webbrowser.open("https://facebook.com")
    
    elif "open youtube" in c.lower():
        speak("Opening YouTube sir")
        webbrowser.open("https://youtube.com")
    
    elif "open linkedin" in c.lower():
        speak("Opening LinkedIn sir")
        webbrowser.open("https://linkedin.com")
        
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)
        
    elif "calculate" in c.lower():
        try:
            # Simple way to evaluate math expression from speech
            expression = c.lower().replace("calculate", "").strip()
            # Replace common spoken words with operators
            expression = expression.replace("plus", "+").replace("minus", "-").replace("times", "*").replace("multiplied by", "*").replace("divided by", "/")
            # Remove any characters that aren't numbers or math symbols for safety
            safe_chars = set("0123456789+-*/. ")
            safe_expression = "".join(char for char in expression if char in safe_chars)
            result = eval(safe_expression)
            speak(f"The answer is {result}")
        except Exception as e:
            speak("Sorry, I couldn't understand the calculation.")
            
    elif "time" in c.lower():
        now = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {now}")
        
    elif "date" in c.lower():
        today = datetime.datetime.now().strftime("%B %d, %Y")
        speak(f"Today's date is {today}")
        
    elif "joke" in c.lower():
        joke = pyjokes.get_joke()
        speak(joke)
        
    elif "wikipedia" in c.lower() or "who is" in c.lower() or "what is" in c.lower():
        try:
            query = c.lower().replace("wikipedia", "").replace("who is", "").replace("what is", "").strip()
            result = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia: " + result)
        except Exception as e:
            speak("Sorry, I couldn't find anything on Wikipedia for that.")
            
    elif "mute volume" in c.lower() or "mute" in c.lower():
        # Toggle mute on Windows using ctypes
        HWND_BROADCAST = 0xFFFF
        WM_APPCOMMAND = 0x319
        APPCOMMAND_VOLUME_MUTE = 0x80000
        ctypes.windll.user32.SendMessageW(HWND_BROADCAST, WM_APPCOMMAND, 0, APPCOMMAND_VOLUME_MUTE)
        speak("Volume muted.")
        
    elif "open notepad" in c.lower():
        speak("Opening Notepad")
        os.system("notepad")
        
    elif "open calculator" in c.lower() and "calculate" not in c.lower():
        speak("Opening Calculator application")
        os.system("calc")
        
    elif "shutdown" in c.lower():
        speak("Shutting down the computer.")
        os.system("shutdown /s /t 1")
        
    elif "restart" in c.lower():
        speak("Restarting the computer.")
        os.system("shutdown /r /t 1")
        
    elif "take a note" in c.lower() or "write this down" in c.lower() or "make a note" in c.lower():
        speak("What should I write down?")
        try:
            with sr.Microphone() as source:
                r_note = sr.Recognizer()
                print("Listening for note...")
                audio = r_note.listen(source, timeout=4, phrase_time_limit=10)
                note = r_note.recognize_google(audio)
                with open("notes.txt", "a") as f:
                    f.write(f"{datetime.datetime.now()}: {note}\n")
                speak("I have taken the note.")
        except Exception as e:
            speak("Sorry, I couldn't catch that note.")
            print(f"Error taking note: {e}")
            
    else:
        speak("I am sorry, I can only perform basic tasks right now.")


if __name__ == "__main__":
    speak("Initializing Jarvis...., Greetings Sir How can I help you today")
    while True:
        # Listen for the wake word "Jarvis"
        # obtain audio from the microphone
        r = sr.Recognizer()
         
        print("recognizing...")
        try:
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source, duration=0.5)
                print("Listening...")
                audio = r.listen(source, timeout=5, phrase_time_limit=3)
            word = r.recognize_google(audio)
            if(word.lower() == "jarvis"):
                speak("Yes Sir")
                # Listen for command
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)


        except Exception as e:
            print("Error; {0}".format(e))
