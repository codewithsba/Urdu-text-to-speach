import pygame
from gtts import gTTS


def speak_text_urdu(text):
    tts = gTTS(text=text, lang='ur', slow=False)
    tts.save("output.mp3")

    # Play the audio file
    pygame.mixer.init()
    pygame.mixer.music.load("output.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue


# Example usage
speak_text_urdu("آپ کیسے ہیں؟")
