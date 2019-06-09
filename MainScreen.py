from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtPrintSupport import *
import Storage
import os
import sys


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "Journal Application"
        self.left = 50
        self.top = 50
        self.width = 640
        self.height = 480
        self.initUI()

    def printfiles(self, list_widget):
        journal_list = Storage.display_all_entries()
        list_widget.clear()
        for entry in journal_list:
            list_widget.addItem(entry[1])

    def loadEntry(self, list_widget, text_edit):
        journal_list = Storage.display_all_entries()
        current_row = list_widget.currentRow()
        entry_text = journal_list[current_row][2]
        text_edit.setText(entry_text)

    def initUI(self):
        loadAct = QAction('&Load', self)
        loadAct.setShortcut('Ctrl+L')
        loadAct.setStatusTip('Load Note')
        loadAct.triggered.connect(lambda: self.printfiles(_list))

        saveAct = QAction('&Save', self)
        saveAct.setShortcut('Ctrl+S')
        saveAct.setStatusTip('Save Note')

        exitAct = QAction('&Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit Application')
        exitAct.triggered.connect(qApp.quit)

        menubar = self.menuBar()
        filemenu = menubar.addMenu('&File')
        aboutmenu = menubar.addMenu('&About')

        filemenu.addAction(loadAct)
        filemenu.addAction(saveAct)
        filemenu.addAction(exitAct)

        textedit = QTextEdit()

        _list = QListWidget()
        self.printfiles(_list)
        _list.itemDoubleClicked.connect(lambda: self.loadEntry(_list, textedit))

        splitter = QSplitter(Qt.Horizontal)
        splitter.addWidget(_list)
        splitter.addWidget(textedit)

        splitter.setSizes([50, 200])

        self.setCentralWidget(splitter)

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
