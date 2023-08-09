from PyQt6.QtWidgets import *
from PyQt6 import QtGui, QtCore, QtWebEngineWidgets
import sys

class Main(QMainWindow):
    def __init__(self):
        super().__init__()

        # --------------
        # central widget
        # --------------
        self.layout = QGridLayout()
        container   = QWidget()
        container.setLayout(self.layout)
        self.setCentralWidget(container)

        # --------------
        # webengine view
        # --------------
        self.browser = QtWebEngineWidgets.QWebEngineView(self)
        self.browser.setMaximumSize(0, 0)

        # -----------------------
        # push button to add tabs
        # -----------------------
        btn = QPushButton('Add Tab')
        btn.released.connect(self.addTab)
        self.layout.addWidget(btn)

        # ----------
        # tab widget
        # ----------
        self.tabCount = 0
        self.tabs = QTabWidget()
        self.tabs.setTabsClosable(True)
        self.layout.addWidget(self.tabs)

    def addTab(self):
        # -------------
        # main elements
        # -------------
        layout = QVBoxLayout()
        container = QWidget()
        container.setLayout(layout)

        # ---------
        # add label
        # ---------
        tabBrowser = QtWebEngineWidgets.QWebEngineView(self)
        txt = '''
        <html>
        Hello World!
        </html>
        '''
        tabBrowser.setHtml(txt)
        layout.addWidget(tabBrowser)

        # -------
        # add tab
        # -------
        self.tabs.addTab(container, str(self.tabCount))
        self.tabCount += 1


if __name__ == '__main__':

    # -----------------
    # exception handler
    # -----------------
    def exception_hook(exc_type, exc_value, tb):
        sys.__excepthook__(exc_type, exc_value, tb)
        main.close()
        sys.exit(1)
    sys.excepthook = exception_hook

    # -----------
    # run program
    # -----------
    app = QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec())