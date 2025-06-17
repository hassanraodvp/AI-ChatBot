import eel
from engine.features import *
playAssistantSound()

eel.init("UI")
eel.start("index.html", mode="chrome", host="localhost", block=True)