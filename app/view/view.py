import app.view.var
import app.images
import sys
from tkinter import *
from tkinter import messagebox
from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QPixmap
from PIL import ImageTk, Image
import app.environment as env

"""
tkinter view
"""
def loginView():
    try:
        from app.template.tkinter.login import LoginUI
        env.root_main = Tk()
        env.root_main.geometry("1000x1000+100+100")
        app.view.var.background_view = ImageTk.PhotoImage(Image.open('app/images/background_login.png').resize((1092, 1080))) ##4213 × 4167
        app.view.var.logo_view = ImageTk.PhotoImage(Image.open('app/images/color_logo.png').resize((120, 75)))
        application = LoginUI(env.root_main)
        env.root_main.mainloop()
    except Exception as e:
        messagebox.showerror(title = "Error", message = e)
        

def homeView():
        from app.template.tkinter.home import Home
        env.root_main = Tk()
        env.root_main.geometry("1000x1000+100+100")
        app.view.var.background_view = ImageTk.PhotoImage(Image.open('app/images/background_login.png').resize((1092, 1080))) ##4213 × 4167
        app.view.var.logo_view = ImageTk.PhotoImage(Image.open('app/images/color_logo.png').resize((40, 25)))
        application = Home(env.root_main)
        env.root_main.mainloop()
    
def helpView():
    try:
        from app.template.tkinter.help import Help
        env.root_temp = Toplevel()
        env.root_temp.geometry("400x600+100+100")
        app.vew.var.background_view_toplevel = ImageTk.PhotoImage(Image.open('app/images/background_login.png').resize((1092, 1080)))
        app_temp = Help(env.root_temp)
        env.root_temp.mainloop()
    except Exception as e:
        messagebox.showerror(title = "Error", message = e)

def loginEditView():
    try:
        from app.template.tkinter.login_edit import LoginEdit
        env.root_temp = Toplevel()
        env.root_temp.geometry("1000x1000+100+100")
        application_edit = LoginEdit(env.root_temp)
        env.root_temp.mainloop()
    except Exception as e:
        messagebox.showerror(title = "Error", message = e)

def editView():
    try:
        from app.template.tkinter.edit import EditEnv
        env.root_temp = Tk()
        env.root_temp.geometry("1000x1000+100+100")
        application_edit = EditEnv(env.root_temp)
        env.root_temp.mainloop()
    except Exception as e:
        messagebox.showerror(title = "Error", message = e)

"""
qt view
"""

def homeViewQT():
    try:
        from app.template.qt.home import HomeQT
        app = QApplication(sys.argv)
        home = HomeQT(env.root)
        home.show()
        sys.exit(app.exec())
    except Exception as e:
        messagebox.showerror(title = "Error", message = e)
        
def loginViewQT():
    try:
        from app.template.qt.login import LoginUIQT
        app = QApplication(sys.argv)
        login = LoginUIQT(env.root)
        login.show()
        sys.exit(app.exec())
    except Exception as e:
        messagebox.showerror(title = "Error", message = e)
