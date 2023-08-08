import sys
import random
import typing
import app.view.var
from functools import partial
from PyQt6.QtWidgets import (
    QHBoxLayout,
    QStyle,
    QVBoxLayout,
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

class HomeQT(QMainWindow):
    def __init__(self, parent = None):
        super().__init__()
        self.setWindowTitle("VinBigData NOHCEL")
        self.resize(1980, 1080)
        self._createAction()
        app.view.var.background_view = QPixmap('app/images/background_login.png').scaled(810, 801, Qt.AspectRatioMode.KeepAspectRatioByExpanding, Qt.TransformationMode.SmoothTransformation) ##4213 × 4167
        app.view.var.logo_view = QPixmap('app/images/color_logo.png').scaled(80, 50, Qt.AspectRatioMode.KeepAspectRatioByExpanding, Qt.TransformationMode.SmoothTransformation)
        self.width = self.frameGeometry().width()
        self.height = self.frameGeometry().height()
        self.initUI()
        self.setStyle()

    def initUI(self):
        """ Mennu """
        self.menu_bar = QMenuBar()
        
        file_menu = self.menu_bar.addMenu("&File")
        edit_menu = self.menu_bar.addMenu("&Edit")
        help_menu = self.menu_bar.addMenu("&Help")

        file_menu.addAction(self.fileAction)
        edit_menu.addAction(self.editAction)
        help_menu.addAction(self.helpAction)
        
        """ label and logo """
        self.label_background = QLabel()
        self.label_background.setPixmap(app.view.var.background_view)
        self.label_background.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.label_privacy = QLabel("VinBigdata Privacy @2023")
        self.label_privacy.setStyleSheet("color: black")
        self.label_privacy.setAlignment(Qt.AlignmentFlag.AlignBottom)
        
        """ tab """
        self.tabs = QTabWidget()
        self.tabs.setTabPosition(QTabWidget.TabPosition.North)
        self.tabs.setTabShape(QTabWidget.TabShape.Rounded)
        self.tabs.setMovable(True)
        self.nohcel = QWidget()
        self.nohcel_layout = QHBoxLayout()
        
        
        self.audio_record = QWidget()
        
        for tab,  name in zip([self.nohcel, self.audio_record], ["NOHCEL", "Speech to Text"]):
            self.tabs.addTab(tab, name)
        
        
        self.nohcel_layout.addWidget(self.label_privacy)
        self.nohcel.setLayout(self.nohcel_layout)
        
        self.setCentralWidget(self.tabs)
    
    def setStyle(self):
        with open("app/template/css/home.css","r") as file:
            self.tabs.setStyleSheet(file.read())

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
    app = QApplication(sys.argv)
    home = HomeQT()
    home.show()
    app.exec()

if __name__ == "__main__":
    main()

# python3 app/template/home.py