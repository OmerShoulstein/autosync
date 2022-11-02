from PyQt5 import QtCore


class Listener(QtCore.QThread):
    signal = QtCore.pyqtSignal(dict)

    def __init__(self, sock):
        super(Listener, self).__init__()
        self.socket = sock
        self.done = False
        self.function = None

    def connect(self, function):
        if self.function is not None:
            self.signal.disconnect(self.function)
        self.function = function
        self.signal.connect(self.function)

    def run(self):
        while not self.done:
            try:
                data = self.socket.recv()
                self.signal.emit(data)

            except:
                self.done = True
