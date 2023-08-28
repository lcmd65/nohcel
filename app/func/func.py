from functools import partial
import speech_recognition as sr
import pyttsx4
from gtts import gTTS
import playsound
import pyaudio
import threading
import time
import app.environment

def sequence(*functions):
    def func(*args, **kwargs):
        return_value = None
        for function in functions:
            return_value = function(*args, **kwargs)
        return return_value
    return func

def speakText(command):
    # Initialize the engine
    engine = pyttsx4.init(driverName='sapi5') 
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 0.5)
    engine.say(command)
    engine.runAndWait()
    
def speakTextOS(command):
    pass

def audioMicroToText():
    try:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            speakText("hey hahahaha")
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source, phrase_time_limit= 10)
            text = r.recognize_google(audio, language="vi-VI")
                # The `processingTest()` method is not available in macOS Ventura.
                # You can remove this line or replace it with another method to process the text.
                # text = text.processingTest()
            return text
    except Exception as e:
        print(e)

def audioToText(audio_path):
    """ audio file to text """
    try:
        r = sr.Recognizer()
        with audio_path as source:
            r.adjust_for_ambient_noise(source)
            audio = r.record(source)
            text = r.recognize_google(audio, language="vi-VI")
            return text
    except Exception as e:
        print(e)
            
def textToAudio(text):
    """ processing text to audio by google api """
    try:
        output = gTTS(text,lang="vi", slow = False)
        output.save("".join(["output/", str(time.time),".mp3"]))
        # playsound.playsound("".join(["output/", str(time.time),".mp3"]), True)
    except Exception as e:
        print(e)

def showAudio():
    """ task """
    pass

## threading 

def audioMicroToTextThread():
    th = threading.Thread(target= partial(audioMicroToText))
    th.daemon = True
    th.start()
    
def speakTextThread(command):
    app.environment.thread2 = threading.Thread(target= partial(speakText, command))
    app.environment.thread2.daemon = True
    app.environment.thread2.start()
    
    
    
    
    
    