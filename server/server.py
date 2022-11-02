import json
import socket
import select
import re
from hashlib import sha256
from random import choices
from string import ascii_letters, digits
from executeQuery import execute_query
import os
from utils import ServerEndpoint, ClosingSocket, DividingSocket, decrypt, SecureSocket
import threading
import rsa
import smtplib
import ssl

versions = {}


def load_private_key():
    with open("rsaKeys/privateKey.pem", 'rb') as f:
        private_key = rsa.PrivateKey.load_pkcs1(f.read())
    return private_key


def load_public_key_bytes():
    with open("rsaKeys/publicKey.pem", 'rb') as f:
        public_key = f.read()
    return public_key


def handle_main(client, username, key):
    client = ClosingSocket(client, key)
    client_id = username
    client.send({"success": "dummy"})
    client_folder = 'folders' + '/' + client_id
    server_endpoint = ServerEndpoint(client, client_folder)
    while True:
        if not os.path.exists(client_folder):
            client.send({"type": "new"})
            os.makedirs('folders' + '/' + client_id, exist_ok=True)
            server_endpoint.directory = 'folders' + '/' + client_id
            versions[client_id] = []
            server_endpoint.download_folder()
        else:
            client.send({"type": "old"})
            msg = client.recv()
            version = int(msg["version"])
            if client_id not in versions.keys():
                versions[client_id] = []
            server_endpoint.sync(versions[client_id], version)

        msg = client.recv()
        # Sync until client disconnects
        while msg["type"] != "bye":
            if msg["type"] == "SYNC":
                server_endpoint.sync(versions[client_id], msg["version"])
            msg = client.recv()


def insert_to_db(data):
    username = data["username"]
    password = data["password"]
    email = data["email"]
    password_hash = sha256()
    password_hash.update(password.encode())
    n = 10
    salt = ''.join(choices(ascii_letters + digits, k=n))
    password_hash.update(salt.encode())
    execute_query("INSERT INTO users (username, email, password, salt) VALUES (?, ?, ?, ?)",
                  (username, email, password_hash.hexdigest(), salt))


def validate_password(password, confirm_password):
    result = dict()
    result["messages"] = []
    valid = True
    if len(password) < 8:
        result["type"] = "reset_answer"
        result["success"] = False
        result["messages"].append(("Password is too short", "password"))
        valid = False
    elif not re.search('[0-9]', password):
        result["type"] = "reset_answer"
        result["success"] = False
        result["messages"].append(("Password must contain a digit", "password"))
        valid = False
    elif not re.search('[a-z]', password):
        result["type"] = "reset_answer"
        result["success"] = False
        result["messages"].append(("Password must contain a lowercase", "password"))
        valid = False
    elif not re.search('[A-Z]', password):
        result["type"] = "reset_answer"
        result["success"] = False
        result["messages"].append(("Password must contain an uppercase", "password"))
        valid = False
    if confirm_password != password:
        result["type"] = "reset_answer"
        result["success"] = False
        result["messages"].append(("Passwords do not match", "confirm_password"))
        valid = False
    return result, valid


def handle_signup(data, client_socket):
    result = dict()
    username = data["username"]
    password = data["password"]
    confirm_password = data["confirm_password"]
    email = data["email"]
    valid = True
    result["messages"] = []
    if len(execute_query("select username from users where username= ?", (username,))) != 0:
        result["type"] = "signup_answer"
        result["success"] = False
        result["messages"].append(("Username already in use", "username"))
        valid = False
    elif len(username) < 3:
        result["type"] = "signup_answer"
        result["success"] = False
        result["messages"].append(("Invalid username length", "username"))
        valid = False
    elif not username.isalnum():
        result["type"] = "signup_answer"
        result["success"] = False
        result["messages"].append(("Username must be alphanumeric", "username"))
        valid = False
    if not bool(re.fullmatch(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[a-zA-Z]{2,}\b', email)):
        result["type"] = "signup_answer"
        result["success"] = False
        result["messages"].append(("Invalid e-mail address", "email"))
        valid = False
    elif len(execute_query("select email from users where email= ?", (email,))):
        result["type"] = "signup_answer"
        result["success"] = False
        result["messages"].append(("Email already in use", "email"))
        valid = False
    password_result, password_valid = validate_password(password, confirm_password)
    if not password_valid:
        result["type"] = "signup_answer"
        result["success"] = False
        result["messages"] += password_result["messages"]
    valid = valid and password_valid
    if valid:
        insert_to_db(data)
        result["type"] = "signup_answer"
        result["success"] = True
        result["messages"] = username
    client_socket.send(result)


def handle_login(data, client_socket):
    result = dict()
    username = data["username"]
    password = data["password"]
    fetched_password = execute_query("SELECT password,salt FROM users WHERE username = ?", (username,))
    if len(fetched_password) == 0:
        result["type"] = "login_answer"
        result["success"] = False
        client_socket.send(result)
    else:
        salt = fetched_password[0][1]
        fetched_password = fetched_password[0][0]
        password_hash = sha256()
        password_hash.update(password.encode())
        password_hash.update(salt.encode())
        if password_hash.hexdigest() != fetched_password:
            result["type"] = "login_answer"
            result["success"] = False
            client_socket.send(result)
        else:
            result["type"] = "login_answer"
            result["success"] = True
            result["message"] = username
            client_socket.send(result)


def send_mail(data, user_passwords):
    code = ''.join(choices(digits, k=6))
    port = 465
    password = 'eigffuksiqbzimrn'
    context = ssl.create_default_context()
    sender = "autosyncCyber@gmail.com"
    address = data["address"]
    receiver = address
    usernames = execute_query("SELECT username FROM users WHERE email = ?", (address,))
    if len(usernames) == 0:
        return
    username = usernames[0][0]
    user_passwords[address] = code
    message = """\
    Autosync authentication code for %s

    Your code is %s """ % (username, code)
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(sender, password)
        server.sendmail(sender, receiver, message)


def main():
    os.makedirs("folders", exist_ok=True)
    server_port = 54321
    server_ip = "0.0.0.0"
    client_sockets = []
    private_key = load_private_key()
    public_key = load_public_key_bytes()
    keys = dict()
    user_passwords = dict()
    with socket.socket() as server:
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind((server_ip, server_port))
        server.listen()
        print('server is running')
        while True:
            rlist, wlist, xlist = select.select([server] + client_sockets, [], [])
            for current_socket in rlist:
                if current_socket is server:
                    client_socket, client_address = server.accept()
                    client_sockets.append(client_socket)
                else:
                    dividing_socket = DividingSocket(current_socket)
                    data = dividing_socket.recv()
                    if 'ciphertext' in data.keys():
                        data = decrypt(data['nonce'].encode('cp437'), data['ciphertext'].encode('cp437'),
                                       data['tag'].encode('cp437'), keys[dividing_socket.socket])
                        data = json.loads(data)
                    if data["type"] == "getPubKey":
                        dividing_socket.send({"key": public_key.decode('cp437')})
                        continue
                    if data["type"] == "getSymKey":
                        cipher = data["secret"]
                        secret = rsa.decrypt(cipher.encode('cp437'), private_key).decode('ascii')
                        keys[dividing_socket.socket] = secret.encode('cp437')
                        continue
                    dividing_socket = SecureSocket(current_socket, keys[current_socket])
                    if data["type"] == "stop":
                        client_sockets.remove(current_socket)
                    elif data["type"] == "login":
                        handle_login(data, dividing_socket)
                    elif data["type"] == "signup":
                        handle_signup(data, dividing_socket)
                    elif data["type"] == "sync":
                        client_sockets.remove(current_socket)
                        username = data["username"]
                        main_thread = threading.Thread(target=handle_main,
                                                       args=(current_socket, username, keys[current_socket]),
                                                       daemon=True)
                        main_thread.start()
                    elif data["type"] == "reset password":
                        send_mail(data, user_passwords)
                    elif data["type"] == "check code":
                        if data["mail"] not in user_passwords.keys():
                            dividing_socket.send({"success": False})
                            continue
                        if data["code"] == user_passwords[data["mail"]]:
                            dividing_socket.send({"success": True, "mail": data["mail"]})
                        else:
                            dividing_socket.send({"success": False})
                    elif data["type"] == "new password":
                        result, password_valid = validate_password(data["password"], data["confirm_password"])
                        if password_valid:
                            hashed_password = sha256()
                            hashed_password.update(data["password"].encode())
                            salt = execute_query("SELECT salt FROM users WHERE email = ?", (data["mail"],))[0][0]
                            hashed_password.update(salt.encode())
                            execute_query("UPDATE users SET password = ? WHERE email = ?",
                                          (hashed_password.hexdigest(), data["mail"]),)
                            dividing_socket.send({"success": True})
                        else:
                            dividing_socket.send(result)


if __name__ == "__main__":
    main()
