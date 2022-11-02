from PyQt5 import QtCore, QtGui, QtWidgets

import SignupLogic


class UiSignupWindow(object):
    def setup_ui(self, signupWindow, socket, listener):
        self.window = signupWindow
        self.logic = SignupLogic.SignupLogic(self, socket, listener)
        self.invalid_messages = []
        signupWindow.setObjectName("signupWindow")
        signupWindow.resize(960, 540)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(signupWindow.sizePolicy().hasHeightForWidth())
        signupWindow.setSizePolicy(sizePolicy)
        signupWindow.setMinimumSize(QtCore.QSize(960, 540))
        signupWindow.setMaximumSize(QtCore.QSize(960, 540))
        signupWindow.setStyleSheet("background-color: rgb(244, 250, 255);")
        self.centralwidget = QtWidgets.QWidget(signupWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(-1, 0, 200, 145))
        self.logo.setObjectName("logo")
        self.username_label = QtWidgets.QLabel(self.centralwidget)
        self.username_label.setGeometry(QtCore.QRect(170, 115, 280, 50))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(20)
        self.username_label.setFont(font)
        self.username_label.setStyleSheet("background-color: rgba(0, 0, 0,0);")
        self.username_label.setAlignment(QtCore.Qt.AlignCenter)
        self.username_label.setObjectName("username_label")
        self.username_question_mark = QtWidgets.QLabel(self.centralwidget)
        self.username_question_mark.setGeometry(QtCore.QRect(390, 130, 20, 20))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.username_question_mark.setFont(font)
        self.username_question_mark.setStyleSheet("background-image: url(:/photos/question_mark.svg);\n"
                                                  "image:url(:/photos/question_mark.svg);")
        self.username_question_mark.setObjectName("username_question_mark")
        self.username_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.username_edit.setGeometry(QtCore.QRect(170, 170, 280, 50))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
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
        self.password_label = QtWidgets.QLabel(self.centralwidget)
        self.password_label.setGeometry(QtCore.QRect(170, 270, 280, 50))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(20)
        self.password_label.setFont(font)
        self.password_label.setStyleSheet("background-color: rgba(0, 0, 0,0);")
        self.password_label.setAlignment(QtCore.Qt.AlignCenter)
        self.password_label.setObjectName("password_label")
        self.password_question_mark = QtWidgets.QLabel(self.centralwidget)
        self.password_question_mark.setGeometry(QtCore.QRect(385, 285, 20, 20))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.password_question_mark.setFont(font)
        self.password_question_mark.setStyleSheet("background-image: url(:/photos/question_mark.svg);\n"
                                                  "image:url(:/photos/question_mark.svg);")
        self.password_question_mark.setObjectName("password_question_mark")
        self.email_label = QtWidgets.QLabel(self.centralwidget)
        self.email_label.setGeometry(QtCore.QRect(510, 115, 280, 50))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(20)
        self.email_label.setFont(font)
        self.email_label.setStyleSheet("background-color: rgba(0, 0, 0,0);")
        self.email_label.setAlignment(QtCore.Qt.AlignCenter)
        self.email_label.setObjectName("email_label")
        self.email_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.email_edit.setGeometry(QtCore.QRect(510, 170, 280, 50))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.email_edit.setFont(font)
        self.email_edit.setStyleSheet("QLineEdit{\n"
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
        self.email_edit.setObjectName("email_edit")
        self.email_question_mark = QtWidgets.QLabel(self.centralwidget)
        self.email_question_mark.setGeometry(QtCore.QRect(700, 130, 20, 20))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.email_question_mark.setFont(font)
        self.email_question_mark.setStyleSheet("background-image: url(:/photos/question_mark.svg);\n"
                                                  "image:url(:/photos/question_mark.svg);")
        self.email_question_mark.setObjectName("email_question_mark")
        self.password_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.password_edit.setGeometry(QtCore.QRect(170, 320, 280, 50))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
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
        self.confirm_password_label = QtWidgets.QLabel(self.centralwidget)
        self.confirm_password_label.setGeometry(QtCore.QRect(510, 270, 280, 50))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(20)
        self.confirm_password_label.setFont(font)
        self.confirm_password_label.setStyleSheet("background-color: rgba(0, 0, 0,0);")
        self.confirm_password_label.setAlignment(QtCore.Qt.AlignCenter)
        self.confirm_password_label.setObjectName("confirm_password_label")
        self.confirm_password_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.confirm_password_edit.setGeometry(QtCore.QRect(510, 320, 280, 50))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(20)
        self.confirm_password_edit.setFont(font)
        self.confirm_password_edit.setStyleSheet("QLineEdit{\n"
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
        self.confirm_password_edit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirm_password_edit.setObjectName("confirm_password_edit")
        self.signup_button = QtWidgets.QPushButton(self.centralwidget)
        self.signup_button.setGeometry(QtCore.QRect(340, 420, 280, 50))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(20)
        self.signup_button.setFont(font)
        self.signup_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.signup_button.setStyleSheet("background-color: rgb(77, 183, 249);\n"
                                         "color: rgb(255, 255, 255);\n"
                                         "border-radius:10px;")
        self.signup_button.setObjectName("signup_button")
        self.login_label = QtWidgets.QLabel(self.centralwidget)
        self.login_label.setGeometry(QtCore.QRect(290, 470, 360, 50))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.login_label.setFont(font)
        self.login_label.setStyleSheet("background-color: rgba(0, 0, 0,0);")
        self.login_label.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.login_label.setObjectName("login_label")
        self.login_button = QtWidgets.QPushButton(self.centralwidget)
        self.login_button.setGeometry(QtCore.QRect(640, 470, 100, 50))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(20)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.login_button.setFont(font)
        self.login_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.login_button.setStyleSheet("border: none;\n"
                                        "background-color: rgba(0, 0, 0,0);\n"
                                        "color: rgb(77, 183, 249);")
        self.login_button.setObjectName("login_button")
        self.invalid_username_label = QtWidgets.QLabel(self.centralwidget)
        self.invalid_username_label.setGeometry(QtCore.QRect(140, 215, 340, 50))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(14)
        self.invalid_username_label.setFont(font)
        self.invalid_username_label.setStyleSheet("color: rgb(239, 41, 41);\n"
                                                  "background-color: rgba(0, 0, 0,0);")
        self.invalid_username_label.setText("")
        self.invalid_username_label.setAlignment(QtCore.Qt.AlignCenter)
        self.invalid_username_label.setObjectName("invalid_username_label")
        self.invalid_email_label = QtWidgets.QLabel(self.centralwidget)
        self.invalid_email_label.setGeometry(QtCore.QRect(510, 215, 280, 50))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(14)
        self.invalid_email_label.setFont(font)
        self.invalid_email_label.setStyleSheet("color: rgb(239, 41, 41);\n"
                                               "background-color: rgba(0, 0, 0,0);")
        self.invalid_email_label.setText("")
        self.invalid_email_label.setAlignment(QtCore.Qt.AlignCenter)
        self.invalid_email_label.setObjectName("invalid_email_label")
        self.invalid_password_label = QtWidgets.QLabel(self.centralwidget)
        self.invalid_password_label.setGeometry(QtCore.QRect(135, 365, 350, 50))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(14)
        self.invalid_password_label.setFont(font)
        self.invalid_password_label.setStyleSheet("color: rgb(239, 41, 41);\n"
                                                  "background-color: rgba(0, 0, 0,0);")
        self.invalid_password_label.setText("")
        self.invalid_password_label.setAlignment(QtCore.Qt.AlignCenter)
        self.invalid_password_label.setObjectName("short_password_label")
        self.password_mismatch_label = QtWidgets.QLabel(self.centralwidget)
        self.password_mismatch_label.setGeometry(QtCore.QRect(490, 365, 320, 50))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(14)
        self.password_mismatch_label.setFont(font)
        self.password_mismatch_label.setStyleSheet("color: rgb(239, 41, 41);\n"
                                                   "background-color: rgba(0, 0, 0,0);")
        self.password_mismatch_label.setText("")
        self.password_mismatch_label.setAlignment(QtCore.Qt.AlignCenter)
        self.password_mismatch_label.setObjectName("password_mismatch_label")
        signupWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(signupWindow)
        self.signup_button.clicked.connect(self.logic.signup)
        self.login_button.clicked.connect(self.logic.go_to_login)
        QtCore.QMetaObject.connectSlotsByName(signupWindow)

    def retranslateUi(self, signupWindow):
        _translate = QtCore.QCoreApplication.translate
        signupWindow.setWindowTitle(_translate("signupWindow", "MainWindow"))
        self.logo.setText(
            _translate("signupWindow", "<html><head/><body><p><img src=\":/photos/logo.png\"/></p></body></html>"))
        self.username_label.setText(_translate("signupWindow", "Username"))
        self.username_question_mark.setToolTip(_translate("signupWindow",
                                                          "<html><head/><body><p><span style=\" font-size:15pt;\">Username has to include at least 3 alphanumerics</span></p></body></html>"))
        self.username_question_mark.setText(_translate("signupWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.email_question_mark.setToolTip(_translate("signupWindow",
                                                       "<html><head/><body><p><span style=\" font-size:15pt;\">Enter a valid e-mail address</span></p></body></html>"))
        self.email_question_mark.setText(_translate("signupWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.password_label.setText(_translate("signupWindow", "Password"))
        self.password_question_mark.setToolTip(_translate("signupWindow",
                                                          "<html><head/><body><p><span style=\" font-size:15pt;\">Password must include at least 8 characters, a lowercase, an uppercase and a digit.</span></p></body></html>"))
        self.password_question_mark.setText(_translate("signupWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.email_label.setText(_translate("signupWindow", "E-mail"))
        self.confirm_password_label.setText(_translate("signupWindow", "Confirm password"))
        self.signup_button.setText(_translate("signupWindow", "Sign Up"))
        self.login_label.setText(_translate("signupWindow", "Already have an account? "))
        self.login_button.setText(_translate("signupWindow", "Log in"))


import photos_rc

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    signupWindow = QtWidgets.QMainWindow()
    ui = UiSignupWindow()
    ui.setup_ui(signupWindow)
    signupWindow.show()
    sys.exit(app.exec_())
