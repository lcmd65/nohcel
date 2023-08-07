import app.view.var
import app.images
import sys
import logging
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
        app = QApplication(sys.argv)
        home = HomeQT()
        home.show()
        sys.exit(app.exec())
    except Exception as e:
        env.root_main = QWidget()
        error_message = str(e)
        QMessageBox.critical(env.root_main, "Error", error_message)

        
def loginViewQT():
    try:
        from app.template.login import LoginUIQT
        app = QApplication(sys.argv)
        login = LoginUIQT()
        login.show()
        sys.exit(app.exec())
    except Exception as e:
        env.root_main = QWidget()
        error_message = str(e)
        QMessageBox.critical(env.root_main, "Error", error_message)

