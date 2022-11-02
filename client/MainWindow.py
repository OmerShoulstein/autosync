import os
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import MainWindowLogic


class UiMainWindow(object):
    def setup_ui(self, MainWindow, username, socket, listener):
        self.line_style_sheet = (
            "QLineEdit {padding-left: 5px;padding-right: 5px;margin: 2px;background-color: rgb(240, 240, 240);"
            "border-radius: 10px;}")
        self.username = username
        self.logic = MainWindowLogic.MainWindowLogic(self, username, socket, listener)
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(960, 540)
        MainWindow.setMinimumSize(QtCore.QSize(960, 540))
        MainWindow.setMaximumSize(QtCore.QSize(960, 540))
        MainWindow.setFocusPolicy(QtCore.Qt.StrongFocus)
        MainWindow.setStyleSheet("background-color: rgb(244, 250, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(-1, 0, 200, 145))
        self.logo.setObjectName("logo")
        self.username_label = QtWidgets.QLabel(self.centralwidget)
        self.username_label.setGeometry(QtCore.QRect(190, 110, 280, 50))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(20)
        self.username_label.setFont(font)
        self.username_label.setStyleSheet("background-color: rgba(0, 0, 0,0);")
        self.username_label.setAlignment(QtCore.Qt.AlignCenter)
        self.username_label.setObjectName("username_label")
        self.selection_label = QtWidgets.QLabel(self.centralwidget)
        self.selection_label.setGeometry(QtCore.QRect(320, 240, 320, 50))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(20)
        self.selection_label.setFont(font)
        self.selection_label.setStyleSheet("background-color: rgba(0, 0, 0,0);")
        self.selection_label.setAlignment(QtCore.Qt.AlignCenter)
        self.selection_label.setObjectName("selection_label")
        self.browse_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.browse_edit.setGeometry(QtCore.QRect(280, 290, 400, 50))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setFamily("Lato")
        self.browse_edit.setFont(font)
        self.browse_edit.setStyleSheet("QLineEdit{\n"
                                       "    padding-left: 5px;\n"
                                       "    padding-right: 5px;\n"
                                       "    margin: 2px;\n"
                                       "    background-color: rgb(240, 240, 240);\n"
                                       "    border-radius: 10px\n"
                                       "}\n"
                                       "QLineEdit:hover\n"
                                       "{\n"
                                       "    padding-left: 5px;\n"
                                       "    padding-right: 5px;\n"
                                       "    margin: 0px;\n"
                                       "     border-style: solid;\n"
                                       "    border-width: 2px;\n"
                                       "    border-color: rgb(200, 200, 200);\n"
                                       "}\n"
                                       "QLineEdit:focus {\n"
                                       "    padding-left: 5px;\n"
                                       "    padding-right: 5px;\n"
                                       "    margin: 0px;\n"
                                       "    border-style: solid;\n"
                                       "    border-width: 2px;\n"
                                       "    border-color:  rgb(0, 0, 255);\n"
                                       "}")
        self.browse_edit.setReadOnly(True)
        self.browse_edit.setObjectName("browse_edit")
        self.browse_button = QtWidgets.QPushButton(self.centralwidget)
        self.browse_button.setGeometry(QtCore.QRect(340, 430, 150, 65))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(26)
        self.browse_button.setFont(font)
        self.browse_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.browse_button.setStyleSheet("background-color: rgb(77, 183, 249);\n"
                                         "color: rgb(255, 255, 255);\n"
                                         "border-radius:10px;")
        self.browse_button.setObjectName("browse_button")
        self.sync_button = QtWidgets.QPushButton(self.centralwidget)
        self.sync_button.setGeometry(QtCore.QRect(580, 430, 60, 65))
        self.sync_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.sync_button.setFocusPolicy(QtCore.Qt.TabFocus)
        self.sync_button.setStyleSheet("background-image: url(:/photos/sync_symbol.svg);\n"
                                       "image: url(:/photos/sync_symbol.svg);\n"
                                       "border-radius:1px;")
        self.sync_button.setText("")
        self.sync_button.setObjectName("sync_button")
        self.select_folder_label = QtWidgets.QLabel(self.centralwidget)
        self.select_folder_label.setGeometry(QtCore.QRect(350, 340, 280, 50))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(18)
        self.select_folder_label.setFont(font)
        self.select_folder_label.setStyleSheet("color: rgb(239, 41, 41);\n"
                                               "background-color: rgba(0, 0, 0,0);")
        self.select_folder_label.setText("")
        self.select_folder_label.setAlignment(QtCore.Qt.AlignCenter)
        self.select_folder_label.setObjectName("select_folder_label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslate_ui(MainWindow)
        self.sync_button.clicked.connect(self.logic.start_sync)
        self.browse_button.clicked.connect(self.logic.browse)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslate_ui(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.logo.setText(
            _translate("MainWindow", "<html><head/><body><p><img src=\":/photos/logo.png\"/></p></body></html>"))
        self.username_label.setText(_translate("MainWindow", "Hello " + self.username))
        self.selection_label.setText(_translate("MainWindow", "Select a folder to sync"))
        self.browse_button.setText(_translate("MainWindow", "browse"))
        self.sync_button.setToolTip(_translate("MainWindow", "<html><head/><body><p>Start syncing</p></body></html>"))
        self.sync_button.setWhatsThis(
            _translate("MainWindow", "<html><head/><body><p><img src=\":/photos/sync_symbol.png\"/></p></body></html>"))
        user_path = "user_folders/" + self.username
        if os.path.exists(user_path):
            with open(user_path, 'r') as file:
                self.browse_edit.setText(file.read())


import photos_rc

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = UiMainWindow()
    ui.setup_ui(MainWindow, "omer")
    MainWindow.show()
    sys.exit(app.exec_())
