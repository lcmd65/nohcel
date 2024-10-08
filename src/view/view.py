import src.view.var
import src.images
import sys
import threading
from PyQt6.QtWidgets import (
    QApplication
)
import src.environment as env

def homeViewQT():
    from src.template.home import HomeQT
    home = HomeQT()
    home.show()
        
def loginViewQT():
    from src.template.login import LoginUIQT
    env.src = QApplication(sys.argv)
    login = LoginUIQT()
    login.show()
    env.src.exec()

###

def homeViewThreading():
    th = threading.Thread(target= homeViewQT)
    th.daemon = True
    th.start()

