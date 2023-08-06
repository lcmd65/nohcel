from tkinter import * 
from tkinter import messagebox, ttk, Button
import json

class EditEnv(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()
    
    def envOpen(self):
        with open("app/embedded.json") as jsonfile:
            data = json.loads(jsonfile)
                    
    def initUI(self):
        self.parent.title("Edit Parameter")
        self.pack(fill = BOTH, side = TOP)
        
        label_privacy = Label(self.parent, text = "lcmd privacy @2023")
        label_privacy.pack(side = LEFT)
        
        frame_list = [None for _ in range()]