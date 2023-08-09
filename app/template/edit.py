from PyQt6.QtWidgets import *
from PyQt6.QtGui import *

class EditQT(QMainWindow):
    def __init__(self, parent = None):
        super().__init__()
        self.setWindowTitle("Edit")
        self.resize(990, 540)
        self._createAction()
        self.setExternalVal()
        self.initUI()
        self.setStyleObject()
    
    def setExternalVal(self):
        pass
    
    def initUI(self):
        self.main_layout = QFormLayout()
        self.main_layout.addItem()