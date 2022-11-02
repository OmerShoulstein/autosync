import SignupWindow
import MainWindow
import EnterMailWindow
from PyQt5 import QtWidgets


class LoginLogic:
    def __init__(self, window, socket, listener):
        self.window = window
        self.socket = socket
        self.listener = listener

    def show_password(self):
        self.window.password_edit.setEchoMode(QtWidgets.QLineEdit.Normal)

    def hide_password(self):
        self.window.password_edit.setEchoMode(QtWidgets.QLineEdit.Password)

    def go_to_signup(self):
        ui = SignupWindow.UiSignupWindow()
        ui.setup_ui(self.window.window, self.socket, self.listener)

    def check_login(self, status):
        success = status["success"]
        if success == "dummy":
            return
        if success:
            ui = MainWindow.UiMainWindow()
            ui.setup_ui(self.window.window, status["message"], self.socket, self.listener)
        else:
            self.window.wrong_password_label.setText("Invalid username or password")
            self.window.wrong_password_label.show()

    def login(self):
        self.listener.connect(self.check_login)
        self.window.wrong_password_label.hide()
        username = self.window.username_edit.text()
        password = self.window.password_edit.text()
        self.socket.send({"type": "login", "username": username, "password": password})

    def forgot_password(self):
        ui = EnterMailWindow.UiEnterMailWindow()
        ui.setup_ui(self.window.window, self.socket, self.listener)
