import os
import json
from threading import Lock
from Cryptodome.Cipher import AES

lock = Lock()


def encrypt(msg, key):
    cipher = AES.new(key, AES.MODE_EAX)
    nonce = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(msg.encode())
    return nonce, ciphertext, tag


def decrypt(nonce, ciphertext, tag, key):
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    plaintext = cipher.decrypt(ciphertext)
    try:
        cipher.verify(tag)
        return plaintext.decode()
    except:
        return False


class DividingSocket:
    def __init__(self, tcp_socket):
        self.socket = tcp_socket

    def send(self, message):
        message = json.dumps(message)
        message = message.encode()
        message += b"<<done>>"
        self.socket.send(message)

    def recv(self):
        lock.acquire()
        data = b""
        # Receive all files
        while not data.endswith(b"<<done>>"):
            recv = self.socket.recv(1)
            data += recv
        data = data[:-8]
        data = data.decode()
        lock.release()
        return json.loads(data)


class SecureSocket(DividingSocket):
    def __init__(self, tcp_socket, key):
        super().__init__(tcp_socket)
        self.key = key

    def send(self, dict_message):
        dict_message = json.dumps(dict_message)
        nonce, ciphertext, tag = encrypt(dict_message, self.key)
        message = dict()
        message['nonce'] = nonce.decode('cp437')
        message['ciphertext'] = ciphertext.decode('cp437')
        message['tag'] = tag.decode('cp437')
        message = json.dumps(message)
        message = message.encode()
        message += b"<<done>>"
        self.socket.send(message)

    def recv(self):
        data = super().recv()
        nonce, ciphertext, tag = data['nonce'].encode('cp437'), data['ciphertext'].encode('cp437'), data['tag'].encode(
            'cp437')
        result = decrypt(nonce, ciphertext, tag, self.key)
        return json.loads(result)


class ClosingSocket(SecureSocket):
    def __init__(self, tcp_socket, key):
        super().__init__(tcp_socket, key)

    def recv(self):
        data = super().recv()
        if data["type"] == "stop":
            exit()
        return data


class Endpoint:
    def __init__(self, socket: DividingSocket, directory: str):
        self.socket = socket
        self.directory = directory
        self.to_upload = set()

    # Upload a single file
    def __upload_file(self, file_path: str):
        rel_path = os.path.relpath(file_path, self.directory)
        if os.path.exists(file_path):
            if os.path.isfile(file_path):
                with open(file_path, "r", encoding='cp437') as file:
                    content = file.read()
                self.socket.send({"type": "file", "name": rel_path, "content": content})
            elif os.path.isdir(file_path):
                self.socket.send({"type": "folder", "name": rel_path})
        else:
            self.socket.send({"type": "delete", "name": rel_path})

    # Upload a set of files
    def upload_files(self, files: set):
        for file in files:
            self.__upload_file(file)
        self.socket.send({"type": "DONE"})

    # Upload all files in a folder
    def __upload_folder(self, subdirectory):
        for f in os.listdir(subdirectory):
            f_path = subdirectory + '/' + f
            if os.path.isfile(f_path):
                self.__upload_file(f_path)
            elif os.path.isdir(f_path):
                self.__upload_folder(f_path)

    def upload_folder(self):
        self.__upload_folder(self.directory)
        self.socket.send({"type": "DONE"})

    # Download a folder
    def download_folder(self):
        files = set()
        msg = self.socket.recv()
        while msg["type"] != "DONE":
            what = msg["type"]
            # Download a file
            if what == "file":
                path = msg["name"]
                content = msg["content"]
                path = self.directory + '/' + path
                files.add(path)
                os.makedirs(os.path.dirname(path), exist_ok=True)
                with open(path, 'wb') as f:
                    f.write(content.encode('cp437'))
            # Download a directory
            elif what == "directory":
                path = msg["name"]
                files.add(self.directory + '/' + path)
                os.makedirs(self.directory + '/' + path, exist_ok=True)
            # Remove a file or a directory
            elif what == "delete":
                path = msg["name"]
                path = self.directory + '/' + path
                files.add(path)
                if os.path.exists(path):
                    if os.path.isfile(path):
                        os.remove(path)
                    else:
                        for root, dirs, files1 in os.walk(path, topdown=False):
                            for name in files1:
                                os.remove(root + '/' + name)
                            for name in dirs:
                                os.rmdir(root + '/' + name)
                        os.rmdir(path)
            msg = self.socket.recv()
        return files


class ServerEndpoint(Endpoint):
    def sync(self, versions, version):
        # Get version and send files accordingly
        if version == 0:
            self.upload_folder()
            self.socket.send({"type": "version", "version": '1'})
            versions.append(set())
            return
        files_to_upload = set()
        for i in versions[version:]:
            files_to_upload.update(i)
        if version > len(versions):
            versions.append(self.download_folder())
        self.upload_files(files_to_upload.copy())
        self.socket.send({"type": "version", "version": str(len(versions))})
