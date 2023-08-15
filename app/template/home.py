import sys
import random
import typing
import app.view.var
from functools import partial
from app.func.func import audioMicroToText
from PyQt6.QtWidgets import (
    QHBoxLayout,
    QTreeView,
    QStyle,
    QVBoxLayout,
    QApplication,
    QMenuBar,
    QLabel,
    QMainWindow,
    QPushButton,
    QTabWidget,
    QWidget,
    QMessageBox,
    QFrame,
    QLineEdit
)
from PyQt6.QtGui import *
from PyQt6.QtCore import *

class HomeQT(QMainWindow):
    def __init__(self, parent = None):
        super().__init__()
        self.setWindowTitle("VinBigData NOHCEL")
        self.resize(1980, 1080)
        self._createAction()
        self.setExternalVal()
        self.initUI()
        self.setStyleObject()
        self._edit = None
        self._help = None
        self._file = None

    def setExternalVal(self):
        app.view.var.background_view = QPixmap('app/images/background_login.png').scaled(810, 801, Qt.AspectRatioMode.KeepAspectRatioByExpanding, Qt.TransformationMode.SmoothTransformation) ##4213 × 4167
        app.view.var.logo_view = QPixmap('app/images/color_logo.png').scaled(80, 50, Qt.AspectRatioMode.KeepAspectRatioByExpanding, Qt.TransformationMode.SmoothTransformation)

    def setStyle(self, object, css_path):
        with open(css_path,"r") as file:
            style= file.read()
            object.setStyleSheet(style)
        file.close()
    
    def set_icon(self, button, image_path):
        """Sets the icon of the button to the image at the specified path."""
        pixmap = QPixmap(image_path).scaled(50, 50, Qt.AspectRatioMode.KeepAspectRatioByExpanding, Qt.TransformationMode.SmoothTransformation)
        icon = QIcon(pixmap)
        button.setIcon(icon)
        button.setIconSize(pixmap.rect().size())
    
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
        
        """ tab1 """
        self.nohcel = QWidget()
        self.nohcel_layout = QVBoxLayout()
        self.nohcel_main_layout = QHBoxLayout()
        self.nohcel_layout.addLayout(self.nohcel_main_layout)

        self.audio_record = QWidget()
        self.audio_layout = QHBoxLayout()
        
        for tab,  name in zip([self.nohcel, self.audio_record], ["NOHCEL", "Speech to Text"]):
            self.tabs.addTab(tab, name)

        self.data_view = QTreeView()
        self.data_view.setMinimumWidth(150)
        self.data_view.setMaximumWidth(250)
        self.nohcel_main_layout.addWidget(self.data_view)
        
        self.nohcel_frame = QFrame()
        self.nohcel_frame_layout = QVBoxLayout()
        self.nohcel_frame.setLayout(self.nohcel_frame_layout)
        self.nohcel_main_layout.addWidget(self.nohcel_frame)
        
        self.nohcel_conversation_view = QLabel()
        self.nohcel_frame_layout.addWidget(self.nohcel_conversation_view)
        
        self.nohcel_conversation_entry = QLineEdit()
        self.nohcel_conversation_entry.setPlaceholderText("Nhập câu lệnh tại đây")
        self.nohcel_frame_layout.addWidget(self.nohcel_conversation_entry)
        
        self.audio_record.setLayout(self.audio_layout)
        self.temp_data_view = QTreeView()
        self.temp_data_view.setMinimumWidth(150)
        self.temp_data_view.setMaximumWidth(250)
        self.audio_layout.addWidget(self.temp_data_view)
        
        self.temp_frame = QFrame()
        self.temp_frame_layout = QVBoxLayout()
        self.temp_frame.setLayout(self.temp_frame_layout)
        self.audio_layout.addWidget(self.temp_frame)
        
        self.audio_temp_frame = QFrame()
        self.audio_temp_frame_layout = QVBoxLayout()
        self.audio_temp_frame_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.audio_temp_frame.setLayout(self.audio_temp_frame_layout)
        self.temp_frame_layout.addWidget(self.audio_temp_frame)
        
        self.label_temp_frame = QFrame()
        self.label_temp_frame.setObjectName("label")
        self.label_temp_frame_layout = QVBoxLayout()
        self.label_temp_frame_layout.setAlignment(Qt.AlignmentFlag.AlignBottom)
        self.label_temp_frame.setLayout(self.label_temp_frame_layout)
        self.temp_frame_layout.addWidget(self.label_temp_frame)
        
        self.label_view = QLabel()
        self.label_view.setAlignment(Qt.AlignmentFlag.AlignBottom)
        self.label_temp_frame_layout.addWidget(self.label_view)
        
        self.button_record = QPushButton()
        self.button_record.clicked.connect(partial(self.eventClickButtonAudioRecord, self.label_view))
        self.set_icon(self.button_record, 'app/images/icons/microphone.png')
        self.audio_temp_frame_layout.addWidget(self.button_record)
        self.audio_temp_frame_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.nohcel_layout.addWidget(self.menu_bar)
        self.nohcel_layout.addWidget(self.label_privacy)
        self.audio_layout.addWidget(self.label_privacy)
        self.nohcel.setLayout(self.nohcel_layout)
        self.setCentralWidget(self.tabs)

    def eventButtonClickEdit(self):
        try:
            from app.template.edit import EditQT
            self._edit = EditQT()
            self._edit.show()
        except Exception as e:
            QMessageBox.critical(self, "Edit", str(e))

    def eventButtonClickHelp(self):
        try:
            from app.template.help import HelpQT
            self._help = HelpQT()
            self._help.show()
        except Exception as e:
            QMessageBox.critical(self, "Edit", str(e))
        
    def eventButtonClickFile(self):
        try:
            from app.template.file import FileQT
            self._file = FileQT()
            self._file.show()
        except Exception as e:
            QMessageBox.critical(self, "Edit", str(e))

    def eventClickButtonAudioRecord(self, label):
        text = audioMicroToText()
        label.clear()
        label.setText(text)
        
    def _createAction(self):
        self.fileAction = QAction("&File Open", self, triggered = self.eventButtonClickFile)
        self.editAction = QAction("&Edit Param", self, triggered= self.eventButtonClickEdit)
        self.helpAction = QAction("$Help Infor", self, triggered= self.eventButtonClickHelp)

    def createLayoutLoginBox(self):
        
        pass
    
    def setStyleObject(self):
        self.setStyleSheet("background-color: #ececec")
        self.setStyle(self.tabs, "app/template/css/home/tab.css")
        self.setStyle(self.data_view, "app/template/css/home/tree.css")
        self.setStyle(self.nohcel_frame, "app/template/css/home/frame.css")
        self.setStyle(self.nohcel_conversation_view, "app/template/css/home/qlabel_conv.css")
        self.setStyle(self.nohcel_conversation_entry, "app/template/css/home/qline_conv.css")
        self.setStyle(self.temp_data_view, 'app/template/css/home/temp/qframe.css')
        self.setStyle(self.button_record, "app/template/css/home/temp/button.css")
        self.setStyle(self.label_view,  "app/template/css/home/temp/label.css")
        self.setStyle(self.label_temp_frame, 'app/template/css/home/temp/qframe.css')

def main():
    app = QApplication(sys.argv)
    home = HomeQT()
    home.show()
    app.exec()

if __name__ == "__main__":
    main()

# python3 app/template/home.py