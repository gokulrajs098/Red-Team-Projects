import socket
import threading

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ("127.0.0.1", 1234)
    server_socket.bind(server_address)
    server_socket.listen()

    clients = []

    while True:
        client_socket, client_address = server_socket.accept(1024)
        handler = threading.Thread(target = handle_client, args = (client_socket, client_address, clients))
        handler.start()

def handle_client(client_socket, client_address, clients):
    clients.append(client_socket)

    while True:
        data = client_socket.recv()
        if not data:
            break

    text = data.decode()
    message = encryption(text, 6)

    broadcast(message, clients)

    client_socket.close()
    clients.remove(client_socket)

def encryption(text, key):
    cipher = ""

    for char in text:

        if char.islower():
            cipher += chr((ord(char) + key - 97) % 26 + 97)

        elif char.isupper():
            cipher += chr((ord(char) + key - 65) % 26 + 65)

        else:
            cipher += char

    return cipher

def broadcast(message, clients):

    for client in clients:
        client.send(message.encode())
        client.close()




    

