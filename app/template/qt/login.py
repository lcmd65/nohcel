import sys
import app.environment
import app.view.var
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from functools import partial
from app.view.view import loginEditView
from app.view.view import homeView
from app.func.database import userAuthentication
from PyQt6.QtWidgets import QMessageBox


class LoginUIQT(QMainWindow):
    def __init__(self, parent):
        super().__init__(self, parent)
        app.view.var.background_view = QPixmap('app/images/background_login.png').resize((1092, 1080)) ##4213 × 4167
        app.view.var.logo_view = QPixmap('app/images/color_logo.png').resize((40, 25))
        self.initUI()
    
    def eventLoginClick(self, account, password):
        if userAuthentication(account.text(), password.text()) == True:
            app.tkinter.environment.root_main.destroy()
            homeView()
        else:
            QMessageBox.critical(self, "Login", "Wrong Username or password")

    def eventLoginEditClick(self):
        loginEditView()
    
    def initUI(self):
        self.setWindowTitle("NOHCEL")
        self.resize(600, 800)
        self.setStyleSheet("background-color: #ececec")

        self.label_privacy = QLabel("VinBigdata Privacy @2023")
        self.label_privacy.setStyleSheet("color: black")
        self.label_privacy.setAlignment(Qt.AlignmentFlag.AlignBottom)
        self.label_privacy.move(0, 0)

        self.notebook = QTabWidget()
        self.notebook.addTab(QWidget(), "     LOGIN     ")

        self.frame_login = QWidget()
        self.notebook.setTabText(0, "Login")

        Label_login = QLabel()
        Label_login.setPixmap(app.view.var.logo_view)
        self.frame_login.layout().addWidget(Label_login)

        label_account = QLabel("Username")
        label_account.setStyleSheet("color: black")
        self.frame_login.layout().addWidget(label_account)

        account = QLineEdit()
        self.frame_login.layout().addWidget(account)

        label_password = QLabel("Password")
        label_password.setStyleSheet("color: black")
        self.frame_login.layout().addWidget(label_password)

        password = QLineEdit()
        password.setEchoMode(QLineEdit.Password)
        self.frame_login.layout().addWidget(password)

        label_forgot = QLabel("Forgot Password?")
        label_forgot.setStyleSheet("color: black")
        label_forgot.setCursor(Qt.PointingHandCursor)
        self.frame_login.layout().addWidget(label_forgot)
        label_forgot.linkActivated.connect(partial(self.eventLoginEditClick))

        button_login = QPushButton("Sign In")
        button_login.setStyleSheet("color: black")
        button_login.clicked.connect(partial(self.eventLoginClick, account, password))
        self.frame_login.layout().addWidget(button_login)

        self.setLayout(self.notebook.layout())

def main():
    app = QApplication(sys.argv)
    login = LoginUIQT()
    login.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

# python3 app/template/qt/login.py