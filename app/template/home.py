import sys
import random
import typing
import app.view.var
from functools import partial
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
    QFrame
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
        self.nohcel_frame.setMinimumWidth(1000)
        self.nohcel_frame.setLayout(self.nohcel_frame_layout)
        self.nohcel_main_layout.addWidget(self.nohcel_frame)
        
        self.conversation = 
        
        self.nohcel_layout.addWidget(self.label_privacy)
        self.nohcel.setLayout(self.nohcel_layout)
        self.setCentralWidget(self.tabs)

    def eventButtonClickEdit(self):
        self.text.setText("Edit Param")

    def eventButtonClickHelp(self):
        QMessageBox.information(self, "Help", "This is the help message.")

    def _createAction(self):
        self.fileAction = QAction("&File Open", self)
        self.editAction = QAction("&Edit Param", self, triggered=self.eventButtonClickEdit)
        self.helpAction = QAction("$Help Infor", self, triggered=self.eventButtonClickHelp)

    def createLayoutLoginBox(self):
        pass
    
    def setStyleObject(self):
        self.setStyleSheet("background-color: #ececec")
        self.setStyle(self.tabs, "app/template/css/home/tab.css")
        self.setStyle(self.data_view, "app/template/css/home/tree.css")
        self.setStyle(self.nohcel_frame, "app/template/css/home/frame.css")

def main():
    app = QApplication(sys.argv)
    home = HomeQT()
    home.show()
    app.exec()

if __name__ == "__main__":
    main()

# python3 app/template/home.py