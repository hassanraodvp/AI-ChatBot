from playsound import playsound
import eel
@eel.expose
def playAssistantSound():
    music_file = "UI\\assets\\Audio\\sound.mp3"
    playsound(music_file)