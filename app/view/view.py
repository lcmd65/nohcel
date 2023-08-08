import app.view.var
import app.images
import sys
from PyQt6.QtWidgets import (
    QWidget,
    QApplication,
    QMessageBox
)
import app.environment as env

"""
qt view
"""

def homeViewQT():
    try:
        from app.template.home import HomeQT
        window = QApplication.instance().activeWindow()
        window.close()
        home = HomeQT()
        home.show()
    except Exception as e:
        env.root_main = QWidget()
        error_message = str(e)
        QMessageBox.critical(env.root_main, "Error", error_message)
        
def loginViewQT():
    try:
        from app.template.login import LoginUIQT
        env.app = QApplication(sys.argv)
        login = LoginUIQT()
        login.show()
        env.app.exec()
    except Exception as e:
        env.root_main = QWidget()
        error_message = str(e)
        QMessageBox.critical(env.root_main, "Error", error_message)

