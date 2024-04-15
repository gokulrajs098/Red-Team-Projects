import socket

def main():
    target_host = input("Enter the Host you want to scan:")
    target_port = int(input("Enter the port you want to scan:"))
    scan_port(target_host, target_port)

def scan_port(target_host, target_port):
    try:    
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect((target_host, target_port))
        if result == 0:
            print(f"{target_port} is open")
        else:
            print(f"{target_port} is closed")
    except socket.error:
        print("Couldn't connect to the server")

if __name__ == "__main__":
    main()
            
