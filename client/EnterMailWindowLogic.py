import LoginWindow
from PyQt5 import QtCore, QtWidgets


class EnterMailWindowLogic:
    def __init__(self, window, socket, listener):
        self.window = window
        self.socket = socket
        self.listener = listener

    def go_to_login(self):
        ui = LoginWindow.UiLoginWindow()
        ui.setup_ui(self.window.window, self.socket, self.listener)

    def send_mail(self):
        self.window.invalid_label.hide()
        mail = self.window.mail_edit.text().strip()
        if mail == "":
            self.window.invalid_label.setText("Enter an address")
            self.window.invalid_label.show()
            return
        self.socket.send({"type": "reset password", "address": mail})
        self.wait_for_code(mail)

    def wait_for_code(self, mail):
        self.window.invalid_label.setText("Invalid code")
        self.window.reset_password_button.setText("Submit")
        self.window.title_label.setText("Enter authentication code")
        self.window.title_label2.setText("Code was sent to " + mail)
        self.window.mail_edit.setText("")
        self.window.reset_password_button.clicked.disconnect()
        self.window.reset_password_button.clicked.connect(lambda x: self.submit_code(mail))

    def submit_code(self, mail):
        code = self.window.mail_edit.text()
        if code == "":
            self.window.invalid_label.show()
            return
        self.listener.connect(self.check_code_status)
        self.socket.send({"type": "check code", "code": code, "mail": mail})

    def check_code_status(self, status):
        success = status["success"]
        if success:
            self.window.invalid_label.hide()
            self.wait_for_passwords(status["mail"])
        else:
            self.window.invalid_label.show()

    def wait_for_passwords(self, mail):
        self.window.title_label.setText("Enter your new password")
        self.window.mail_edit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.window.mail_edit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.window.title_label2.setText("")
        self.window.reset_password_button.setText("Submit")
        self.window.reset_password_button.clicked.disconnect()
        self.window.mail_edit.setGeometry(QtCore.QRect(310, 200, 340, 50))
        self.window.mail_edit.setText("")
        self.window.mail_edit_2.show()
        self.window.reset_password_button.clicked.connect(lambda x: self.submit_passwords(mail))

    def submit_passwords(self, mail):
        self.window.invalid_label.hide()
        password = self.window.mail_edit.text()
        confirm_password = self.window.mail_edit_2.text()
        self.socket.send(
            {"type": "new password", "password": password, "confirm_password": confirm_password, "mail": mail})
        self.listener.connect(self.check_passwords_status)

    def check_passwords_status(self, status):
        success = status["success"]
        if success:
            self.go_to_login()
        else:
            self.window.invalid_label.setText(status["messages"][0][0])
            self.window.invalid_label.show()
