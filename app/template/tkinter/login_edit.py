from tkinter import *
from tkinter import messagebox
from functools import partial
from app.func.database import userAuthenticationNonePass

class LoginEdit(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()
    
    def eventButtonCLick(self, account, email, newpass, confirm_newpass):
        try:
            if newpass.get() == confirm_newpass.get():
                try:
                    if userAuthenticationNonePass(account.get(), email.get()) == True:
                        pass 
                    """ task here"""
                except Exception as e:
                    messagebox.showerror(title = "Error", message = e)
        except Exception as e:
            messagebox.showerror(title = "Error", message = e)
        
    def initUI(self):
        self.parent.title("Edit")
        self.pack(fill = BOTH, side = TOP) 
    
        self.label_privacy  = Label(self.parent, text  = " Nohcel privacy 2023@")
        self.label_privacy.pack(side = LEFT)
        
        frame_list = [None for _ in range(5)]
        
        for index in range(5):
            frame_list[index] = Frame(self)
            frame_list[index].pack(side= TOP, fill = X, padx= 5, pady = 5)
        frame_list[4] = Frame(self)
        frame_list[4].pack(side= RIGHT, fill = X, padx= 5, pady = 5)
            
        label_account = Label(frame_list[0], text = " account")
        label_account.pack(side = LEFT)
        
        entry_account = Entry(frame_list[0])
        entry_account.pack(side = RIGHT, fill = X)
        
        label_email = Label(frame_list[1], text = "email")
        label_email.pack(side = LEFT)
        
        entry_email = Entry(frame_list[1])
        entry_email.pack(side = RIGHT, fill = X)
        
        label_newpass = Label(frame_list[2], text = " account")
        label_newpass.pack(side = LEFT)
        
        entry_newpass = Entry(frame_list[2])
        entry_newpass.pack(side = RIGHT, fill = X)
        
        label_confirm_newpass = Label(frame_list[3], text = " account")
        label_confirm_newpass.pack(side = LEFT)
        
        entry_confirm_newpass  = Entry(frame_list[3])
        entry_confirm_newpass.pack(side = RIGHT, fill = X)
        
        button_run = Button(frame_list[4], text = "OK", width= 10, command= partial(self.eventButtonCLick, entry_account, entry_email, entry_newpass, entry_confirm_newpass))
        button_run.pack(side = RIGHT)
        