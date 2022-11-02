import LoginWindow
import MainWindow


class SignupLogic:
    def __init__(self, window, socket, listener):
        self.window = window
        self.socket = socket
        self.listener = listener

    def go_to_login(self):
        ui = LoginWindow.UiLoginWindow()
        ui.setup_ui(self.window.window, self.socket, self.listener)

    def check_signup(self, status):
        self.window.invalid_username_label.setText("")
        self.window.invalid_email_label.setText("")
        self.window.invalid_password_label.setText("")
        self.window.password_mismatch_label.setText("")
        success = status["success"]
        if success == "dummy":
            return
        if success:
            ui = MainWindow.UiMainWindow()
            ui.setup_ui(self.window.window, status["messages"], self.socket, self.listener)
        else:
            for message in status["messages"]:
                if message[1] == "username":
                    self.window.invalid_username_label.setText(message[0])
                elif message[1] == "email":
                    self.window.invalid_email_label.setText(message[0])
                elif message[1] == "password":
                    self.window.invalid_password_label.setText(message[0])
                elif message[1] == "confirm_password":
                    self.window.password_mismatch_label.setText(message[0])

    def signup(self):
        for message in self.window.invalid_messages:
            message.hide()
        self.listener.connect(self.check_signup)
        username = self.window.username_edit.text()
        password = self.window.password_edit.text()
        email = self.window.email_edit.text()
        confirm_password = self.window.confirm_password_edit.text()
        self.socket.send({"type": "signup", "username": username, "email": email, "password": password,
                          "confirm_password": confirm_password})
