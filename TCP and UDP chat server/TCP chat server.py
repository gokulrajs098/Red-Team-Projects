import socket
import threading

def main():

    # Creating a Socket function
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ("127.0.0.1", 1234)
    
    # Binding server address
    server_socket.bind(server_address)

    server_socket.listen()
    # server liatening on port 1234

    clients = []

    while True:
        
        # Accepting incoming connections
        client_address, client_socket = server_socket.accept()
        client_handle = threading.Thread(target = handle_client, args = (clients, client_socket, client_address))
        client_handle.start()

def handle_client(clients, client_socket, client_address):
    
    # Accepting incoming clients
    clients.append(client_socket)

    while True:
        try:    
            data = client_socket.recv(1024)
            if not data:
                break

            message = f"{client_address}: {data:decode()}"

            broadcast(message, clients)

        except Exception as e:
            print(f"client error handling: {e}")
            break

    clients.remove(client_socket)
    client_socket.close

    print(f"Connection from {client_address} closed.")

def broadcast(message, clients):
    for client in clients:
        try:
            client.send(message.encode())
        except Exception as e:
            print(f"Error broadcasting message to all: {e}")
            client.close()


if __name__ == "__main__":
    main()














