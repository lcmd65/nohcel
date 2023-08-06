import sys
import random
import app.view.var
from functools import partial
from PyQt6.QtWidgets import (
    QApplication,
    QMenuBar,
    QLabel,
    QMainWindow,
    QPushButton,
    QTabWidget,
    QWidget,
    QMessageBox
)
from PyQt6.QtGui import *
from PyQt6.QtCore import *
import PyQt6.QtQuick
class HomeQT(QMainWindow):
    def __init__(self, parent):
        super().__init__(parent)
        self.setWindowTitle("VinBigData NOHCEL")
        self.resize(400, 200)
        self._createAction()
        app.view.var.background_view = QPixmap('app/images/background_login.png').resize((1092, 1080)) ##4213 × 4167
        app.view.var.logo_view = QPixmap('app/images/color_logo.png').resize((40, 25))
        self.initUI()

    def initUI(self):
        self.menu_bar = QMenuBar()
        file_menu = self.menu_bar.addMenu("&File")
        edit_menu = self.menu_bar.addMenu("&Edit")
        help_menu = self.menu_bar.addMenu("&Help")

        file_menu.addAction(self.fileAction)
        edit_menu.addAction(self.editAction)
        help_menu.addAction(self.helpAction)
        
        tabs = QTabWidget()
        tabs.setTabPosition(QTabWidget.TabPosition.North)
        tabs.setMovable(True)

        self.nohcel = QWidget(self)
        self.audio_record = QWidget(self)
        
        for tab,  name in zip([self.nohcel, self.audio_record], ["NOHCEL", "Speech to Text"]):
            tabs.addTab(tab, name)
            
        self.setCentralWidget(tabs)
        

    def eventButtonClickEdit(self):
        self.text.setText("Edit Param")

    def eventButtonClickHelp(self):
        QMessageBox.information(self, "Help", "This is the help message.")

    def _createAction(self):
        self.fileAction = QAction("&File Open", self)
        self.editAction = QAction("&Edit Param", self, triggered=self.eventButtonClickEdit)
        self.helpAction = QAction("$Help Infor", self, triggered=self.eventButtonClickHelp)

    def _createLayoutLoginBox(self):
        pass
        

def main():
    root = None
    app = QApplication(sys.argv)
    home = HomeQT(root)
    home.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()

# python3 app/template/qt/home.py