from PyQt5 import QtCore, QtGui, QtWidgets
import LoginLogic


class UiLoginWindow:
    def setup_ui(self, loginWindow, socket, listener):
        self.socket = socket
        self.window = loginWindow
        self.window.closeEvent = lambda x: self.socket.send({"type": "stop"})
        self.logic = LoginLogic.LoginLogic(self, socket, listener)
        loginWindow.setObjectName("loginWindow")
        loginWindow.setEnabled(True)
        loginWindow.resize(960, 540)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(loginWindow.sizePolicy().hasHeightForWidth())
        loginWindow.setSizePolicy(sizePolicy)
        loginWindow.setMinimumSize(QtCore.QSize(960, 540))
        loginWindow.setMaximumSize(QtCore.QSize(960, 540))
        loginWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        loginWindow.setStyleSheet("background-color: rgb(244, 250, 255);")
        self.centralwidget = QtWidgets.QWidget(loginWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(-1, 0, 200, 145))
        self.logo.setObjectName("logo")
        self.username_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.username_edit.setGeometry(QtCore.QRect(340, 140, 280, 50))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(20)
        self.username_edit.setFont(font)
        self.username_edit.setStyleSheet("QLineEdit{\n"
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
        self.username_edit.setObjectName("username_edit")
        self.usernam_label = QtWidgets.QLabel(self.centralwidget)
        self.usernam_label.setGeometry(QtCore.QRect(100, 140, 280, 50))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(20)
        self.usernam_label.setFont(font)
        self.usernam_label.setStatusTip("")
        self.usernam_label.setWhatsThis("")
        self.usernam_label.setAutoFillBackground(False)
        self.usernam_label.setStyleSheet("background-color: rgba(0, 0, 0,0);")
        self.usernam_label.setAlignment(QtCore.Qt.AlignCenter)
        self.usernam_label.setObjectName("usernam_label")
        self.password_label = QtWidgets.QLabel(self.centralwidget)
        self.password_label.setGeometry(QtCore.QRect(100, 250, 280, 50))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(20)
        self.password_label.setFont(font)
        self.password_label.setStatusTip("")
        self.password_label.setWhatsThis("")
        self.password_label.setAutoFillBackground(False)
        self.password_label.setStyleSheet("background-color: rgba(0, 0, 0,0);")
        self.password_label.setAlignment(QtCore.Qt.AlignCenter)
        self.password_label.setObjectName("password_label")
        self.password_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.password_edit.setGeometry(QtCore.QRect(340, 250, 280, 50))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(20)
        self.password_edit.setFont(font)
        self.password_edit.setStyleSheet("QLineEdit{\n"
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
        self.password_edit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_edit.setObjectName("password_edit")
        self.Login_button = QtWidgets.QPushButton(self.centralwidget)
        self.Login_button.setGeometry(QtCore.QRect(340, 360, 280, 50))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(20)
        self.Login_button.setFont(font)
        self.Login_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Login_button.setStyleSheet("background-color: rgb(77, 183, 249);\n"
                                        "alternate-background-color: rgb(77, 183, 249);\n"
                                        "color: rgb(255, 255, 255);\n"
                                        "border-radius:10px;")
        self.Login_button.setObjectName("Login_button")
        self.password_button = QtWidgets.QPushButton(self.centralwidget)
        self.password_button.setGeometry(QtCore.QRect(320, 425, 320, 35))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(20)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setKerning(False)
        self.password_button.setFont(font)
        self.password_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.password_button.setStyleSheet("border: none;\n"
                                           "background-color: rgba(0, 0, 0,0);\n"
                                           "color: rgb(77, 183, 249);")
        self.password_button.setCheckable(False)
        self.password_button.setObjectName("password_button")
        self.signup_label = QtWidgets.QLabel(self.centralwidget)
        self.signup_label.setGeometry(QtCore.QRect(290, 470, 320, 50))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.signup_label.setFont(font)
        self.signup_label.setStyleSheet("background-color: rgba(0, 0, 0,0);")
        self.signup_label.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.signup_label.setObjectName("signup_label")
        self.signup_button = QtWidgets.QPushButton(self.centralwidget)
        self.signup_button.setGeometry(QtCore.QRect(600, 474, 120, 40))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(20)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.signup_button.setFont(font)
        self.signup_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.signup_button.setStyleSheet("border: none;\n"
                                         "background-color: rgba(0, 0, 0,0);\n"
                                         "color: rgb(77, 183, 249);")
        self.signup_button.setObjectName("signup_button")
        self.wrong_password_label = QtWidgets.QLabel(self.centralwidget)
        self.wrong_password_label.setGeometry(QtCore.QRect(295, 290, 370, 50))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(14)
        self.wrong_password_label.setFont(font)
        self.wrong_password_label.setStyleSheet("color: rgb(239, 41, 41);\n"
                                                "background-color: rgba(0, 0, 0,0);")
        self.wrong_password_label.setText("")
        self.wrong_password_label.setAlignment(QtCore.Qt.AlignCenter)
        self.wrong_password_label.setObjectName("wrong_password_label")
        self.show_password_button = QtWidgets.QPushButton(self.centralwidget)
        self.show_password_button.setGeometry(QtCore.QRect(625, 250, 35, 35))
        self.show_password_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.show_password_button.setStyleSheet("image: url(:/photos/eye_icon.svg);\n"
                                                "background-image:url(:/photos/eye_icon.svg);\n"
                                                "background-color: rgba(0, 0, 0,0);")
        self.show_password_button.setText("")
        self.show_password_button.setObjectName("show_password_button")
        loginWindow.setCentralWidget(self.centralwidget)

        self.retranslate_ui(loginWindow)
        self.Login_button.clicked.connect(self.logic.login)
        self.password_button.clicked.connect(self.logic.forgot_password)
        self.signup_button.clicked.connect(self.logic.go_to_signup)
        self.show_password_button.pressed.connect(self.logic.show_password)
        self.show_password_button.released.connect(self.logic.hide_password)

        QtCore.QMetaObject.connectSlotsByName(loginWindow)

    def retranslate_ui(self, loginWindow):
        _translate = QtCore.QCoreApplication.translate
        loginWindow.setWindowTitle(_translate("loginWindow", "MainWindow"))
        self.logo.setText(
            _translate("loginWindow", "<html><head/><body><p><img src=\":/photos/logo.png\"/></p></body></html>"))
        self.usernam_label.setText(_translate("loginWindow", "Username:"))
        self.password_label.setText(_translate("loginWindow", "Password:"))
        self.Login_button.setText(_translate("loginWindow", "Log In"))
        self.password_button.setText(_translate("loginWindow", "Forgot your password?"))
        self.signup_label.setText(_translate("loginWindow", "don\'t have an account? "))
        self.signup_button.setText(_translate("loginWindow", "Sign up"))

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    loginWindow = QtWidgets.QMainWindow()
    ui = UiLoginWindow()
    ui.setup_ui(loginWindow)
    loginWindow.show()
    sys.exit(app.exec_())
