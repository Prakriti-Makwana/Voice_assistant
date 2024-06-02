from playsound import playsound
import eel


# Playing assistant sound function

@eel.expose
def playAssistantSound():
    music_dir ="www\\assets\\vendore\\texllate-20240601T171506Z-001\\texllate\\audio\\Voicy_Siri sound effect.mp3"
    playsound(music_dir)
