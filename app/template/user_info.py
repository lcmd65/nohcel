import app.view.var
from func.database import userAuthenticationNonePass
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from functools import partial

class PasswordChange(QMainWindow):
    def __init__(self, parent = None):
        super().__init__()
        self.setWindowTitle("Change Password")
        self.resize(990, 540)
        self.setExternalVal()
        self.initUI()
        self.setStyleObject()
    
    def eventSetExternalVal(self):
        pass

    def setStyle(self, object, css_path):
        with open(css_path,"r") as file:
            style= file.read()
            object.setStyleSheet(style)
        file.close()
    
    def setExternalVal(self):
        pass
    
    def initUI(self):
        self.main_layout = QVBoxLayout()
        
        self.main_form = QFormLayout()
        self.main_layout.addLayout(self.main_form)
        
        self.main_form.addRow('New Password:', QLineEdit(self, echoMode=QLineEdit.EchoMode.Password))
        self.main_form.addRow('Confirm Password:', QLineEdit(self, echoMode=QLineEdit.EchoMode.Password))

        self.main_form.addRow(QPushButton('Sign Up'))        
    
    def setStyleObject(self):
        pass
    
class UserChange(QMainWindow):
    def __init__(self, parent = None):
        super().__init__()
        self.setWindowTitle("Forgot Password")
        self.resize(990, 540)
        
        self.changepass_toplevel = None
        
        self.setExternalVal()
        self.initUI()
        self.setStyleObject()
    
    def eventSetExternalVal(self):
        app.view.var.background_view = QPixmap('app/images/background_login.png').scaled(810, 801,\
            Qt.AspectRatioMode.KeepAspectRatioByExpanding,\
            Qt.TransformationMode.SmoothTransformation) ##4213 × 4167
        app.view.var.logo_view = QPixmap('app/images/color_logo.png').scaled(80, 50, \
            Qt.AspectRatioMode.KeepAspectRatioByExpanding, \
            Qt.TransformationMode.SmoothTransformation)

    def setStyle(self, object, css_path):
        with open(css_path,"r") as file:
            style= file.read()
            object.setStyleSheet(style)
        file.close()
    
    def setExternalVal(self):
        pass
    
    def eventButtonClickedChangePass(self):
        pass
    
    def initUI(self):
        self.main_layout = QVBoxLayout()
        
        self.main_form = QFormLayout()
        self.main_layout.addLayout(self.main_form)
        
        self.user = QLineEdit()
        self.email = QLineEdit()
        self.phone = QLineEdit()
        self.button = QPushButton()
        self.button.clicked.connect(partial(self.eventButtonClickedChangePass, self.user, self.email, self.phone))
        
        self.main_form.addRow('Username:', self.user)
        self.main_form.addRow('Email:', self.email)
        self.main_form.addRow('Phone:', self.phone)
        self.main_form.addRow(self.button)  
        
        self.setLayout(self.main_layout)      
    
    def setStyleObject(self):
        pass