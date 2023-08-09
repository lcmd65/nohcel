from functools import partial
import speech_recognition as sr
import pyaudio
from tkinter import messagebox
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
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio,language="vi-VI")
            text = text.processingTest()
            return text
        except Exception as e:
            messagebox.showerror(title = "Error", message = e)

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
        messagebox.showerror(title = "Error", message = e)

def showAudio():
    pass
