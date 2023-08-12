from PyQt6.QtWidgets import *
from PyQt6.QtGui import *

class FileQT(QMainWindow):
    def __init__(self, parent = None):
        super().__init__()
        self.setWindowTitle("File")
        self.resize(500, 800)
        self.initUI()
        self.setStyleObject()
        
    def initUI(self):
        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)
        
        self.information = QTextEdit()
        self.main_layout.addWidget(self.information)
        
        self.button = QPushButton()
        self.main_layout.addWidget(self.button)
    
    def setStyleObject(self):
        pass