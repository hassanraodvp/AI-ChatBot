import os
import re
from playsound import playsound
import eel
from engine.command import speak
from engine.config import ASSISTANT_NAME
import pywhatkit as kit

# This function plays a sound file when called.
@eel.expose
def playAssistantSound():
    music_file = "UI\\assets\\Audio\\sound.mp3"
    playsound(music_file)


@eel.expose
def openCommand(query):
    query = query.replace(ASSISTANT_NAME, "")
    query = query.replace("open", "")
    query.lower()

    if query != "":
        speak(f"Opening {query}")
        os.system(f"start {query}")
    else:
        speak("Please specify what you want to open.")

def playYoutube(query):
    searchItem = extract_yt_term(query)
    speak(f"Playing {searchItem} on YouTube")
    kit.playonyt(searchItem)        

def extract_yt_term(command):
    pattern = r"play\s + (.+)\s + on\s + YouTube"
    match = re.search(pattern, command, re.IGNORECASE)
    return match.group(1) if match else None