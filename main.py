# pip install pyttsx3      -- run this first
import pyttsx3

# initialize the engine
engine = pyttsx3.init()

# Function to speech the text
def text_to_speech(message):
    engine.say(message)
    print(message)
    engine.runAndWait()

text_to_speech("Hello World")
