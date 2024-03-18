import socket

# Creating a Socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ("127.0.0.1",12345)

# Bind the ipadddress and Port to listen
server_socket.bind(server_address)

# Start Listening
server_socket.listen(1)
print("Server listening on port 12345")

# Accepting incoming Connections
while True:
    connection, client_address = server_socket.accept()

    try:
        print("Connection from", client_address)

# Recieving Data from client_address
        while True:
            data  = connection.recv(1024)

            if not data:
                break
            print("Recieved", data.decode())

    finally:
        connection.close()
server_socket.close()




