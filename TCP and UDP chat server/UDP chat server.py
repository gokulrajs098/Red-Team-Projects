import socket 
import threading

def main():

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ("127.0.0.1", 1234)
    server_socket.bind(server_address)

    recieve_thread = threading.Thread(target = recieve_messages, args = (server_socket))
    sending_thread = threading.Thread(target = sending_messages, args = (server_socket))
    recieve_thread.start()
    sending_thread.start()

def recieve_messages(sock):
    while True:
        data, addr = sock.recv()
        print("Recieved messages from {addr}: {data.decode()}")

def sending_messages(sock):
    while True:
        message = input("Enter the message: ")
        sock.sendto(message.encode(), ('127.0.0.1', 1234))

if __name__ == "__main__":
    main()

    
