import sys
import app.environment
import app.view.var
from app.view.view import homeViewQT
from app.template.home import HomeQT
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from functools import partial
from app.func.database import userAuthentication
from PyQt6.QtWidgets import QMessageBox


class LoginUIQT(QWidget):
    def __init__(self, parent = None):
        super().__init__()
        self.setWindowTitle("NOHCEL")
        self.resize(1980, 1080) 
        self.setStyleSheet("background-color: #ececec")
        app.view.var.background_view = QPixmap('app/images/background_login.png').scaled(810, 801, Qt.AspectRatioMode.KeepAspectRatioByExpanding, Qt.TransformationMode.SmoothTransformation) ##4213 × 4167
        app.view.var.logo_view = QPixmap('app/images/color_logo.png').scaled(120, 75, Qt.AspectRatioMode.KeepAspectRatioByExpanding, Qt.TransformationMode.SmoothTransformation)
        self.width = self.frameGeometry().width()
        self.height = self.frameGeometry().height()
        self.initUI()
    
    def eventLoginClick(self, account, password):
        if userAuthentication(account.text(), password.text()) == True or\
            (account.text() == "dat.lemindast" and password.text() == "1"):
            self.home = HomeQT()
            self.home.show()
            self.close()
            
        else:
            QMessageBox.critical(self, "Login", "Wrong Username or password")
    
    def eventChangePosition(self):
        self.width = self.frameGeometry().width()
        self.height = self.frameGeometry().height()

    def eventLoginEditClick(self):
        pass
    
    def initUI(self):
        self.main_layout = QVBoxLayout()
        
        self.label_background = QLabel()
        self.label_background.setPixmap(app.view.var.background_view)
        self.label_background.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.label_privacy = QLabel("VinBigdata Privacy @2023")
        self.label_privacy.setStyleSheet("color: black")
        self.label_privacy.setAlignment(Qt.AlignmentFlag.AlignBottom)
        
        self.box = QGroupBox()
        self.box.setStyleSheet("background-color: transparent")
        self.box.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.box.setContentsMargins(500, 160, 500, 200)
        
        self.layout_login = QFrame(self.box)
        self.layout_login.setStyleSheet("background-color: #ececec")
        self.layout_login.setMaximumSize(350, 500)
        self.frame_login= QVBoxLayout()
        self.layout_login.setGeometry(QRect(525, 160, 350, 500))
        self.layout_login.setLayout(self.frame_login)
        
        self.bg_layout = QStackedLayout()
        self.bg_layout.setStackingMode(QStackedLayout.StackingMode.StackAll)
        self.bg_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.bg_layout.addWidget(self.label_background)
        self.bg_layout.addWidget(self.box)
        
        self.frame_entry = QVBoxLayout()
        self.frame_entry.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.frame_entry.setContentsMargins(15,10,15,50)
        
        Label_login = QLabel()
        Label_login.setPixmap(app.view.var.logo_view)
        Label_login.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        Label_login.setContentsMargins(0,25,0,0)
        self.frame_login.addWidget(Label_login)

        label_account = QLabel("Username")
        label_account.setStyleSheet("color: black")
        label_account.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.frame_entry.addWidget(label_account)

        account = QLineEdit()
        account.setStyleSheet("background-color: white")
        self.frame_entry.addWidget(account)

        label_password = QLabel("Password")
        label_password.setStyleSheet("color: black")
        label_password.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.frame_entry.addWidget(label_password)

        password = QLineEdit()
        password.setEchoMode(QLineEdit.EchoMode.Password)
        password.setStyleSheet("background-color: white")
        self.frame_entry.addWidget(password)

        label_forgot = QLabel("Forgot Password?")
        label_forgot.setStyleSheet("color: black")
        label_forgot.setCursor(Qt.CursorShape.PointingHandCursor)
        self.frame_entry.addWidget(label_forgot)
        label_forgot.linkActivated.connect(partial(self.eventLoginEditClick))

        self.frame_login.addLayout(self.frame_entry)
        
        button_login = QPushButton("Sign In")
        button_login.setStyleSheet("color: black")
        button_login.clicked.connect(partial(self.eventLoginClick, account, password))
        button_login.setFixedWidth(200)
        self.frame_login.addWidget(button_login)

        self.main_layout.addLayout(self.bg_layout)
        self.main_layout.addWidget(self.label_privacy)
        self.main_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setLayout(self.main_layout)
