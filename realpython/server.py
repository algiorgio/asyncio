import socket

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 5002        # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.bind((HOST, PORT))
    sock.listen()
    conn, addr = sock.accept()
    print('Conn: {}'.format(conn))
    print('Addr: {}'.format(addr))
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(4096)
            print(data)
            if not data :
                break
            conn.sendall(data)
