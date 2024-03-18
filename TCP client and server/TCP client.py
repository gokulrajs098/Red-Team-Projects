import socket

# Creating a Socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connecting to the server
server_address = ('127.0.0.1',12345)
client_socket.connect(server_address)

try:

    # Sending a Message
    message = "Hello server!"
    print("Sending message", message)
    client_socket.sendall(message.encode())

finally:
    client_socket.close()


