from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from functools import partial
from func.database import userSender

class HelpQT(QMainWindow):
    def __init__(self, parent = None):
        super().__init__()
        self.setWindowTitle("Help")
        self.resize(500, 800)
        self.initUI()
        self.setStyleObject()
    
    @pyqtSlot
    def eventButtonClickedHelp(self, information):
        userSender(information)        
         
    def initUI(self):
        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)
        
        self.information = QTextEdit()
        self.main_layout.addWidget(self.information)
        
        self.button = QPushButton()
        self.button.clicked.connect(partial(self.eventButtonClickedHelp))
        self.main_layout.addWidget(self.button)
    
    def setStyleObject(self):
        pass