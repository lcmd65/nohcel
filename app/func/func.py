from functools import partial
import speech_recognition as sr
import pyttsx3
import pyaudio
from gtts import gTTS
import playsound
import time

def sequence(*functions):
    def func(*args, **kwargs):
        return_value = None
        for function in functions:
            return_value = function(*args, **kwargs)
        return return_value
    return func

def speakText(command):
    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()
     
def audioMicroToText():
    try:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source)
            text = r.recognize_google(audio,language="vi-VI")
                # The `processingTest()` method is not available in macOS Ventura.
                # You can remove this line or replace it with another method to process the text.
                # text = text.processingTest()
            return text
    except Exception as e:
        print(e)

def audioMicroToText2():
    speakText("Hi! I am Nohcel")
    try:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source)
            text = r.recognize_google(audio,language="vi-VI")
                # The `processingTest()` method is not available in macOS Ventura.
                # You can remove this line or replace it with another method to process the text.
                # text = text.processingTest()
            return text
    except Exception as e:
        print(e)


def audioToText(audio):
    """ task here """
    text = None
    return text
            
def textToAudio(text):
    """ processing text to audio by google api """
    try:
        output = gTTS(text,lang="vi", slow = False)
        output.save("".join(["output/", str(time.time),".mp3"]))
        # playsound.playsound("".join(["output/", str(time.time),".mp3"]), True)
    except Exception as e:
        print(e)

def showAudio():
    pass

if __name__ =="__main__":
    speakText("Hi")
    
# python3 app/func/func.py