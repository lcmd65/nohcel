import app.view.var
import app.images
import sys
import threading
from PyQt6.QtWidgets import (
    QApplication
)
import app.environment as env

def homeViewQT():
    from app.template.home import HomeQT
    home = HomeQT()
    home.show()
        
def loginViewQT():
    from app.template.login import LoginUIQT
    env.app = QApplication(sys.argv)
    login = LoginUIQT()
    login.show()
    env.app.exec()

###

def homeViewThreading():
    th = threading.Thread(target= homeViewQT)
    th.daemon = True
    th.start()

