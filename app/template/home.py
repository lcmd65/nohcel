#############################################################################################################################################################################
# using NLP for processing text from audio record
# using multithreading for except threaeding (process the demon of while loop Qapplication)
# speech_recognition api
import sys
import speech_recognition as sr
import threading
import app.view.var
import app.environment
import gc
from functools import partial
from app.func.func import audioMicroToText, speakTextThread
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

################################################################################################################################################################################
# QObject for Recording with multithreading while running QApplication #########################################################################################################
################################################################################################################################################################################
class VoiceWorker(QObject):
    textRecord = pyqtSignal(str)
    textReply = pyqtSignal(str)
    
    @pyqtSlot()
    def task(self):
        recognizer_engine = sr.Recognizer()
        micro_engine = sr.Microphone()
        try:
            self.textReply.emit("Say something!")
        except:
            pass
        speakTextThread("Say something!")
        try:
            with micro_engine as source:
                try:
                    audio = recognizer_engine.listen(source, phrase_time_limit= 10)
                    value = recognizer_engine.recognize_google(audio)
                    self.textRecord.emit(f"{value}")
                    self.textReply.emit(f"{value}")
                    speakTextThread(str(value))
                    self.textReply.emit("Got it! Now to recognize it...")
                    speakTextThread("Got it! Now to recognize it...")
                except sr.UnknownValueError:
                    self.textReply.emit("Oops")
                    speakTextThread("Oops")
        except Exception as e:
            print(e)

