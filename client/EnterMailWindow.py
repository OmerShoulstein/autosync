from PyQt5 import QtCore, QtGui, QtWidgets
from EnterMailWindowLogic import EnterMailWindowLogic


class UiEnterMailWindow(object):
    def setup_ui(self, MainWindow, socket, listener):
        self.logic = EnterMailWindowLogic(self, socket, listener)
        self.window = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(960, 540)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(960, 540))
        MainWindow.setMaximumSize(QtCore.QSize(960, 540))
        MainWindow.setStyleSheet("background-color: rgb(244, 250, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(-1, 0, 200, 145))
        self.logo.setObjectName("logo")
        self.title_label = QtWidgets.QLabel(self.centralwidget)
        self.title_label.setGeometry(QtCore.QRect(300, 90, 360, 50))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(20)
        self.title_label.setFont(font)
        self.title_label.setStyleSheet("background-color: rgba(0, 0, 0,0);")
        self.title_label.setAlignment(QtCore.Qt.AlignCenter)
        self.title_label.setObjectName("title_label")
        self.mail_edit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.mail_edit_2.setGeometry(QtCore.QRect(310, 290, 340, 50))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(20)
        self.mail_edit_2.setFont(font)
        self.mail_edit_2.setStyleSheet("QLineEdit{\n"
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
        self.mail_edit_2.setReadOnly(False)
        self.mail_edit_2.hide()
        self.mail_edit_2.setObjectName("mail_edit_2")
        self.reset_password_button = QtWidgets.QPushButton(self.centralwidget)
        self.reset_password_button.setGeometry(QtCore.QRect(340, 400, 280, 50))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(20)
        self.reset_password_button.setFont(font)
        self.reset_password_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.reset_password_button.setStyleSheet("background-color: rgb(77, 183, 249);\n"
                                                 "alternate-background-color: rgb(77, 183, 249);\n"
                                                 "color: rgb(255, 255, 255);\n"
                                                 "border-radius:10px;")
        self.reset_password_button.setObjectName("reset_password_button")
        self.back_to_login = QtWidgets.QPushButton(self.centralwidget)
        self.back_to_login.setGeometry(QtCore.QRect(370, 470, 220, 40))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(20)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setKerning(False)
        self.back_to_login.setFont(font)
        self.back_to_login.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.back_to_login.setStyleSheet("border: none;\n"
                                         "background-color: rgba(0, 0, 0,0);\n"
                                         "color: rgb(77, 183, 249);")
        self.back_to_login.setObjectName("back_to_login")
        self.invalid_label = QtWidgets.QLabel(self.centralwidget)
        self.invalid_label.setGeometry(QtCore.QRect(295, 330, 370, 50))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(14)
        self.invalid_label.setFont(font)
        self.invalid_label.setStyleSheet("color: rgb(239, 41, 41);\n"
                                         "background-color: rgba(0, 0, 0,0);")
        self.invalid_label.setText("")
        self.invalid_label.setAlignment(QtCore.Qt.AlignCenter)
        self.invalid_label.setObjectName("invalid_label")
        self.title_label2 = QtWidgets.QLabel(self.centralwidget)
        self.title_label2.setGeometry(QtCore.QRect(0, 130, 960, 50))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(14)
        self.title_label2.setFont(font)
        self.title_label2.setStyleSheet("background-color: rgba(0, 0, 0,0);")
        self.title_label2.setText("")
        self.title_label2.setAlignment(QtCore.Qt.AlignCenter)
        self.title_label2.setObjectName("title_label2")
        self.mail_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.mail_edit.setGeometry(QtCore.QRect(310, 250, 340, 50))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(20)
        self.mail_edit.setFont(font)
        self.mail_edit.setStyleSheet("QLineEdit{\n"
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
        self.mail_edit.setReadOnly(False)
        self.mail_edit.setObjectName("mail_edit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.back_to_login.clicked.connect(self.logic.go_to_login)
        self.reset_password_button.clicked.connect(self.logic.send_mail)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.logo.setText(
            _translate("MainWindow", "<html><head/><body><p><img src=\":/photos/logo.png\"/></p></body></html>"))
        self.title_label.setText(_translate("MainWindow", "Enter your email address"))
        self.reset_password_button.setText(_translate("MainWindow", "reset password"))
        self.back_to_login.setText(_translate("MainWindow", "Back to login"))


import photos_rc
