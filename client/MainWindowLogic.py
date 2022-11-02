import threading
from tkinter import filedialog, Tk
import time
from utils import ClientEndpoint


class MainWindowLogic:
    def __init__(self, window, username, socket, listener):
        self.window = window
        self.username = username
        self.socket = socket
        self.listener = listener

    def sync(self, path):
        client_endpoint = ClientEndpoint(None, path)
        client_endpoint.socket = self.socket
        state = self.socket.recv()
        if state["type"] == "new":
            client_endpoint.upload_folder()
        else:
            self.socket.send({"type": "SYNC", "version": str(client_endpoint.version)})
            client_endpoint.download_folder()
        self.socket.send({"type": "bye"})

        while True:
            client_endpoint.sync()
            self.socket.send({"type": "bye"})
            time.sleep(1)

    def start_sync(self):
        self.listener.done = True
        directory = self.window.browse_edit.text()
        if directory != "":
            self.socket.send({"type": "sync", "username": self.username})
            with open("user_folders/"+self.username, 'w') as file:
                file.write(directory)
            sync_thread = threading.Thread(target=self.sync, daemon=True,
                                           args=(directory,))
            sync_thread.start()
        else:
            self.window.select_folder_label.setText("Select a folder first!")
            self.window.select_folder_label.show()

    def browse(self):
        root = Tk()
        root.withdraw()
        folder_selected = filedialog.askdirectory()
        if folder_selected == "":
            return
        self.window.select_folder_label.hide()
        try:
            self.window.browse_edit.setText(folder_selected)
        except TypeError:
            return
