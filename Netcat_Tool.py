import argparse
import sys
import socket
import threading

def main():
    parser = argparse.ArgumentParser(description="Simple netcat tool")
    parser.add_argument("-l", "--listen", action = "store_true", help= "listen on [host]:[port] for incoming connections")
    parser.add_argument("-t", "--target", type=str, help= "target_host")
    parser.add_argument("-p", "--port", type=int, default= 0, help="target_port")
    parser.add_argument("-r", "--recieve_first", action= "store_true", help= "recieve data before sending")

    args = parser.parse_args()

    if not args.listen and args.target and args.port > 0 :
        buffer = sys.stdin.read()
        client_sender(buffer, args.target, args.port, args.recieve_first)

    if args.listen:
        server_loop('0.0.0.0', args.port, args.target, args.port, args.recieve_first)

def client_sender(buffer, target_host, target_port, recieve_first):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        client.connect((target_host, target_port))

        if buffer:
            client.send(buffer.encode())

        response = client.recv(4096)
        print("Response:", response)

    except Exception as e:
        print("error: {e}")

    finally:
        client.close()

              
def server_loop(local_host, local_port, target_host, target_port, recieve_first):
    
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((local_host, local_port))
    server.listen()
    while True:
        client_socket, addr = server.accept()
        print("Incoming client connections from", addr)
    
    client_thread  = threading.Thread(target = handle_client, args = (cleint_socket, target_host, target_port, recieve_first))
    client_thread.start()


def handle_client(client_socket, target_host, target_port, recieve_first):
    target_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    target_socket.bind((target_host, target_port))
    target_socket.connect()

    if recieve_first:
        target_buffer = target_socket.recv()
        client_socket.send(target_buffer)

    while True:

        local_buffer = client_socket.recv()

        if len(local_buffer):
            target_socket.send(local_buffer)

        target_buffer = target_socket.recv()

        if len(target_buffer):
            client_socket.send(target_buffer)

        if not len(local_buffer) or not len(target_buffer):
            client_socket.close()
            target_socket.close()
            break