from functools import partial
import speech_recognition as sr
import pyaudio
from AppKit import NSSpeechSynthesizer
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

def audioMicroToText():
    """ processing audio from microphone """
    speechSynthesizer = NSSpeechSynthesizer
    speech = speechSynthesizer.alloc().init()
    speech.setVoice_("com.apple.speech.synthesis.voice.Alex")
    speech.setVolume_(1.0)
    speech.setRate_(200)
    speech.startSpeakingString_('Hi! I am Nohcel')
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