################################################################################################################################################################################
# QMainWindow Home view of Project #############################################################################################################################################
################################################################################################################################################################################
class HomeQT(QMainWindow):
    def __init__(self, parent = None):
        super().__init__()
        
        # parent & event 
        self.setWindowTitle("VinBigData NOHCEL")
        self.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.resize(1980, 1080)
        self.eventCreateAction()
        self.createMenuBar()
        self.eventSetExternalVal()
        self.conversation = QStandardItemModel()
        self.conversation_num_shot = 0
        
        # audio thread in environment variable
        self.initThreadingWorker()

        # toplevel in menu button event clicked
        self.edit_toplevel = None
        self.help_toplevel = None
        self.file_toplevel = None
        self.login_toplevel = None
        
        # ui
        self.initUI()
        self.setObjectStyleCSS()
    
    def closeEvent(self, event):
        if event.type() == QEvent.Type.Close:
            # check if event is not a button close click
            if not event.spontaneous():
                event.ignore() # prevent the program auto exit 
            else:
                reply = QMessageBox.question(self, "Quit?", "Are you sure you want to quit?", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
                if reply == QMessageBox.StandardButton.Yes:
                    event.accept()
                else:
                    event.ignore()
        else:
            event.ignore()
                 
    # external variable background and icon init
    def eventSetExternalVal(self):
        app.view.var.background_view = QPixmap('app/images/background_login.png').scaled(810, 801,\
            Qt.AspectRatioMode.KeepAspectRatioByExpanding,\
            Qt.TransformationMode.SmoothTransformation) ##4213 × 4167
        app.view.var.logo_view = QPixmap('app/images/color_logo.png').scaled(80, 50, \
            Qt.AspectRatioMode.KeepAspectRatioByExpanding, \
            Qt.TransformationMode.SmoothTransformation)

    def setStyle(self, object, css_path):
        with open(css_path,"r") as file:
            style= file.read()
            object.setStyleSheet(style)
        file.close()
    
    def initThreadingWorker(self):
        app.environment.worker = VoiceWorker()
        app.environment.worker.moveToThread(app.environment.thread)
    
    def setIconButtonRecord(self, button, image_path):
        """Sets the icon of the button to the image at the specified path."""
        pixmap = QPixmap(image_path).scaled(50, 50, \
            Qt.AspectRatioMode.KeepAspectRatioByExpanding, \
            Qt.TransformationMode.SmoothTransformation)
        icon = QIcon(pixmap)
        button.setIcon(icon)
        button.setIconSize(pixmap.rect().size())
    
    def eventButtonClickedEdit(self):
        try:     
            from app.template.edit import EditQT
            self.edit_toplevel = EditQT()
            self.edit_toplevel.show()
        except Exception as e:
            QMessageBox.critical(None, "Error", repr(e))
    
    def eventButtonClickedLogout(self):
        self.createLayoutLoginBox()
        gc.collect()

    def eventButtonClickedHelp(self):
        try:
            from app.template.help import HelpQT
            self.help_toplevel = HelpQT()
            self.help_toplevel.show()
        except Exception as e:
            QMessageBox.critical(None, "Error", repr(e))
        
    def eventButtonClickedFile(self):
        try:
            from app.template.file import FileQT
            self.file_toplevel = FileQT()
            self.file_toplevel.show()
        except Exception as e:
            QMessageBox.critical(None, "Error", repr(e))
            
    def eventHomeProcessingLLM(self, text):
        """ task 1         """  
        
        pass
    
    # thử nghiệm API speech to text trên sys
    def eventButtonClickedAudioRecord(self):
        if not self.conversation:
            speakTextThread("Hi!, I am Nohcel, chat Assistant developed by VinBigdata")
        else:
            speakTextThread("How can i help you?")
        text = audioMicroToText()
        self.label_view.clear()
        self.label_view.setText(text)
        self.label_view.adjustSize() 
        item = QStandardItem(text)
        self.conversation.appendRow(item)
        self.temp_data_view.setModel(self.conversation)
        self.eventHomeProcessingLLM(text)

    def eventButtonClickedAudioRecordThread(self):
        threading_new_for_record_loop = threading.Thread(target= partial(self.eventButtonClickedAudioRecordQThread))
        threading_new_for_record_loop.daemon = True
        threading_new_for_record_loop.start()
    
    # test API speech to text trên QThread
    def eventButtonClickedAudioRecordQThread(self):
        app.environment.thread.start()
        app.environment.worker.task()
        app.environment.thread.exec()
        
    def eventCreateAction(self):
        self.file_action = QAction("&File Open", self, triggered = self.eventButtonClickedFile)
        self.edit_action = QAction("&Edit Param", self, triggered= self.eventButtonClickedEdit)
        self.help_action = QAction("$Help Infor", self, triggered= self.eventButtonClickedHelp)
        self.login_action = QAction("&Use other Account", self, triggered= self.eventButtonClickedLogout)

    def createLayoutLoginBox(self):
        # circle import for run login view again from home view
        try:
            from app.template.login import LoginUIQT
            self.login_toplevel = LoginUIQT()
            self.login_toplevel.show()
            self.close()    
        except Exception as e:
            QMessageBox.critical(None, "Error", repr(e))
    
    def createMenuBar(self):
        """ Mennu """
        self.menu_bar = QMenuBar()
        
        self.file_menu = self.menu_bar.addMenu("&File")
        self.edit_menu = self.menu_bar.addMenu("&Edit")
        self.help_menu = self.menu_bar.addMenu("&Help")
        self.login_menu = self.menu_bar.addMenu("&Exit")

        self.file_menu.addAction(self.file_action)
        self.edit_menu.addAction(self.edit_action)
        self.help_menu.addAction(self.help_action)
        self.login_menu.addAction(self.login_action)
        
    def initUI(self): 
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
        self.temp_data_view.setUpdatesEnabled(True)
        self.temp_data_view.setModel(self.conversation)
        self.audio_layout.addWidget(self.temp_data_view)
        
        self.temp_frame = QFrame()
        self.temp_frame_layout = QVBoxLayout()
        self.temp_frame.setLayout(self.temp_frame_layout)
        self.audio_layout.addWidget(self.temp_frame)
        
        self.label_temp_frame = QFrame()
        self.label_temp_frame.setObjectName("label")
        self.label_temp_frame_layout = QVBoxLayout()
        self.label_temp_frame_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.label_temp_frame.setLayout(self.label_temp_frame_layout)
        self.temp_frame_layout.addWidget(self.label_temp_frame)
        
        self.label_view = QLabel()
        self.label_view.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.label_temp_frame_layout.addWidget(self.label_view)
        app.environment.worker.textRecord.connect(lambda textRecord: self.label_view.setText(textRecord))
        
        self.audio_temp_frame = QFrame()
        self.audio_temp_frame_layout = QVBoxLayout()
        self.audio_temp_frame_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.audio_temp_frame.setLayout(self.audio_temp_frame_layout)
        self.temp_frame_layout.addWidget(self.audio_temp_frame)
        
        self.label_temp_input_frame = QFrame()
        self.label_temp_input_frame.setObjectName("label")
        self.label_temp_input_frame_layout = QVBoxLayout()
        self.label_temp_input_frame_layout.setAlignment(Qt.AlignmentFlag.AlignBottom)
        self.label_temp_input_frame.setLayout(self.label_temp_input_frame_layout)
        self.temp_frame_layout.addWidget(self.label_temp_input_frame)
        
        self.label_input = QLabel()
        self.label_input.setAlignment(Qt.AlignmentFlag.AlignBottom)
        self.label_temp_input_frame_layout.addWidget(self.label_input)
        app.environment.worker.textReply.connect(lambda textReply: self.label_view.setText(textReply))
        
        self.button_record = QPushButton()
        self.button_record.clicked.connect(self.eventButtonClickedAudioRecordQThread)
        self.setIconButtonRecord(self.button_record, 'app/images/icons/microphone.png')
        self.audio_temp_frame_layout.addWidget(self.button_record)
        self.audio_temp_frame_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.nohcel_layout.addWidget(self.menu_bar)
        self.nohcel_layout.addWidget(self.label_privacy)
        self.audio_layout.addWidget(self.label_privacy)
        self.nohcel.setLayout(self.nohcel_layout)
        self.setCentralWidget(self.tabs)
    
    # style css setting for all object of home page
    def setObjectStyleCSS(self):
        self.setStyleSheet("background-color: #ececec")
        self.setStyle(self.tabs, "app/template/css/home/tab.css")
        self.setStyle(self.data_view, "app/template/css/home/tree.css")
        self.setStyle(self.nohcel_frame, "app/template/css/home/frame.css")
        self.setStyle(self.nohcel_conversation_view, "app/template/css/home/qlabel_conv.css")
        self.setStyle(self.nohcel_conversation_entry, "app/template/css/home/qline_conv.css")
        self.setStyle(self.temp_data_view, 'app/template/css/home/temp/qframe.css')
        self.setStyle(self.button_record, "app/template/css/home/temp/button.css")
        self.setStyle(self.label_view,  "app/template/css/home/temp/label.css")
        self.setStyle(self.label_input,  "app/template/css/home/temp/label.css")
        self.setStyle(self.label_temp_input_frame, 'app/template/css/home/temp/qframe.css')
        self.setStyle(self.label_temp_frame, 'app/template/css/home/temp/qframe.css')

def main():
    app.environment.application = QApplication([])
    app.environment.thread = QThread()
    home = HomeQT()
    home.show()
    sys.exit(app.environment.application.exec())

if __name__ == "__main__":
    main()

# python3 app/template/home.py